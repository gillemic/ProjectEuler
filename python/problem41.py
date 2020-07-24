import time
import math

start = time.time()

def is_pandigital(x):
    s = str(x)
    return set(list(range(1,len(s)+1))) == set([int(i) for i in s])

def generate_primes(n):
    # sieve of eratosthenes
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def pandigital_primes():
    highest = 0
    prime_list = generate_primes(10000000)
    for i in prime_list:
        if (is_pandigital(i) and i > highest):
            highest = i

    print(highest)
    print(max(prime_list))

def main():
    pandigital_primes()

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))