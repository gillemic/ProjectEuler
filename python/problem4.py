''' A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. '''

import time

start = time.time()

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

end = time.time() - start

print("Program took " + str(end) + " seconds")


'''
> 
python3 problem4.py
906609 = 913 x 993
Program took 0.811882495880127 seconds

'''