''' The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. '''

import time

start = time.time()
maxim = 100

sum_of_squares = 0
square_of_sums = 0

for i in range(1, maxim+1):
	sum_of_squares += i * i
	square_of_sums += i

final = square_of_sums * square_of_sums

print(str(final) + " " + str(sum_of_squares))
print(final - sum_of_squares)

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> 
python3 problem6.py
25502500 338350
25164150
Time elapsed: 0.001001119613647461 seconds

'''