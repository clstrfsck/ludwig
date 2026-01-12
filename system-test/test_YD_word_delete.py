from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < ,   ] YD

def test_no_leading_parameter():
    simple_edit_test("yd", "abc  def  ghi\n", "def  ghi\n")

def test_plus_leading_parameter():
    simple_edit_test("+yd", "abc  def  ghi\n", "def  ghi\n")

def test_minus_leading_parameter():
    # This seems kind of buggy.
    # I would have expected "ghi" to be deleted.
    simple_edit_test(">j-yd", "abc  def  ghi\n", "abc  ghi\n")

def test_positive_leading_parameter():
    simple_edit_test("2yd", "abc  def  ghi  jkl\n", "ghi  jkl\n")

def test_negative_leading_parameter():
    # This seems kind of buggy.
    # I would have expected "ghi" and "jkl" to be deleted.
    simple_edit_test(">j-2yd", "abc  def  ghi  jkl\n", "abc  jkl\n")

def test_eop_leading_parameter():
    # This seems kind of buggy.
    # I would have expected "def" and "ghi" to be deleted.
    simple_edit_test("a>yd", "abc\n def\n  ghi\n\njkl\n", "\njkl\n")

def test_bop_leading_parameter():
    # This is kind of buggy.
    # If the " xyz" is removed, then nothing is deleted :(
    simple_edit_test("2a>j<yd", "abc\n def\n  ghi xyz\n\njkl\n", "\nxyz\n\njkl\n")
