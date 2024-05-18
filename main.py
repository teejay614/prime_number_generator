import sympy

def generate_primes(start, end):
    # Ensure start is less than or equal to end
    if start > end:
        # Swap start and end if they are in reverse order
        start, end = end, start
    
    # Generate prime numbers in the range [start, end]
    primes = list(sympy.primerange(start, end + 1))
    
    return primes

def main():
    print("Prime Number Generator!")
    start = int(input("Enter the start point: "))
    end = int(input("Enter the end point: "))
    primes = generate_primes(start,end)
    print("Prime numbers between", start, "and", end, ":", primes)


if __name__ == "__main__":
    main()
