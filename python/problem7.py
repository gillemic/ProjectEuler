''' By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number? '''

import time

start = time.time()

def nth_prime(n):
    counter = 2
    for i in range(3, n**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
               break
        else:
            counter += 1
        if counter == n:
            return i

print(nth_prime(10001))

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> 
python3 problem7.py
104743
Time elapsed: 0.18600010871887207 seconds

'''