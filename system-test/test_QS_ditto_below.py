from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < ,   ] '

def test_no_leading_parameter():
    simple_edit_test("'i/m1/", "\nabcd\n", "am1\nabcd\n")

def test_plus_leading_parameter():
    simple_edit_test("+'i/m1/", "\nabcd\n", "am1\nabcd\n")

def test_minus_leading_parameter():
    simple_edit_test("ep/k=o/>j-'i/m1/", "abcd\nefgh\n", "abcm1h\nefgh\n")

def test_zero_leading_parameter():
    # Buggy: should not mark file as modified.
    simple_edit_test("0'", "\na\n", "\na\n")

def test_positive_leading_parameter():
    simple_edit_test("3'i/m1/", "\nabcd\n", "abcm1\nabcd\n")

def test_negative_leading_parameter():
    simple_edit_test("ep/k=o/>j-3'i/m1/", "abcd\nwxyz\n", "am1xyz\nwxyz\n")

def test_bol_leading_parameter():
    simple_edit_test(">'i/m1/", "\nabcdef\n", "abcdefm1\nabcdef\n")

def test_eol_leading_parameter():
    simple_edit_test("ep/k=o/>j<'i/m1/", "abcdef\ntuvwxy\n", "m1tuvwxy\ntuvwxy\n")
