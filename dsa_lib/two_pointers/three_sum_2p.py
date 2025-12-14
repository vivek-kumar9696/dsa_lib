from typing import List, Tuple


def three_sum_2p(nums: List[int], target: int) -> List[Tuple[int, int, int]]:
    nums.sort()
    res = set()
    if len(nums) == 0:
        return res
    for index, ele in enumerate(nums):
        diff = target - ele
        if index != len(nums) - 1:
            left = index + 1
        else:
            left = index
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < diff:
                left += 1
            elif nums[left] + nums[right] > diff:
                right -= 1
            elif nums[left] + nums[right] == diff:
                val = tuple(sorted((ele, nums[left], nums[right])))
                res.add(val)
                left += 1
                right -= 1
    print(res)
    return list(res)
