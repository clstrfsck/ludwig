from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    ,   ,   ,   ] PL

def test_no_leading_parameter():
    simple_edit_test(">alplti/m1/", "a\nb\nc\n", "m1a\nb\nc\n", ["-O"])

def test_plus_leading_parameter():
    simple_edit_test(">al+plti/m1/", "a\nb\nc\n", "m1a\nb\nc\n", ["-O"])

def test_positive_leading_parameter():
    simple_edit_test("ac2plti/m1/", "a\nb\nc\n", "a\nm1b\nc\n", ["-O"])
