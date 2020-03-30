i = 1
largest = 2

for j in range(3, 1000000):
	isPrime = True
	for k in range(2, j-1):
		if (j % k == 0):
			isPrime = False
			break

		if (isPrime):
			i+=1

		if i == 10001:
			largest = j
			break



print(largest)

