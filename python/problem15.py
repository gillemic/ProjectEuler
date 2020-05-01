import time
import math

start = time.time()

def lattice_paths(n):
    n_fact = math.factorial(n)
    return math.factorial(2 * n) / n_fact / n_fact

print(lattice_paths(20))

print("Time elapsed: " + str(time.time() - start) + " seconds")