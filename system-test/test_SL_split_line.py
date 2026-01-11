from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] SL

def test_no_leading_parameter():
    simple_edit_test("5jsl", "abcdefghij\n", "abcde\nfghij\n")

def test_no_leading_parameter_with_insert():
    simple_edit_test("5jsli/m1/", "abcdefghij\n", "abcde\nm1fghij\n")

def test_plus_leading_parameter():
    syntax_error("j+sl", "ab\n")
