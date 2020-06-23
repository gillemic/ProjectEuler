'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

import time
from statistics import mode

start = time.time()

def right_triangles(n):
    perimeters = []
    for i in range(1, 500):
        for j in range(i, 500):
            k = (i**2 + j**2)**0.5
            if int(k) == k and i+j+k <= 1000:
                perimeters.append(i+j+k)

    print(mode(perimeters))

def main():
    right_triangles(1000)
    pass

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))