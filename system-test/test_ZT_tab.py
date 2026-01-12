from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    ,   ,   ,   ] ZT

def test_no_leading_parameter():
    simple_edit_test("zti/b/", "12345678901234567890\n", "12345678b901234567890\n")

def test_plus_leading_parameter():
    simple_edit_test("+zti/b/", "12345678901234567890\n", "12345678b901234567890\n")

def test_positive_leading_parameter():
    simple_edit_test("2zti/b/", "12345678901234567890\n", "1234567890123456b7890\n")
