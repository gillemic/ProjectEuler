#importing time module 
import time

#time at the start of execution
start = time.time()

def fib(i, j):
    return i + j

def fib_length(n):
    i = 2
    k = 1
    j = 1
    while len(str(k)) < n:
        k = fib(k, j)
        j = k - j
        i += 1

    return i

def main():
    print(fib_length(1000))
    pass

if __name__ == '__main__':
    main()

#printing the total time
print("Time elapsed: " + str(time.time() - start) + " seconds")