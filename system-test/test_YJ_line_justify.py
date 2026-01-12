from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] YJ

def test_no_leading_parameter():
    simple_edit_test("ep/m=(1,11)/yj", "abc def\nghi  jkl\n", "abc     def\nghi  jkl\n")

def test_plus_leading_parameter():
    simple_edit_test("ep/m=(1,11)/+yj", "abc def\nghi  jkl\n", "abc     def\nghi  jkl\n")

def test_positive_leading_parameter():
    words = "abc def ghi jkl mno pqr\n" * 4
    filled = ("abc  def   ghi  jkl   mno  pqr\n" * 2) + ("abc def ghi jkl mno pqr\n" * 2)
    simple_edit_test("ep/m=(1,30)/2yj", words, filled)

def test_eop_leading_parameter():
    line = "abc def ghi jkl mno pqr\n"
    fline = "abc  def   ghi  jkl   mno  pqr\n"
    words = (line * 4) + "\n" + (line * 2)
    filled = (fline * 3) + line + "\n" + (line * 2)
    simple_edit_test("ep/m=(1,30)/>yj", words, filled)
