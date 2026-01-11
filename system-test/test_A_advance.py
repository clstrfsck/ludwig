from systest import command_failed, simple_edit_test

#  LEADING PARAMETER: [none, + , - , +n , -n , > , < , @ ] J

def test_no_leading_parameter():
    # Should insert the text after advancing to the next line
    simple_edit_test("ai/m1/", "a\nb\n", "a\nm1b\n")

def test_plus_leading_parameter():
    simple_edit_test("+ai/m1/", "a\nb\n", "a\nm1b\n")

def test_minus_leading_parameter():
    simple_edit_test("ai/m1/-ai/m2/", "a\nb\n", "m2a\nm1b\n")

def test_zero_leading_parameter():
    simple_edit_test("ji/m1/0ai/m2/", "a\nb\n", "m2am1\nb\n")

def test_positive_leading_parameter():
    simple_edit_test("3ai/m1/", "a\nb\nc\nd\ne\nf\n", "a\nb\nc\nm1d\ne\nf\n")

def test_negative_leading_parameter():
    simple_edit_test("3ai/m1/-2ai/m2/", "a\nb\nc\nd\ne\nf\n", "a\nm2b\nc\nm1d\ne\nf\n")

def test_equals_leading_parameter():
    simple_edit_test("3a=ai/m1/", "a\nb\nc\nd\ne\nf\n", "m1a\nb\nc\nd\ne\nf\n")

def test_eof_leading_parameter():
    simple_edit_test(">ai/m1/", "a\nb\nc\nd\ne\nf\n", "a\nb\nc\nd\ne\nf\nm1\n")

def test_bof_leading_parameter():
    simple_edit_test(">ai/m1/<ai/m2/", "a\nb\nc\nd\ne\nf\n", "m2a\nb\nc\nd\ne\nf\nm1\n")

def test_command_failed():
    command_failed("a", "")
