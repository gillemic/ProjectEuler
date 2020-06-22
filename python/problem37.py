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
    
    return prime_list

def truncatable_primes(prime_list):
    truncatables = set()
    for i in prime_list[4:]:
        nums = []
        digits = str(i)
        for j in range(1, len(digits)):
            nums.append(int(digits[j:]))
            nums.append(int(digits[:j]))
        if all(n in prime_list for n in nums):
            truncatables.add(i)
        

    
    print(truncatables)
    print(sum(truncatables))

def main():
    primes = find_primes(1000000)
    truncatable_primes(primes)

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))