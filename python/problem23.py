'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import time

#square root from math module
from math import sqrt

#time at the start of execution
start = time.time()

#Function used from problem 21
def divisors(n):
	"""This function will generate 
	divisors of given number
	Example: divisors(28) will give
	[1,2,4,7,14]"""
	divs = [1]
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			divs.extend([i,n//i])
	return list(set(divs))

#list to store the values of abundant numbers
ab = []

#For loop to generate the abundant numbers
for i in range(12,28123):
	if sum(divisors(i))>i:
		ab.append(i)

#first let us assume all the numbers are 
#not sum of abundant numbers
non_ab_sum = [x for x in range(28123)]

#for loop to generate sum of two 
#abundant numbers
for i in range(len(ab)):
	for j in range(i,28123):
		if ab[i]+ab[j] < 28123:
			#negating the value of the abundant sum
			non_ab_sum[ab[i]+ab[j]] = 0
		else:
			break

#printing the value of the sum of non abundant sum
print(sum(non_ab_sum))
        
#printing the total execution time
print("Time elapsed: " + str(time.time() -start) + " seconds")

'''
> python3 problem23.py
4179871
Time elapsed: 5.269253969192505 seconds

'''