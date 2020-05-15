''' 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000? '''

import time
import math

start = time.time()

def sum_of_power(n):
    number = str(2**n)
    num_list = [int(i) for i in number]
    
    return sum(num_list)
    

print(sum_of_power(1000))

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> python3 problem16.py
1366
Time elapsed: 0.0 seconds

'''