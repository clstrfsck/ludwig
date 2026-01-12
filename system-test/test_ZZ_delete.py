from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] ZZ

def test_no_leading_parameter():
    simple_edit_test(">jzzi/m1/", "abc\nb\n", "abm1\nb\n")

def test_no_leading_parameter_overwrite():
    simple_edit_test("ep/k=o/2jzz", "abc\nb\n", "a c\nb\n")

def test_plus_leading_parameter():
    simple_edit_test(">j+zzi/m1/", "abc\nb\n", "abm1\nb\n")

def test_positive_leading_parameter():
    simple_edit_test(">j2zzi/m1/", "abc\nb\n", "am1\nb\n")

def test_bol_leading_parameter():
    simple_edit_test(">j>zzi/m1/", "abc\nb\n", "m1\nb\n")
