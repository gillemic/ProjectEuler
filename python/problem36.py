import time

start = time.time()

def palidrome_nums(n):
    pals = []
    for i in range(1, n):
        num = str(i)
        bin_num = bin(i)[2:]
        if (num == num[::-1] and bin_num == bin_num[::-1]):
            pals.append(i)

    print(pals)
    print(sum(pals))

def main():
    palidrome_nums(1000000)
    pass

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))