from systest import multi_file_edit_test

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] FT

def test_no_leading_parameter():
    multi_file_edit_test(
        "ft",
        { "zz": "line1\nline2\nline3\n" },
        { "zz": "line1\nline2\nline3\n" },
        [
            '^$',  '^$',
            '^Usage   Mod Frame  Filename$',
            '^------- --- ------ --------$',
            '^$',
            '^FO          LUDWIG .*/test_file$'
        ]
    )
