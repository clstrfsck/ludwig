from systest import simple_edit_test, unmodified_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] YC

def test_no_leading_parameter():
    simple_edit_test("ep/m=(1,10)/yc", "abc\n def\n  ghi\n", "   abc\n def\n  ghi\n")

def test_plus_leading_parameter():
    simple_edit_test("ep/m=(1,10)/yc", "abc\n def\n  ghi\n", "   abc\n def\n  ghi\n")

def test_zero_leading_parameter():
    unmodified_test("0yc", "")

def test_positive_leading_parameter():
    simple_edit_test("ep/m=(1,10)/2yc", "abc\n def\n  ghi\n", "   abc\n   def\n  ghi\n")

def test_eop_leading_parameter():
    simple_edit_test("ep/m=(1,10)/>yc", "abc\n def\n  ghi\n\njkl\n", "   abc\n   def\n   ghi\n\njkl\n")
