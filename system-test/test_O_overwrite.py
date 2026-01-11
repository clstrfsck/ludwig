from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + ,   , +n ,    ,   ,   ,   ] O

def test_no_leading_parameter():
    simple_edit_test("o/overwrite/", "abcdefghij\n", "overwritej\n")

def test_plus_leading_parameter():
    simple_edit_test("o/overwrite/", "abc\n", "overwrite\n")

def test_n_leading_parameter():
    simple_edit_test("3o/overwrite/", "abcdefghiabcdefghiabcdefghij\n", "overwriteoverwriteoverwritej\n")

def test_minus_leading_parameter():
    syntax_error("-o/overwrite/", "")
