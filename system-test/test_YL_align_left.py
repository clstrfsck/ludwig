from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] YL

def test_no_leading_parameter():
    simple_edit_test("ep/m=(1,11)/yl", " abc def\nghi  jkl\n", "abc def\nghi  jkl\n")

def test_plus_leading_parameter():
    simple_edit_test("ep/m=(2,12)/+yli/m1/", "     abc def\nghi  jkl\n", " abc def\ngm1hi  jkl\n")

def test_positive_leading_parameter():
    words = "  abc def ghi jkl mno pqr\n"
    unaligned = words * 4
    aligned = (" abc def ghi jkl mno pqr\n" * 2) + (words * 2)
    simple_edit_test("ep/m=(2,31)/2yl", unaligned, aligned)

def test_eop_leading_parameter():
    line = "    abc def ghi jkl mno pqr\n"
    aline = "  abc def ghi jkl mno pqr\n"
    words = (line * 4) + "\n" + (line * 2)
    aligned = (aline * 4) + "\n" + (line * 2)
    simple_edit_test("ep/m=(3,33)/>yl", words, aligned)
