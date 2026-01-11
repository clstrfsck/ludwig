from systest import simple_edit_test, syntax_error

# LEADING PARAMETER: [none, + , - , +n , -n ,   ,   ,   ] G

def test_no_leading_parameter():
    simple_edit_test("g/cat/i/m1/", "batCatdat\n", "batCatm1dat\n")

def test_no_leading_parameter_exact():
    simple_edit_test("g\"Cat\"i/m1/", "catcatCatdat\n", "catcatCatm1dat\n")

def test_plus_leading_parameter():
    simple_edit_test("g/cat/i/m1/", "batCatdat\n", "batCatm1dat\n")

def test_minus_leading_parameter():
    simple_edit_test(">j-g/cat/i/m1/", "batCatdat\n", "batm1Catdat\n")

def test_minus_leading_parameter_exact():
    simple_edit_test(">j-g\"Cat\"i/m1/", "catcatCatcat\n", "catcatm1Catcat\n")

def test_zero_leading_parameter():
    syntax_error("0g", "")

def test_positive_leading_parameter():
    simple_edit_test("3g/cat/i/m1/", "catcatcatcat\n", "catcatcatm1cat\n")

def test_negative_leading_parameter():
    simple_edit_test(">j-3g/cat/i/m1/", "catcatcatcat\n", "catm1catcatcat\n")
