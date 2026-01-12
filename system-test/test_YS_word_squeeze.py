from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    , > ,   ,   ] YS

def test_no_leading_parameter():
    simple_edit_test("ep/m=(1,11)/ys", " abc    def\nghi  jkl\n", " abc def\nghi  jkl\n")

def test_plus_leading_parameter():
    simple_edit_test("ep/m=(2,12)/+ysi/m1/", "  abc     def\nghi  jkl\n", "  abc def\ngm1hi  jkl\n")

def test_positive_leading_parameter():
    words = "  abc   def   ghi    jkl     mno    pqr\n"
    spaced = words * 4
    squeezed = ("  abc def ghi jkl mno pqr\n" * 2) + (words * 2)
    simple_edit_test("ep/m=(2,40)/2ys", spaced, squeezed)

def test_eop_leading_parameter():
    line = "    abc   def   ghi   jkl   mno   pqr\n"
    sline = "    abc def ghi jkl mno pqr\n"
    words = (line * 4) + "\n" + (line * 2)
    aligned = (sline * 4) + "\n" + (line * 2)
    simple_edit_test("ep/m=(3,43)/>ys", words, aligned)
