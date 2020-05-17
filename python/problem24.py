'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''

import time
import sys
from math import factorial

start = time.time()

def permutations(n, s):
    if len(s) == 1: 
        return s
    q, r = divmod(n, factorial(len(s)-1))
    return s[q] + permutations(r, s[:q] + s[q+1:])

def main():
	nums = '0123456789'
	n = 1000000

	print(permutations(n-1, nums))

if __name__ == '__main__':
    main()

print("Time elapsed: " + str(time.time() -start) + " seconds")