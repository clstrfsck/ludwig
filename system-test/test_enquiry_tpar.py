from systest import simple_edit_test

# Test that a trailing parameter delimited by ? is replaced by Ludwig variable
# values. Values that are likely to change between test runs (e.g. file names)
# are not tested here.
var_names = [
    "terminal-name",
    "terminal-height",
    "terminal-width",
    "terminal-speed",
    "frame-name",
#    "frame-inputfile",
#    "frame-outputfile",
    "frame-modified",
    "ludwig-version",
    "ludwig-command_introducer",
    "ludwig-insert_mode",
    "ludwig-overtype_mode",
#    "ludwig-opsys",
    "env-TEST_ENV"
]

def test_tpar_enquiry():
    cmd = "".join(f"ti?{var}?kc" for var in var_names)
    simple_edit_test(
        cmd,
        "",
        "\n                   4\n                  80\n                   0\nLUDWIG\nY\nX5.0-006\n\\\nY\nN\ntest-value\n",
        ["-O"], {"TEST_ENV": "test-value"})
