from systest import simple_edit_test, syntax_error, unmodified_test

# LEADING PARAMETER: [none, + , - , +n , -n ,   ,   ,   ] L

def test_no_leading_parameter():
    simple_edit_test("a2jli/m1/", "abcd\nbcde\n", "abcd\n  m1\nbcde\n")

def test_plus_leading_parameter():
    simple_edit_test("ali/m1/", "a\nb\n", "a\nm1\nb\n")

def test_minus_leading_parameter():
    simple_edit_test("a2j-li/m1/", "abcd\nbcde\n", "abcd\n\nbcm1de\n")

def test_zero_leading_parameter():
    unmodified_test("0l", "a\nb\n")

def test_positive_leading_parameter():
    simple_edit_test("2li/xyz/", "a\nb\n", "xyz\n\na\nb\n")

def test_negative_leading_parameter():
    simple_edit_test("-2li/xyz/", "a\nb\n", "\n\nxyza\nb\n")

def test_equals_leading_parameter():
    syntax_error("=l", "")
