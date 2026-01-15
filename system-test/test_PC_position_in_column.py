from systest import simple_edit_test

# LEADING PARAMETER: [none, + ,   , +n ,    ,   ,   ,   ] PC

def test_no_leading_parameter():
    simple_edit_test(">acti/m1/pcti/m2/", "abcdefghij\n", "m2abcdefghijm1\n", ["-O"])

def test_plus_leading_parameter():
    simple_edit_test(">acti/m1/+pcti/m2/", "abcdefghij\n", "m2abcdefghijm1\n", ["-O"])

def test_positive_leading_parameter():
    simple_edit_test("ti/m1/5pcti/m2/", "abcdefghij\n", "m1abm2cdefghij\n", ["-O"])
