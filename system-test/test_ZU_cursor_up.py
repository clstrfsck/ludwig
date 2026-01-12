from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] ZU

def test_no_leading_parameter():
    simple_edit_test(">azui/m1/", "a\nb\nc\n", "a\nb\nm1c\n")

def test_plus_leading_parameter():
    simple_edit_test(">azui/m1/", "a\nb\nc\n", "a\nb\nm1c\n")

def test_positive_leading_parameter():
    simple_edit_test(">a2zui/m1/", "a\nb\nc\n", "a\nm1b\nc\n")

def test_positive_leading_parameter_split():
    simple_edit_test(">a>zui/m1/", "a\nb\nc\n", "m1a\nb\nc\n")
