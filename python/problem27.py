'''
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''
#importing time module 
import time
import math

#time at the start of execution
start = time.time()

def is_prime(n):
    for i in range(2, (math.ceil(math.sqrt(math.fabs(n))))):
        if (n % i == 0):
            return False
        
    return True

def check_coefficients(a, b):
    prime_streak = i = 0
    while True:
        if is_prime((i ** 2) + (i * a) + b):
            prime_streak += 1
            i += 1
        else:
            return prime_streak

def main():
    highest = 0
    a = b = 0
    for i in range(-999, 999):
        for j in range(-1000, 1000):
            result = check_coefficients(i, j)
            if (result > highest):
                highest = result
                a = i
                b = j
    
    print("Longest prime streak: 0-{}\na = {}, b = {}".format(highest, a, b))

if __name__ == '__main__':
    main()

#printing the total time
print("Time elapsed: " + str(time.time() - start) + " seconds")