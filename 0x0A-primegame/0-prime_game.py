#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): Array containing the values of n for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"), or None if no winner.
    """
    def sieve_of_eratosthenes(n):
        """Generate a list of prime numbers up to n using the Sieve of Eratosthenes."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, n + 1, i):
                    primes[multiple] = False
        return primes

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_counts = [0] * (max_n + 1)

    # Precompute the count of primes up to each number
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
