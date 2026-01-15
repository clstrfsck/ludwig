from systest import simple_edit_test, unmodified_test

# LEADING PARAMETER: [none, + , - , +n , -n , > , < ,   ] R

def test_no_leading_parameter():
    simple_edit_test("r/cat/tac/i/xyz/", "abcdefgcathijklmn\n", "abcdefgtacxyzhijklmn\n")

def test_no_leading_parameter_exact():
    simple_edit_test("r\"Cat\"Tac\"i/xyz/", "abcatdefgCathijklmn\n", "abcatdefgTacxyzhijklmn\n")

def test_plus_leading_parameter():
    simple_edit_test("+r/cat/tac/", "abcdefgcathijklmn\n", "abcdefgtachijklmn\n")

def test_minus_leading_parameter():
    simple_edit_test(">j-r/cat/tac/", "abcdefgcathijklmn\n", "abcdefgtachijklmn\n")

def test_zero_leading_parameter():
    unmodified_test("0r/cat/tac/", "abcdefgcathijklmn\n")

def test_positive_leading_parameter():
    simple_edit_test("3r/cat/tac/i/m1/", "abcdcatcatefgcathij\n", "abcdtactacefgtacm1hij\n")

def test_negative_leading_parameter():
    simple_edit_test(">j-3r/cat/tac/i/m1/", "catabcdcatcatefgcathij\n", "catabcdm1tactacefgtachij\n")

def test_bob_leading_parameter():
    simple_edit_test(">a<r/cat/tac/i/m1/", "abcatd\nbcat\ncat\n", "abm1tacd\nbtac\ntac\n")

def test_eob_leading_parameter():
    simple_edit_test(">r/cat/tac/i/m1/", "abcatd\nbcat\ncat\n", "abtacd\nbtac\ntacm1\n")
