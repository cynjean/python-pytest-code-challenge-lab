from palindrome import longest_palindromic_substring


def test_racecar():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_single_character():
    assert longest_palindromic_substring("a") == "a"


def test_two_characters():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]


def test_babad():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]

def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_no_repeating_characters():
    result = longest_palindromic_substring("abcd")
    assert len(result) == 1


def test_long_palindrome():
    assert longest_palindromic_substring("abccba") == "abccba"