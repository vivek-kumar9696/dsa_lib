from typing import List


def buy_sell_stocks(prices: List[int]) -> int:
    if len(prices) != 0:
        buy = prices[0]
        profit = 0
    else:
        return 0

    for stock in prices:
        if stock < buy:
            buy = stock
        else:
            new_profit = stock - buy
            if new_profit > profit:
                profit = new_profit

    return profit
