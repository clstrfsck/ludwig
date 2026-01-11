from systest import simple_edit_test

# Not really a swap.  More of a move.
# LEADING PARAMETER: [none, + , - , +n , -n , > , < , @ ] SW

def test_no_leading_parameter():
    simple_edit_test("sw", "a\nb\n", "b\na\n")

def test_plus_leading_parameter():
    simple_edit_test("sw", "a\nb\n", "b\na\n")

def test_minus_leading_parameter():
    simple_edit_test("a-sw", "a\nb\n", "b\na\n")

def test_zero_leading_parameter():
    # This might be buggy.  Probably should not modify the file.
    simple_edit_test("0sw", "a\nb\n", "a\nb\n")

def test_positive_leading_parameter():
    simple_edit_test("3sw", "a\nb\nc\nd\n", "b\nc\nd\na\n")

def test_negative_leading_parameter():
    simple_edit_test("3a-3sw", "a\nb\nc\nd\n", "d\na\nb\nc\n")

def test_equals_leading_parameter():
    simple_edit_test("3a=sw", "a\nb\nc\nd\n", "d\na\nb\nc\n")

def test_bol_leading_parameter():
    simple_edit_test(">a-a<sw", "a\nb\nc\nd\n", "d\na\nb\nc\n")

def test_eol_leading_parameter():
    simple_edit_test(">sw", "a\nb\nc\nd\n", "b\nc\nd\na\n")
