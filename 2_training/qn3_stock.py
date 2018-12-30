#!/usr/bin/env python3
def max_profit(arr):
    """max_profit(arr) --> a function taking an array of stock prices with indexes indicating the amount of time
    after the stock opening time, 9:30, gives out the maximum profit of purchasing and selling one item.

    :param arr: Array of integers
    :return: Integer
    """

    i = 0
    max_profit = 0
    while i < len(arr) - 1:
        purchase = arr[i]
        sale = max(arr[i+1:])
        profit = sale - purchase
        if profit > max_profit:
            max_profit = profit
        i = i + 1
    return max_profit

if __name__ == "__main__":
    stock_prices_yesterday = [10,7,5,8,11,9]
    print(max_profit( stock_prices_yesterday))
    arr = [3, 4, 5, 6, 8, 9, 1, 7, 8]
    print(max_profit(arr))