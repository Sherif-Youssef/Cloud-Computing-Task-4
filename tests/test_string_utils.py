from src.string_utils import StringUtils


def test_reverse():
    assert StringUtils.reverse("hello") == "olleh"


def test_reverse_empty():
    assert StringUtils.reverse("") == ""


def test_is_palindrome_true():
    assert StringUtils.is_palindrome("racecar") is True


def test_is_palindrome_with_spaces_and_case():
    assert StringUtils.is_palindrome("Never Odd Or Even") is True


def test_is_palindrome_false():
    assert StringUtils.is_palindrome("python") is False


def test_count_vowels():
    assert StringUtils.count_vowels("hello world") == 3


def test_count_vowels_empty():
    assert StringUtils.count_vowels("") == 0


def test_to_title_case():
    assert StringUtils.to_title_case("hello world") == "Hello World"
