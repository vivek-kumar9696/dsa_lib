from typing import List, Tuple


def three_sum(nums: List[int], target: int) -> List[Tuple[int, int, int]]:
    nums.sort()
    res = set()

    for index, ele in enumerate(nums):
        seen = set()
        diff = target - ele
        for j in nums[index + 1 :]:
            diff2 = diff - j
            if diff2 in seen:
                res.add((ele, j, diff2))
            seen.add(j)
    return list(res)
