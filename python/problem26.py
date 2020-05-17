#importing time module 
import time

#time at the start of execution
start = time.time()

def divide_up_to(x):
    num = longest = 1
    for n in range(3, x, 2):
        if n % 5 == 0:
            continue

        p = 1
        while (10 ** p) % n != 1:
            p += 1

        if p > longest:
            num, longest = n, p

    print(num)

def main():
    divide_up_to(1000)
    pass

if __name__ == '__main__':
    main()

#printing the total time
print("Time elapsed: " + str(time.time() - start) + " seconds")