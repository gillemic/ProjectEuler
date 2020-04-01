import math

maximum = 2000000
summ = 2

for i in range(3, maximum):
    isPrime = True
    for j in range(2, math.ceil(math.sqrt(i))+1):
        if (i % j == 0):
            isPrime = False

    if (isPrime):
        summ += i

print(summ)