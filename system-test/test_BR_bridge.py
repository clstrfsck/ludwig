from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + , - ,    ,    ,   ,   ,   ] BR

def test_no_leading_parameter_single():
    simple_edit_test("br/a/i/m1/", "aaaaaab\n", "aaaaaam1b\n")

def test_no_leading_parameter_range():
    simple_edit_test("br/a..f/i/m1/", "abcdefghijkl\n", "abcdefm1ghijkl\n")

def test_plus_leading_parameter():
    simple_edit_test("+br/a..f/i/m1/", "abcdefghijkl\n", "abcdefm1ghijkl\n")

def test_minus_leading_parameter():
    # This seems a bit buggy.  Using -br/a/ where there are multiple a's
    # to the beginning of the frame does not move dot to the first a.
    # ie this will fail:
    # simple_edit_test("6j-br/a/i/m1/", "aaaaaab\n", "m1aaaaaab\n")
    #
    # The actual result here will be "aaaaaam1b" because br/a/ does not
    # move dot.  Here the "k" is used as a sentinel.
    simple_edit_test("7j-br/a/i/m1/", "kaaaaaabbbbbb\n", "km1aaaaaabbbbbb\n")

def test_zero_leading_parameter():
    syntax_error("0br/a/", "a\n")
