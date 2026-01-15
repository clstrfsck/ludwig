from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < ,   ] DW

def test_no_leading_parameter():
    simple_edit_test("dw", "abc  def  ghi\n", "def  ghi\n", ["-O"])

def test_plus_leading_parameter():
    simple_edit_test("+dw", "abc  def  ghi\n", "def  ghi\n", ["-O"])

def test_minus_leading_parameter():
    # This seems kind of buggy.
    # I would have expected "ghi" to be deleted.
    simple_edit_test(">ac-dw", "abc  def  ghi\n", "abc  ghi\n", ["-O"])

def test_positive_leading_parameter():
    simple_edit_test("2dw", "abc  def  ghi  jkl\n", "ghi  jkl\n", ["-O"])

def test_negative_leading_parameter():
    # This seems kind of buggy.
    # I would have expected "ghi" and "jkl" to be deleted.
    simple_edit_test(">ac-2dw", "abc  def  ghi  jkl\n", "abc  jkl\n", ["-O"])

def test_eop_leading_parameter():
    simple_edit_test("al>dw", "abc\n def\n  ghi\n\njkl\n", "\n\n\njkl\n", ["-O"])

def test_bop_leading_parameter():
    # This is kind of buggy.
    # If the " xyz" is removed, then ghi is not deleted :(
    simple_edit_test("2al>ac<dw", "abc\n def\n  ghi xyz\n\njkl\n", "\nxyz\n\njkl\n", ["-O"])
