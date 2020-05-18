#importing time module 
import time
import math

#time at the start of execution
start = time.time()

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if (n % i == 0):
            return False
        
    return True

def main():
    n = 97
    print("The value {} is {}".format(n, is_prime(n)))

if __name__ == '__main__':
    main()