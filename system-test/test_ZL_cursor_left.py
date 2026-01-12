from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] ZL

def test_no_leading_parameter():
    simple_edit_test(">jzli/m1/", "abc\nb\n", "abm1c\nb\n")

def test_plus_leading_parameter():
    simple_edit_test(">jzli/m1/", "abc\nb\n", "abm1c\nb\n")

def test_positive_leading_parameter():
    simple_edit_test(">j2zli/m1/", "abc\nb\n", "am1bc\nb\n")

def test_positive_leading_parameter_split():
    simple_edit_test(">j>zli/m1/", "abc\nb\n", "m1abc\nb\n")
