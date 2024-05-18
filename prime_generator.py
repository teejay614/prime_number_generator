import sympy

class PrimeGenerator:
    def __init__(self):
        pass

    def generate_primes(self, start, end):
        # Ensure start is less than or equal to end
        if start > end:
            # Swap start and end if they are in reverse order
            start, end = end, start
        
        # Generate prime numbers in the range [start, end]
        primes = list(sympy.primerange(start, end + 1))
        
        return primes
