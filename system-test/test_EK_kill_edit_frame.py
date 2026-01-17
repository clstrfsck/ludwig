from systest import multi_file_edit_test

# LEADING PARAMETER: [none,   ,   ,    ,    ,   ,   ,   ] EK

def test_no_leading_parameter():
    multi_file_edit_test(
        "ed/asd/erek/asd/si",
        { "zz": "line1\nline2\nline3\n" },
        { "zz": "line1\nline2\nline3\n" },
        [
            '^$', '^$', '^$',
            '^Spans$',
            '^=====$',
            '^          <none>$',
            '^$',
            '^Frames$',
            '^======$',
            '^COMMAND *$',
            '^$', '^$', '^$',
            '^Frames$',
            '^======$',
            '^HEAP *$',
            '^$', '^$', '^$',
            '^Frames$',
            '^======$',
            '^LUDWIG *$',
            '^  Output: .*/test_file$',
            '^$', '^$', '^$',
            '^Frames$',
            '^======$',
            '^OOPS *$',
        ]
    )
