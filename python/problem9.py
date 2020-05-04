''' A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. '''

import time

start = time.time()

def calc():
  for a in range(1,1000):
    for b in range(1,1000):
      c = 1000-a-b
      if (a**2+b**2) == c**2:
        print(a*b*c)
        return

calc()

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> python3 problem9.py
31875000
Time elapsed: 0.20799851417541504 seconds

'''