from typing import List


def generate_prime_factors(number: int) -> List[int]:
    primes = []
    candidate = 2
    while number > 1:
        while number % candidate == 0:
            primes.append(candidate)
            number /= candidate
        candidate += 1
    return primes
