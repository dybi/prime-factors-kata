from typing import List


def generate_prime_factors(number: int) -> List[int]:
    primes = []
    if number > 1:
        primes.append(number)
    return primes
