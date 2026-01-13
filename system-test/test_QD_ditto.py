from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < ,   ] "

def test_no_leading_parameter():
    simple_edit_test("a\"i/m1/", "abcd\n\n", "abcd\nam1\n")

def test_plus_leading_parameter():
    simple_edit_test("a+\"i/m1/", "abcd\n\n", "abcd\nam1\n")

def test_minus_leading_parameter():
    simple_edit_test("ep/k=o/a>j-\"i/m1/", "abcd\nefgh\n", "abcd\nefgm1d\n")

def test_zero_leading_parameter():
    # Buggy: should not mark file as modified.
    simple_edit_test("a0\"", "a\n\n", "a\n\n")

def test_positive_leading_parameter():
    simple_edit_test("a3\"i/m1/", "abcd\n\n", "abcd\nabcm1\n")

def test_negative_leading_parameter():
    simple_edit_test("ep/k=o/a>j-3\"i/m1/", "abcd\nwxyz\n", "abcd\nwm1bcd\n")

def test_bol_leading_parameter():
    simple_edit_test("a>\"i/m1/", "abcdef\n\n", "abcdef\nabcdefm1\n")

def test_eol_leading_parameter():
    simple_edit_test("ep/k=o/a>j<\"i/m1/", "abcdef\ntuvwxy\n", "abcdef\nm1abcdef\n")
