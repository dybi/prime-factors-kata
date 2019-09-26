from unittest import TestCase

from prime_factors import generate_prime_factors


class TestGeneratePrimeFactors(TestCase):
    def test_one_should_have_empty_prime_factors_list(self):
        self.assertEqual(generate_prime_factors(1), [])
