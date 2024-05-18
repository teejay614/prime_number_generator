import pytest

from main import generate_primes

def test_generate_primes():
    # Test normal range
    assert generate_primes(1, 10) == [2, 3, 5, 7]
    
    # Test inverse range
    assert generate_primes(10, 1) == [2, 3, 5, 7]

    # Test range with valid primes 7900-7920
    assert generate_primes(7900, 7920) == [7901, 7907, 7919]

    # Test range with no primes
    assert generate_primes(8, 10) == []

    # Test range from Wikipedia list
    assert generate_primes(1,101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    #Test negative numbers
    assert generate_primes(-1,-23) ==[]

def test_generate_primes_with_non_integer_inputs():
    with pytest.raises(TypeError):
        generate_primes('am', 'cool')

if __name__ == "__main__":
    pytest.main()