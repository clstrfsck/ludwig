from systest import simple_edit_test, unmodified_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < , @ ] K

def test_no_leading_parameter():
    simple_edit_test("ki/m1/", "a\n", "m1\n")

def test_plus_leading_parameter():
    simple_edit_test("+ki/m1/", "a\n", "m1\n")

def test_minus_leading_parameter():
    simple_edit_test("ak", "a\nb\n", "a\n")

def test_zero_leading_parameter():
    unmodified_test("a0k", "a\nb\n")

def test_positive_leading_parameter():
    simple_edit_test("2j2ki/xyz/", "abcd\nbcde\ncdef\ndefg\n", "cdxyzef\ndefg\n")

def test_negative_leading_parameter():
    simple_edit_test("2a2j-2ki/xyz/", "abcd\nbcde\ncdef\ndefg\n", "cdxyzef\ndefg\n")

def test_equals_leading_parameter():
    simple_edit_test("2a=ki/xyz/", "abcd\nbcde\ncdef\ndefg\n", "xyzcdef\ndefg\n")

def test_bol_leading_parameter():
    simple_edit_test("2a>ki/xyz/", "abcd\nbcde\ncdef\ndefg\n", "abcd\nbcde\nxyz\n")

def test_eol_leading_parameter():
    simple_edit_test("2a<ki/xyz/", "abcd\nbcde\ncdef\ndefg\n", "xyzcdef\ndefg\n")
