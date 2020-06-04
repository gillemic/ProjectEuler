import time
from math import factorial

start = time.time()

def find_factorial_sum():
    factorial_sums = []
    for i in range(3, 100000):
        total = 0
        nums = list(str(i))
        for j in nums:
            total += factorial(int(j))

        if (total == i):
            factorial_sums.append(i)
    
    print(factorial_sums)


def main():
    find_factorial_sum()
    pass

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))