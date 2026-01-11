from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + ,   , +n ,    ,   ,   ,   ] I

def test_no_leading_parameter():
    simple_edit_test("i/insert/", "", "insert\n")

def test_plus_leading_parameter():
    simple_edit_test("+i/insert/", "", "insert\n")

def test_n_leading_parameter():
    simple_edit_test("3i/insert/", "", "insertinsertinsert\n")

def test_minus_leading_parameter():
    syntax_error("-i/insert/", "")
