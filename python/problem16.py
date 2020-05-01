import time
import math

start = time.time()

def sum_of_power(n):
    number = str(2**n)
    num_list = [int(i) for i in number]
    
    return sum(num_list)
    

print(sum_of_power(1000))

print("Time elapsed: " + str(time.time() - start) + " seconds")