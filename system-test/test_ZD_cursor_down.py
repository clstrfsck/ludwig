from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] ZD

def test_no_leading_parameter():
    simple_edit_test("zdi/m1/", "a\nb\n", "a\nm1b\n")

def test_plus_leading_parameter():
    simple_edit_test("+zdi/m1/", "a\nb\n", "a\nm1b\n")

def test_positive_leading_parameter():
    simple_edit_test("2zdi/m1/", "a\nb\nc\n", "a\nb\nm1c\n")

def test_positive_leading_parameter_split():
    simple_edit_test(">zdi/m1/", "a\nb\nc\n", "a\nb\nc\nm1\n")
