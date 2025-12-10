import pytest
from dsa_lib.arrays import two_sum


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
