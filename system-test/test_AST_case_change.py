from systest import simple_edit_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < ,   ] '

def test_no_leading_parameter_u():
    simple_edit_test("*ui/m1/", "abcd\n", "Am1bcd\n")

def test_no_leading_parameter_l():
    simple_edit_test("*li/m1/", "ABCD\n", "am1BCD\n")

def test_no_leading_parameter_e():
    simple_edit_test("*ei/m1/", "abcd\n", "Am1bcd\n")

def test_no_leading_parameter_ee():
    simple_edit_test("*e*ei/m1/", "abcd\n", "Abm1cd\n")

def test_plus_leading_parameter_u():
    simple_edit_test("+*ui/m1/", "abcd\n", "Am1bcd\n")

def test_plus_leading_parameter_l():
    simple_edit_test("+*li/m1/", "ABCD\n", "am1BCD\n")

def test_plus_leading_parameter_e():
    simple_edit_test("+*ei/m1/", "abcd\n", "Am1bcd\n")

def test_plus_leading_parameter_ee():
    simple_edit_test("+*e+*ei/m1/", "abcd\n", "Abm1cd\n")

def test_minus_leading_parameter_u():
    simple_edit_test(">j-*ui/m1/", "abcd\n", "abcm1D\n")

def test_minus_leading_parameter_l():
    simple_edit_test(">j-*li/m1/", "ABCD\n", "ABCm1d\n")

def test_minus_leading_parameter_e():
    simple_edit_test(">j-*ei/m1/", "abcd\n", "abcm1d\n")

def test_minus_leading_parameter_eeee():
    simple_edit_test(">j-*e-*e-*e-*ei/m1/", "abcd\n", "m1Abcd\n")

def test_zero_leading_parameter():
    # Buggy: should not mark file as modified.
    simple_edit_test("0*u", "a\n", "a\n")

def test_positive_leading_parameter_u():
    simple_edit_test("3*ui/m1/", "abcd\n", "ABCm1d\n")

def test_positive_leading_parameter_l():
    simple_edit_test("3*li/m1/", "ABCD\n", "abcm1D\n")

def test_positive_leading_parameter_e():
    simple_edit_test("3*ei/m1/", "abcd\n", "Abcm1d\n")

def test_negative_leading_parameter_u():
    simple_edit_test(">j-3*ui/m1/", "abcd\n", "am1BCD\n")

def test_negative_leading_parameter_l():
    simple_edit_test(">j-3*li/m1/", "ABCD\n", "Am1bcd\n")

def test_negative_leading_parameter_e():
    simple_edit_test(">j-3*ei/m1/", "aBCD\n", "am1bcd\n")

def test_bol_leading_parameter_u():
    simple_edit_test(">*ui/m1/", "abcdef\n", "ABCDEFm1\n")

def test_bol_leading_parameter_l():
    simple_edit_test(">*li/m1/", "ABCDEF\n", "abcdefm1\n")

def test_bol_leading_parameter_e():
    simple_edit_test(">*ei/m1/", "aBCDEF\n", "Abcdefm1\n")

def test_eol_leading_parameter_u():
    simple_edit_test(">j<*ui/m1/", "abcdef\n", "m1ABCDEF\n")

def test_eol_leading_parameter_l():
    simple_edit_test(">j<*li/m1/", "ABCDEF\n", "m1abcdef\n")

def test_eol_leading_parameter_e():
    simple_edit_test(">j<*ei/m1/", "aBCDEF\n", "m1Abcdef\n")
