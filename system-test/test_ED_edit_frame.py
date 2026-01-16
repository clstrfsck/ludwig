from systest import multi_file_edit_test

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] ED

def test_no_leading_parameter():
    multi_file_edit_test(
        "ed/asd/fo/asd/i/asd/",
        { "zz": "line1\nline2\nline3\n" },
        { "zz": "line1\nline2\nline3\n", "asd": "asd\n" },
        ["/asd created \\(1 line written\\)\\.$"]
    )
