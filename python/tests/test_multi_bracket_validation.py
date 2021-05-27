from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_curly_brackets(): ## 1
    assert multi_bracket_validation('{}')
    assert multi_bracket_validation('{}(){}')

def test_multi_brackets_compination_validation(): ## 2
    assert multi_bracket_validation('{}()[[]]')

def test_multi_bracket_validation(): ## 3
    assert multi_bracket_validation('(){}[]')

def test_parentheses_validation(): ## 4
    assert multi_bracket_validation('()')

def test_multi_square_curly_bracket_validation(): ## 5
    assert multi_bracket_validation('{[]}')

def test_defferent_closing_bracket_validation(): ## 6
    assert not multi_bracket_validation('(]')
    assert not multi_bracket_validation('[}')

def test_multi_open_parentheses_validation(): ## 7
    assert not multi_bracket_validation('((')

def test_enterfaring_bracket_validation_nine(): ## 8
    assert not multi_bracket_validation('([)]')

def test_multi_missing_parantheses_validation(): ## 9
    assert not multi_bracket_validation('[({}]')

def test_enterfaring_parantheses_validation(): ## 10
    assert not multi_bracket_validation('{(})')

def test_missing_bracket_validation(): ## 11
    assert not multi_bracket_validation('{')

def test_multi_bracket_with_text_validation(): ## 12
    assert not multi_bracket_validation('()[[Extra Characters]]')
    assert not multi_bracket_validation('{}{Code}[Fellows](())')

def test_missing_paranteses_opening_validation(): ## 13
    assert not multi_bracket_validation(')')


