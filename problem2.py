summ = 2
i = 2
prev = 1

while (i < 4000000):
	i = i + prev
	prev = i - prev

	if (i % 2 == 0):
		summ += i

print(summ)