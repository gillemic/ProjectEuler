# Sum of all multiples of 3 or 5 below 1000
import time

start = time.time()

sum = 0

for i in range(1, 1000):
	if (i % 3 == 0) or (i % 5 == 0):
		sum += i

print(sum)

print("Operation took " + str(time.time() - start) + " seconds")