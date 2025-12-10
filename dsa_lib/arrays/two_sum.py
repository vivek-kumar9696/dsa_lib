from typing import List, Optional


def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Finds indices of two numbers in an array that add up to a specific target.

    This implementation uses a hash map to achieve O(n) time complexity.

    Args:
        nums: A list of integers.
        target: The target integer sum.

    Returns:
        A list containing the two indices [index1, index2] if found,
        otherwise None.

    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    seen = {}  # Map value -> index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

    return None
