import time
import math

start = time.time()

def isPrime(x):
    if (x == 2):
        return True
    if (x % 2 == 0 or x == 1):
        return False
    for i in range(3, (math.ceil(math.sqrt(x)))+1, 2):
        if (x % i == 0):
            return False
        
    return True

def find_primes(n):
    prime_list = [2]
    for i in range(3, n, 2):
        if (isPrime(i)):
            prime_list.append(i)
    
    find_circular_primes(prime_list)

def find_circular_primes(prime_list):
    circular_primes = set()
    for i in prime_list:
        nums = list(str(i))
        rotations = []
        for j in range(len(nums)):
            new = nums[j:] + nums[:j]
            rotations.append(int(''.join(new)))

        if all([isPrime(n) for n in rotations]):
            circular_primes.update(rotations)

    print(sorted(circular_primes))
    print(len(circular_primes))

def main():
    find_primes(1000000)

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))