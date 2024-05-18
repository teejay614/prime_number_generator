# prime_number_generator
Prime Number Generator

This is a prime number generator program that returns an ordered list of all prime numbers in a given range,
inclusive of the endpoints. You can run the app and provide input for the range to receive the prime numbers through the command line.

My journey to building this app:

This is a coding challenge focused on building tests around a prime number generator. I had no clue at first how to get the prime number of anything and just remembered numbers like 7 and 13 were prime. So, I went to Wikipedia / Google to search more about how to determine if a number is prime. 

I read up on Sieve of Eratosthenes algorithm, and found a formula. I then began to write out some if statements and loops to go through an entire list and find if the numbers in the list were prime based off the formula. As I was doing this I thought to myself why try and reinvent the wheel.

So, I used one of my favorite languages python, and found out that there is a library out there that does this for me. It's called sympy. I figured since the coding challenge was focusing on Test Driven Development I should hone in on writing the tests first and then having a simple program with a method using sympy to provide a list of prime numbers. You will see in test_main.py those tests.

The tests fulfilled the coding challenge of making sure the following requirements were met:
1. The code should handle inverse ranges such that 1-10 and 10-1 are equivalent.
2. Ensure a test exists for the range 7900 and 7920 (valid primes are 7901, 7907, 7919).

I also built a test for testing w/ negative numbers which shouldn't return any results.

I also built a test for testing w/ non-integer values. I commented it out of the test because it fails due to the fact that the code does not know how to handle when a non-integer value is entered. Since there isn't a requirement to make sure that non-integer values should be handled.

I still created a test that would handle the TypeError being raised when entering non-integer values. Once there is a fix for the TypeError then the test will fail and then will have to adjust the test to match how the app will handle TypeErrors.


1. Clone repository
2. run `pip3 install -r requirements.txt ` in root directory
3. to run app manually `python3 main.py` in root directory
4. to run tests `pytest` in root directory  