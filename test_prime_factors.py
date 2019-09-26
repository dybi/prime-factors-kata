from unittest import TestCase

from prime_factors import generate_prime_factors


class TestGeneratePrimeFactors(TestCase):
    def test_one_should_have_empty_prime_factors_list(self):
        self.assertEqual(generate_prime_factors(1), [])

    def test_two_should_have_two_on_prime_factors_list(self):
        self.assertEqual(generate_prime_factors(2), [2])

    def test_three_should_have_three_on_prime_factors_list(self):
        self.assertEqual(generate_prime_factors(3), [3])
