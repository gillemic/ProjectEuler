#largest palindrome product of two 3 digit numbers

highest = 0

x = 1
y = 1

for i in range(100, 999):
	for j in range(100, 999):
		total = str(i * j).split()[0]
		if total == total[::-1] and int(total) > highest:
			highest = int(total)
			x = i
			y = j

print(str(highest) + " = " + str(x) + " x " + str(y))