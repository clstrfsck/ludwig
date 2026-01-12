from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    ,   ,   ,   ] ZC

def test_no_leading_parameter():
    simple_edit_test("10jzci/b/", "12345678901234567890\n", "12345678901234567890\nb\n")

def test_plus_leading_parameter():
    simple_edit_test("ep/o=n/10jzci/b/", "12345678901234567890\n", "1234567890\nb1234567890\n")

def test_positive_leading_parameter():
    simple_edit_test("10j2zci/b/", "12345678901234567890\n", "12345678901234567890\n\nb\n")

def test_positive_leading_parameter_split():
    simple_edit_test("ep/o=n/10j3zci/b/", "12345678901234567890\n", "1234567890\nb1234567890\n")
