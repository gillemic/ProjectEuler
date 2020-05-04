''' n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100! '''

import time
import math
import sys

start = time.time()

def sum_of_factorial(n):
    fact = str(math.factorial(n))

    print(str(n) + '! = ' + fact)
    print(sum([int(i) for i in fact]))

def main():
    if len(sys.argv) > 1 and int(sys.argv[1]) >= 0:
        n = int(sys.argv[1])
    else:
        n = 100

    sum_of_factorial(n)

if __name__ == '__main__':
    main()

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> python3 problem20.py
100! = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
Sum of digits: 648
Time elapsed: 0.001003265380859375 seconds

'''