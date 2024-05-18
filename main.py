from prime_generator import PrimeGenerator

def main():
    prime_gen = PrimeGenerator()
    print("Prime Number Generator!")
    start = int(input("Enter the start point: "))
    end = int(input("Enter the end point: "))
    primes = prime_gen.generate_primes(start,end)
    print("Prime numbers between", start, "and", end, ":", primes)


if __name__ == "__main__":
    main()
