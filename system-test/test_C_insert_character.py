from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + , - , +n , -n ,   ,   ,   ] C

def test_no_leading_parameter():
    # Should insert the text after advancing to the next line
    simple_edit_test("ci/m1/", "a\nb\n", "m1 a\nb\n")

def test_plus_leading_parameter():
    simple_edit_test("+ci/m1/", "a\nb\n", "m1 a\nb\n")

def test_minus_leading_parameter():
    simple_edit_test("-ci/m1/", "a\nb\n", " m1a\nb\n")

def test_zero_leading_parameter():
    simple_edit_test("0c", "a\nb\n", "a\nb\n")

def test_positive_leading_parameter():
    simple_edit_test("3ci/m1/", "a\nb\nc\nd\ne\nf\n", "m1   a\nb\nc\nd\ne\nf\n")

def test_negative_leading_parameter():
    simple_edit_test("-3ci/m1/", "a\nb\nc\nd\ne\nf\n", "   m1a\nb\nc\nd\ne\nf\n")

def test_equals_leading_parameter():
    syntax_error("=ci/m1/", "a\nb\nc\nd\ne\nf\n")
