#largest prime factor of 600851475143

import time

start = time.time()

n = 600851475143
i = 2

while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print(n)

print("Time elapsed: " + str(time.time() - start) + " seconds")