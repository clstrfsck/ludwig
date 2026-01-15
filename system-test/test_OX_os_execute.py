from systest import simple_edit_test

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] OX

def test_no_leading_parameter():
    simple_edit_test("ti/m1/ox/echo \"This is a test\"/ti/m2/", "", "This is a test\nm2m1\n", ["-O"])
