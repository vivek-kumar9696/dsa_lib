import pytest
from dsa_lib.sliding_windows import (
    buy_sell_stocks,
    sliding_window_max_bf,
)  # Import the function


# The "Table" of test cases
@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),  # Simple case: Buy at 1 and sell at 6
        ([7, 6, 4, 3, 1], 0),  # No profit: Prices are decreasing
        ([1, 2, 3, 4, 5], 4),  # Simple case: Buy at 1 and sell at 5
        (
            [10, 20, 30, 40, 50],
            40,
        ),  # Increasing prices: Max profit is 40 (buy at 10, sell at 50)
        ([5, 2, 8, 3, 10, 1], 8),  # Profit from buying at 2 and selling at 10
        ([10], 0),  # Edge case: Only one price, no profit
        ([], 0),  # Edge case: Empty list
    ],
)
def test_buy_sell_stocks(prices, expected):
    """
    Run buy_sell_stocks against multiple scenarios automatically.
    """
    result = buy_sell_stocks(prices)

    assert result == expected


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),  # Standard case
        ([], 3, []),  # Empty list
        ([4, 2, 3, 1, 5], 1, [4, 2, 3, 1, 5]),  # Window size 1
        ([1, 2, 3], 5, []),  # Window size larger than array
        ([-1, -3, -2, -5, -4], 3, [-1, -2, -2]),  # Negative numbers
        ([7, 7, 7, 7, 7], 2, [7, 7, 7, 7]),  # Identical elements
        ([4], 1, [4]),  # Single element array
        ([1, 3, 2, 5, 4, 8, 7, 6, 9], 4, [5, 5, 8, 8, 8, 9]),  # Large window
        (
            [10, 10, 10, 10, 10],
            2,
            [10, 10, 10, 10],
        ),  # Array with one element multiple times
    ],
)
def test_sliding_window_max_bf(arr, k, expected):
    # Call the sliding_window_max_bf function and compare the result to the expected output
    result = sliding_window_max_bf(arr, k)
    assert result == expected
