import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, Tuple, Optional, Sequence
from conftest import ludwig_path

def _write_files(base_path: str, files: Dict[str, str]) -> None:
    for relpath, content in files.items():
        target = os.path.join(base_path, relpath)
        parent = os.path.dirname(target)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        # mark likely executables as executable (scripts)
        if relpath.endswith(".sh") or relpath.endswith(".py"):
            try:
                st = os.stat(target)
                os.chmod(target, st.st_mode | 0o111)
            except Exception:
                pass


def _collect_files(base_path: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for root, _, files in os.walk(base_path):
        for fn in files:
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, base_path)
            try:
                with open(full, "r", encoding="utf-8", errors="surrogateescape") as f:
                    out[rel] = f.read()
            except Exception:
                # fall back to binary read decoded with latin-1
                with open(full, "rb") as f:
                    out[rel] = f.read().decode("latin-1")
    return out


def run_in_sandbox(
    files_map: Dict[str, str],
    stdin: str,
    executable: Path,
    argv: Optional[Sequence[str]] = None,
    timeout: int = 10,
    env: Optional[dict] = {},
) -> Tuple[Dict[str, str], int, list[str], list[str]]:
    """Create a temporary sandbox, write `files_map`, run `executable` with `stdin`.

    Returns `(files_after_map, returncode, stdout, stderr)`.

    Parameters
    - `files_map`: mapping of relative paths -> initial file contents to create inside the sandbox
    - `stdin`: string to send to the child process's stdin
    - `executable`: path to executable inside the sandbox (e.g. './prog.py') or absolute path
    - `argv`: optional sequence of additional command-line arguments (not including the executable)
    - `env`: if `None`, child inherits parent env; if provided (including `{}`), the child will use that env
    """

    with tempfile.TemporaryDirectory() as td:
        _write_files(td, files_map)
        cmd: Sequence[str]
        if argv:
            cmd = [str(executable), "-M", "-I"] + list(argv)
        else:
            cmd = [str(executable), "-M", "-I"]

        proc = subprocess.run(
            cmd,
            input=stdin.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=td,
            timeout=timeout,
            env=env,
        )

        files_after = _collect_files(td)
        returncode = proc.returncode
        out = proc.stdout.decode("utf-8", errors="replace")
        err = proc.stderr.decode("utf-8", errors="replace")
        return files_after, returncode, out.splitlines(), err.splitlines()

def simple_edit_test(
    cmd: str,
    infile: str,
    outfile: str,
    argv: Optional[Sequence[str]] = None,
    env: Optional[dict] = None,
) -> None:
    inlines = infile.count('\n')
    outlines = outfile.count('\n')
    files, exit, out, err = run_in_sandbox(
        { "test_file": infile },
        cmd,
        ludwig_path(), (list(argv) if argv else []) + [ "test_file" ],
        env=env
    )
    assert files.keys() == {"test_file", "test_file~1"}
    assert files["test_file~1"] == infile
    assert files["test_file"] == outfile
    assert exit == 0
    assert len(out) == 2
    if inlines == 1:
        assert out[0].endswith(f"/test_file closed (1 line read).")
    else:
        assert out[0].endswith(f"/test_file closed ({inlines} lines read).")
    if outlines == 1:
        assert out[1].endswith(f"/test_file created (1 line written).")
    else:
        assert out[1].endswith(f"/test_file created ({outlines} lines written).")
    assert err == []

def unmodified_test(cmd: str, infile: str, argv: Optional[Sequence[str]] = None) -> None:
    inlines = infile.count('\n')
    files, exit, out, err = run_in_sandbox(
        { "test_file": infile },
        cmd,
        ludwig_path(), (list(argv) if argv else []) + [ "test_file" ]
    )
    assert files.keys() == {"test_file"}
    assert files["test_file"] == infile
    assert exit == 0
    assert len(out) == 1
    if inlines == 1:
        assert out[0].endswith(f"/test_file closed (1 line read).")
    else:
        assert out[0].endswith(f"/test_file closed ({inlines} lines read).")
    assert err == []

def _failed_edit(cmd: str, infile: str, what: str, argv: Optional[Sequence[str]] = None) -> None:
    inlines = infile.count('\n')
    files, exit, out, err = run_in_sandbox(
        { "test_file": infile },
        cmd,
        ludwig_path(), (list(argv) if argv else []) + [ "test_file" ]
    )
    assert files.keys() == {"test_file"}
    assert files["test_file"] == infile
    assert exit == 0
    assert len(out) == 2
    assert out[0].strip().endswith(what)
    if inlines == 1:
        assert out[1].endswith(f"/test_file closed (1 line read).")
    else:
        assert out[1].endswith(f"/test_file closed ({inlines} lines read).")
    assert err == []

def syntax_error(cmd: str, infile: str = "", argv: Optional[Sequence[str]] = None) -> None:
    _failed_edit(cmd, infile, "Syntax error.", argv)

def command_failed(cmd: str, infile: str = "", argv: Optional[Sequence[str]] = None) -> None:
    _failed_edit(cmd, infile, "COMMAND FAILED", argv)
