from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < ,   ] AW

def test_no_leading_parameter():
    simple_edit_test("awti/m1/", "abc def ghi\n", "abc m1def ghi\n", ["-O"])

def test_plus_leading_parameter():
    simple_edit_test("+awti/m1/", "abc def ghi\n", "abc m1def ghi\n", ["-O"])

def test_minus_leading_parameter():
    simple_edit_test(">ac-awti/m1/", "abc def ghi\n", "abc m1def ghi\n", ["-O"])

def test_zero_leading_parameter():
    simple_edit_test(">ac0awti/m1/", "abc def ghi\n", "abc def m1ghi\n", ["-O"])

def test_positive_leading_parameter():
    simple_edit_test("2awti/m1/", "abc def ghi\n", "abc def m1ghi\n", ["-O"])

def test_negative_leading_parameter():
    simple_edit_test(">ac-2awti/m1/", "abc def ghi jkl\n", "abc m1def ghi jkl\n", ["-O"])

def test_bop_leading_parameter():
    simple_edit_test("2al>ac<awti/m1/", "abc def ghi\n\njkl mno pqr\n", "abc def ghi\n\nm1jkl mno pqr\n", ["-O"])

def test_eop_leading_parameter():
    simple_edit_test(">awti/m1/", "abc def ghi\n\njkl mno pqr\n", "abc def ghi m1\n\njkl mno pqr\n", ["-O"])
