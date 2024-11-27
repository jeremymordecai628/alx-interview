#!/usr/bin/python3
"""
Module for solving the coin change problem.
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The target amount.
        
    Returns:
        int: Fewest number of coins needed to meet total, or -1 if it's not possible.
    """
    if total <= 0:
        return 0
    
    # Initialize DP array with a value higher than the maximum possible number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total of 0

    for i in range(coin, total + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1