''' Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000. '''

import time
import sys

start = time.time()

def check_divisors(n):
    divs = [1]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divs.append(i)

    return divs


def amicable_numbers(max):
    amicable_nums = [220, 284]
    for i in range(1, max+1):
        a_divisors = check_divisors(i)
        j = sum(a_divisors)
        b_divisors = check_divisors(j)

        if i == sum(b_divisors) and (i not in amicable_nums or j not in amicable_nums) and i != j:
            amicable_nums.append(i)
            amicable_nums.append(j)

    print(amicable_nums)
    print(sum(amicable_nums))

def main():
    if len(sys.argv) > 1 and int(sys.argv[1]) >= 0:
        n = int(sys.argv[1])
    else:
        n = 10000

    amicable_numbers(n)

if __name__ == '__main__':
    main()

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> python3 problem21.py
[220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
Sum: 31626
Time elapsed: 2.6568055152893066 seconds

'''