from systest import simple_edit_test
import pytest

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] ZH

@pytest.mark.skip(reason="ZH home command not available in batch mode")
def test_no_leading_parameter():
    # No window / no home in batch mode.
    simple_edit_test(">ai/m1/zhi/m2/", "a\nb\nc\n", "m2a\nb\nc\nm1\n")
