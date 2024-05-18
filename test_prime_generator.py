import pytest
from prime_generator import PrimeGenerator


@pytest.fixture
def prime_generator():
    # Setup: create an instance of PrimeGenerator
    generator = PrimeGenerator()
    return generator


def test_normal_range(prime_generator):
     assert prime_generator.generate_primes(1, 10) == [2, 3, 5, 7]

def test_inverse_range(prime_generator):
    assert prime_generator.generate_primes(10, 1) == [2, 3, 5, 7]

def test_range_7900_to_7920(prime_generator):
    assert prime_generator.generate_primes(7900, 7920) == [7901, 7907, 7919]

def test_range_with_no_primes(prime_generator):
    assert prime_generator.generate_primes(8, 10) == []

def test_range_from_wikipedia_list(prime_generator):
    assert prime_generator.generate_primes(1,101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def test_negative_numbers(prime_generator):
    assert prime_generator.generate_primes(-1,-23) ==[]

def test_negative_number_to_non_negative_number_range(prime_generator):
    assert prime_generator.generate_primes(-9, 8)== [2,3,5,7]

def test_non_negative_to_negative_number_range(prime_generator):
    assert prime_generator.generate_primes(-8, 9)== [2,3,5,7]

def test_generate_primes_with_non_integer_inputs(prime_generator):
    with pytest.raises(TypeError):
        prime_generator.generate_primes('start_string_test', 'end_string_test')