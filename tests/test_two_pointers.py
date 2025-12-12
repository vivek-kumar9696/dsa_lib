import pytest
from dsa_lib.two_pointers import check_palindrome


@pytest.mark.parametrize(
    "text, expected",
    [
        # Case 1: Standard simple palindrome
        ("racecar", True),
        ("madam", True),
        # Case 2: Not a palindrome
        ("hello", False),
        ("world", False),
        # Case 3: Mixed case (Should be case-insensitive)
        ("RaceCar", True),
        ("MaDaM", True),
        # Case 4: Sentences with spaces (Should ignore spaces)
        ("never odd or other", False),
        ("was it a car or a cat I saw", True),
        # Case 5: Special characters/Punctuation (Should be ignored)
        ("A man, a plan, a canal: Panama", True),
        ("Madam, I'm Adam.", True),
        # Case 6: Numbers
        ("12321", True),
        ("123456", False),
        # Case 7: Edge Cases
        ("", True),  # Empty string is a palindrome
        ("a", True),  # Single char is a palindrome
        ("!!", True),  # Only punctuation becomes empty string -> True
    ],
)
def test_check_palindrome_logic(text, expected):
    """
    Verifies the palindrome logic including string cleaning (removing non-alnum)
    and case insensitivity.
    """
    assert check_palindrome(text) == expected
