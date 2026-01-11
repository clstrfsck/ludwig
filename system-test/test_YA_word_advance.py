from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < ,   ] YA

def test_no_leading_parameter():
    simple_edit_test("yai/m1/", "abc def ghi\n", "abc m1def ghi\n")

def test_plus_leading_parameter():
    simple_edit_test("+yai/m1/", "abc def ghi\n", "abc m1def ghi\n")

def test_minus_leading_parameter():
    simple_edit_test(">j-yai/m1/", "abc def ghi\n", "abc m1def ghi\n")

def test_zero_leading_parameter():
    simple_edit_test(">j0yai/m1/", "abc def ghi\n", "abc def m1ghi\n")

def test_positive_leading_parameter():
    simple_edit_test("2yai/m1/", "abc def ghi\n", "abc def m1ghi\n")

def test_negative_leading_parameter():
    simple_edit_test(">j-2yai/m1/", "abc def ghi jkl\n", "abc m1def ghi jkl\n")

def test_bop_leading_parameter():
    simple_edit_test(">a<yai/m1/", "abc def ghi\n\njkl mno pqr\n", "abc def ghi\n\nm1jkl mno pqr\n")

def test_eop_leading_parameter():
    simple_edit_test(">yai/m1/", "abc def ghi\n\njkl mno pqr\n", "abc def ghi\n\nm1jkl mno pqr\n")
