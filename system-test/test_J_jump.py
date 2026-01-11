from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < , @ ] J

def test_no_leading_parameter():
    simple_edit_test("ji/m1/", "a\n", "am1\n")

def test_plus_leading_parameter():
    simple_edit_test("+ji/m1/", "a\n", "am1\n")

def test_minus_leading_parameter():
    simple_edit_test("i/m1/-ji/m2/", "a\n", "mm21a\n")

def test_zero_leading_parameter():
    simple_edit_test("0ji/m1/", "a\n", "m1a\n")

def test_positive_leading_parameter():
    simple_edit_test("3ji/m1/", "abcd\n", "abcm1d\n")

def test_negative_leading_parameter():
    simple_edit_test("i/xyz/-2ji/tuv/", "a\n", "xtuvyza\n")

def test_equals_leading_parameter():
    simple_edit_test("i/xyz/=ji/m1/", "a\n", "m1xyza\n")

def test_bol_leading_parameter():
    simple_edit_test("i/xyz/<ji/m1/", "abcd\n", "m1xyzabcd\n")

def test_eol_leading_parameter():
    simple_edit_test("i/xyz/>ji/m1/", "abcd\n", "xyzabcdm1\n")
