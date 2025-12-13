from typing import List


def two_sum_2p(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0:
        return []
    nums.sort()
    left = 0
    right = len(nums) - 1
    sum = nums[left] + nums[right]

    while sum != target and left < right:
        if sum > target:
            right -= 1
            sum = nums[left] + nums[right]

        elif sum < target:
            left += 1
            sum = nums[left] + nums[right]

    if left < right:
        return [nums[left], nums[right]]
    else:
        return []
