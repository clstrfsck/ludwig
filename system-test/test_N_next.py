from systest import command_failed, simple_edit_test, unmodified_test

# LEADING PARAMETER: [none, + , - , +n , -n ,   ,   ,   ] N

def test_no_leading_parameter_single():
    simple_edit_test("n/b/i/m1/", "aaaaaabbbccc\n", "aaaaaam1bbbccc\n")

def test_no_leading_parameter_range():
    simple_edit_test("n/e..f/i/m1/", "abcdefghijkl\n", "abcdm1efghijkl\n")

def test_plus_leading_parameter():
    simple_edit_test("+n/e..f/i/m1/", "abcdefghijkl\n", "abcdm1efghijkl\n")

def test_minus_leading_parameter():
    simple_edit_test("7j-n/a/i/m1/", "akkkkkkbbbbbb\n", "am1kkkkkkbbbbbb\n")

def test_zero_leading_parameter():
    # Not sure if this is a bug or a feature,
    # 0N seems to behave like a noop.
    unmodified_test("0n/a/", "")

def test_positive_leading_parameter():
    simple_edit_test("3n/a/i/m1/", "abababab\n", "abababm1ab\n")

def test_positive_leading_parameter_too_big():
    command_failed("4n/a/i/m1/", "abababab\n")

def test_negative_leading_parameter():
    simple_edit_test(">j-3n/a/i/m1/", "abababab\n", "abam1babab\n")
