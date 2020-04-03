#fib sequence
#sum of even numbers under 4000000
import time

start = time.time()

summ = 2
i = 2
prev = 1

while (i < 4000000):
	i = i + prev
	prev = i - prev

	if (i % 2 == 0):
		summ += i

print(summ)

print("Operation took " + str(time.time() - start) + " seconds")