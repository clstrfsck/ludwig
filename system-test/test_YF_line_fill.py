from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] YF

def test_no_leading_parameter():
    simple_edit_test("ep/m=(1,11)/yf", "abc def\nghi  jkl\n", "abc def ghi\njkl\n")

def test_plus_leading_parameter():
    simple_edit_test("ep/m=(1,14)/+yf", "abc  def\n  ghi\n", "abc  def ghi\n")

def test_positive_leading_parameter():
    words = "abc def ghi jkl\n" * 4
    filled = "abc def ghi jkl abc def ghi\njkl abc def ghi jkl abc def\nghi jkl\n"
    simple_edit_test("ep/m=(1,30)/3yf", words, filled)

def test_eop_leading_parameter():
    line = "abc def ghi jkl\n"
    words = (line * 4) + "\n" + (line * 4)
    filled = "abc def ghi jkl abc def ghi\njkl abc def ghi jkl abc def\nghi jkl\n\n" + (line * 4)
    simple_edit_test("ep/m=(1,30)/>yf", words, filled)
