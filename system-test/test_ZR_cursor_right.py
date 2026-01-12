from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] ZR

def test_no_leading_parameter():
    simple_edit_test("zri/m1/", "abc\nb\n", "am1bc\nb\n")

def test_plus_leading_parameter():
    simple_edit_test("zri/m1/", "abc\nb\n", "am1bc\nb\n")

def test_positive_leading_parameter():
    simple_edit_test("2zri/m1/", "abc\nb\n", "abm1c\nb\n")

def test_positive_leading_parameter_split():
    simple_edit_test("ep/m=(1,10)/>zri/m1/", "abc\nb\n", "abc      m1\nb\n")
