#!/usr/bin/python3
"""
Module to calculate the minimum number of operations
to reach exactly n H characters in the file.
"""

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    # Iterate over the possible factors starting from 2
    while factor * factor <= n:
        # If 'factor' is a divisor of 'n', it means we can "Copy All" 
        # and then "Paste" factor times
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    # If there is any remaining prime factor greater than sqrt(n), add it to the operations
    if n > 1:
        operations += n
    
    return operations
