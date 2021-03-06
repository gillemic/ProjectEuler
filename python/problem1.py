''' If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. '''

import time

start = time.time()

summ = 0

for i in range(1, 1000):
	if (i % 3 == 0) or (i % 5 == 0):
		summ += i

print(summ)

print("Operation took " + str(time.time() - start) + " seconds")


'''
> python3 problem1.py 
233168
Operation took 0.03300142288208008 seconds

'''