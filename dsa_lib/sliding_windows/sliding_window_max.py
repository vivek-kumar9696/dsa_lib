from typing import List


def sliding_window_max_bf(arr: List[int], k: int) -> List[int]:
    res = []
    if len(arr) == 0:
        return res

    for i in range(len(arr) - k + 1):
        max = -float("inf")
        for j in range(k):
            if arr[i + j] > max:
                max = arr[i + j]
        res.append(max)

    return res
