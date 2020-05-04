''' The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million. '''

import math
import time

start = time.time()

maximum = 2000000
summ = 2

for i in range(3, maximum):
    isPrime = True
    for j in range(2, math.ceil(math.sqrt(i))+1):
        if (i % j == 0):
            isPrime = False

    if (isPrime):
        summ += i

print(summ)
print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> python3 problem10.py
142913828922
Time elapsed: 194.82365608215332 seconds

needs optimizing very badly
'''