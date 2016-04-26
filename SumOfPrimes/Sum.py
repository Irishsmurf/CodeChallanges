import sys

def isPrime(n):
    if n % 2 == 0:
        return False

    for x in xrange(3, int(n/2), 2):
        if(n % x == 0):
            return False
    else:
        return True


num_primes = 1
sum_primes = 2
counter = 3

while num_primes < 1000:
    if isPrime(counter):
        sum_primes += counter
        num_primes += 1
    counter += 1

print sum_primes
