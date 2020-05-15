''' Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid? '''

import time
import math

start = time.time()

def lattice_paths(n):
    n_fact = math.factorial(n)
    return math.factorial(2 * n) // n_fact // n_fact

print(lattice_paths(20))

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> python3 problem15.py
137846528820
Time elapsed: 0.0 seconds

'''