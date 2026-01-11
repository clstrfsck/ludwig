import os
import pytest
import sys
from pathlib import Path

ludwig_envs = ["LUDWIG_EXE", "LUDWIG_PATH"]

def _compute_ludwig_path() -> Path:
    use_path = None
    for env_name in ludwig_envs:
        env = os.getenv(env_name)
        if env:
            use_path = Path(os.path.expandvars(env)).expanduser()
            break
    if not use_path:
        use_path = Path(__file__).parent.parent / "src" / "ludwig"
    # normalize but don't require the file to exist during resolution
    use_path = use_path.resolve(strict=False)

    # fail fast if the target doesn't exist or isn't an executable file
    if not use_path.exists():
        raise FileNotFoundError(
            f"Ludwig executable not found at: {use_path!s}.\n"
            f"Set one of {ludwig_envs} to the correct executable path."
        )
    if not use_path.is_file():
        raise FileNotFoundError(f"Ludwig path exists but is not a file: {use_path!s}")
    if not os.access(str(use_path), os.X_OK):
        raise PermissionError(
            f"Ludwig executable at {use_path!s} is not executable; check permissions."
        )

    print(f"Using Ludwig executable at: {use_path}", file=sys.stderr)
    return use_path

_ludwig_path: Path | None = None

def ludwig_path() -> Path:
    if _ludwig_path is None:
        raise RuntimeError("Ludwig path not initialized")
    return _ludwig_path

def pytest_sessionstart(session):
    try:
        global _ludwig_path
        _ludwig_path = _compute_ludwig_path()
    except Exception as exc:
        pytest.exit(f"{exc}", returncode=2)
