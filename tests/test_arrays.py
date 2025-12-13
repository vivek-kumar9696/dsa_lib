import pytest
from dsa_lib.arrays import two_sum, three_sum
from typing import List, Tuple

# ---------------------------------- Start Two Sum----------------------------------------


# The "Table" of test cases
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),  # Basic case
        ([3, 2, 4], 6, [1, 2]),  # Elements not at start
        ([3, 3], 6, [0, 1]),  # Duplicate numbers
        ([1, 2, 3], 100, None),  # No solution
        ([], 5, None),  # Empty list
    ],
)
def test_two_sum(nums, target, expected):
    """
    Run two_sum against multiple scenarios automatically.
    """
    result = two_sum(nums, target)

    # If we expect a list, sort it to ensure order doesn't matter
    if isinstance(expected, list) and isinstance(result, list):
        assert sorted(result) == sorted(expected)
    else:
        assert result == expected


# --------------------------------- End Two Sum-------------------------------------------


# ----------------------------------Start 3 Sum Hashset----------------------------------
def normalize_triplets(
    triplets: List[Tuple[int, int, int]],
) -> List[Tuple[int, int, int]]:
    """
    Helper function to sort each triplet internally and then sort the list of triplets.
    This ensures that (-1, 0, 1) is treated the same as (-1, 1, 0).
    """
    return sorted([tuple(sorted(t)) for t in triplets])


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Case 1: Standard LeetCode example (Target 0)
        ([-1, 0, 1, 2, -1, -4], 0, [(-1, -1, 2), (-1, 0, 1)]),
        # Case 2: Positive Target
        ([1, 2, 3, 4, 5], 9, [(1, 3, 5), (2, 3, 4)]),
        # Case 3: Duplicates in input, unique triplets required
        ([0, 0, 0, 0], 0, [(0, 0, 0)]),
        # Case 4: No solution
        ([1, 2, 3], 10, []),
        # Case 5: Empty or small input
        ([], 0, []),
        ([1, 2], 3, []),
    ],
)
def test_three_sum_logic(nums, target, expected):
    """
    Verifies that the function identifies the correct unique triplets.
    """
    result = three_sum(nums, target)
    assert normalize_triplets(result) == normalize_triplets(expected)


def test_negative_target_logic_bug():
    """
    CRITICAL TEST: This exposes the bug in the line `if ele > target: break`.

    Scenario: nums=[-5, -1, 0], target=-6.
    'ele' starts at -5.
    -5 > -6 is True.
    Your code breaks and returns [], but the answer is [(-5, -1, 0)].
    """
    nums = [-5, -1, 0]
    target = -6
    expected = [(-5, -1, 0)]

    result = three_sum(nums, target)

    # If your code is fixed, this passes. Currently, it will fail.
    assert normalize_triplets(result) == normalize_triplets(expected)


def test_large_numbers():
    """
    Test with larger integers to ensure no overflow logic issues (Python handles large ints natively).
    """
    nums = [100, 200, 300, 600]
    target = 600
    expected = [(100, 200, 300)]
    assert normalize_triplets(three_sum(nums, target)) == normalize_triplets(expected)


# -------------------------------------- End 3 Sum Hashset -----------------------------------------------
