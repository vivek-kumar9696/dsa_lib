import pytest
from dsa_lib.two_pointers import check_palindrome, two_sum_2p, three_sum_2p


# ------------------------------------------Start Palindrome Tests---------------------------------------
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


# --------------------------------------End Palindrome Tests--------------------------------------

# ---------------------------------- Start Two Sum----------------------------------------


# The "Table" of test cases
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [2, 7]),  # Basic case
        ([3, 2, 4], 6, [2, 4]),  # Elements not at start
        ([3, 3], 6, [3, 3]),  # Duplicate numbers
        ([1, 2, 3], 100, []),  # No solution
        ([], 5, []),  # Empty list
    ],
)
def test_two_sum(nums, target, expected):
    """
    Run two_sum against multiple scenarios automatically.
    """
    result = two_sum_2p(nums, target)

    # If we expect a list, sort it to ensure order doesn't matter
    if isinstance(expected, list) and isinstance(result, list):
        assert sorted(result) == sorted(expected)
    else:
        assert result == expected


# --------------------------------- End Two Sum-------------------------------------------

# ----------------------------------Start Three Sum ----------------------------------------


def normalize_results(results):
    """
    Helper to sort results so order doesn't matter (e.g. [A, B] vs [B, A])
    and sort within triplets (-1, 0, 1) is same as (0, -1, 1).
    """
    return sorted([tuple(sorted(t)) for t in results])


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Case 1: Standard Success
        ([-1, 0, 1, 2, -1, -4], 0, [(-1, -1, 2), (-1, 0, 1)]),
        # Case 2: No solution
        ([1, 2, 3], 10, []),
        # Case 3: Empty input
        ([], 0, []),
    ],
)
def test_three_sum_basic(nums, target, expected):
    """
    Tests basic functionality.
    """
    result = three_sum_2p(nums, target)
    assert normalize_results(result) == normalize_results(expected)


def test_collision_bug():
    """
    CRITICAL TEST: Detects if the code uses the same element twice.
    Input: [1, 4], Target: 9
    Logic:
      - ele = 1, diff = 8.
      - left = 1 (val 4), right = 1 (val 4).
      - Loop doesn't run (left is not < right).
      - Check: nums[1] + nums[1] (4+4) == 8.
      - Your code likely returns [(1, 4, 4)], which is WRONG (index 1 used twice).
    """
    nums = [1, 4]
    target = 9
    expected = []  # Impossible to get 9 from unique indices

    result = three_sum_2p(nums, target)

    # This assertion will likely FAIL with your current code
    assert normalize_results(result) == expected


def test_missing_multiple_pairs():
    """
    Logic Check: Can it find multiple pairs for the SAME first element?
    Input: [-2, 0, 1, 1, 2], Target: 0
    Pairs for -2: (-2, 0, 2) AND (-2, 1, 1)

    Your code stops the 'while' loop immediately after finding the first match,
    so it will miss the second triplet.
    """
    nums = [-2, 0, 1, 1, 2]
    target = 0
    # Both are valid
    expected = [(-2, 0, 2), (-2, 1, 1)]

    result = three_sum_2p(nums, target)

    # This assertion will likely FAIL (you might only get one of them)
    assert normalize_results(result) == normalize_results(expected)


# --------------------------------------- End Three Sum------------------------------
