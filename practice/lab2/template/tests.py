import os
import subprocess
from expand_template import *


def test_expand_template():
    row = 'Good %time%, %person%.'
    params = {'%time%': 'morning', '%person%': 'William Gibson'}
    expected = 'Good morning, William Gibson.'

    patterns = [key for key in params.keys()]
    aho_korasik_tree: AhoKorasikTree = AhoKorasikTree(patterns)

    result = expand_template(row, params, aho_korasik_tree)
    assert result == expected


def test_expand_template_some_patterns():
    row = '%time%, %time%, %time%'
    params = {'%time%': 'morning', 'empty': 'none'}
    expected = 'morning, morning, morning'

    patterns = [key for key in params.keys()]
    aho_korasik_tree: AhoKorasikTree = AhoKorasikTree(patterns)

    result = expand_template(row, params, aho_korasik_tree)
    assert result == expected


def test_expand_template_expand_longest_pattern():
    row = 'aaaaa'
    params = {'a': 'b', 'aa': 'cc', 'aaa': 'ddd', 'aaaa': 'eeee', 'aaaaa': 'fffff'}
    expected = 'fffff'

    patterns = [key for key in params.keys()]
    aho_korasik_tree: AhoKorasikTree = AhoKorasikTree(patterns)

    result = expand_template(row, params, aho_korasik_tree)
    assert result == expected


def test_expand_template_empty_params():
    row = 'acac'
    params = {'': 'ded'}
    expected = 'acac'

    patterns = [key for key in params.keys()]
    aho_korasik_tree: AhoKorasikTree = AhoKorasikTree(patterns)

    result = expand_template(row, params, aho_korasik_tree)
    assert result == expected


def test_expand_template_from_file():
    input_file: str = './data/test.txt'
    output_file: str ='./data/result.txt'

    params = ['python', 'expand_template.py', input_file, output_file,
              '-l', '%WEEK_DAY%', 'wednesday', '%USER_NAME%', 'dudes']
    expected = 'It is wednesday my dudes\n' * 6
    res = subprocess.run(params, stdout=subprocess.PIPE)
    result = ''
    with open(output_file, 'r', encoding='utf-8') as file:
        for row in file:
            result += row
    try:
        assert result == expected
    finally:
        os.remove(output_file)


def test_expand_most_possible_template():
    row = '-AABBCCCCCABC+'
    params = {
        'A': '[a]',
        'AA': '[aa]',
        'B': '[b]',
        'BB': '[bb]',
        'C': '[c]',
        'CC': '[cc]'
    }

    patterns = [key for key in params.keys()]
    aho_korasik_tree: AhoKorasikTree = AhoKorasikTree(patterns)

    assert (expand_template(row, params, aho_korasik_tree) == "-[aa][bb][cc][cc][c][a][b][c]+")

#Лучше назвать test_expanded_text_is_not_expand
def test_expanded_test_is_not_expand():
    row = "Hello, %USER_NAME%. Today is {WEEK_DAY}."
    params = {
        '%USER_NAME%': 'Super %USER_NAME% {WEEK_DAY}',
        '{WEEK_DAY}': 'Friday. {WEEK_DAY}'
    }

    patterns = [key for key in params.keys()]
    aho_korasik_tree: AhoKorasikTree = AhoKorasikTree(patterns)

    assert (expand_template(row, params, aho_korasik_tree) ==
            "Hello, Super %USER_NAME% {WEEK_DAY}. Today is Friday. {WEEK_DAY}.")
