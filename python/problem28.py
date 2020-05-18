import time

start = time.time()

def find_diagonals(n):
    summ = 1
    if (n < 3):
        return 1
    elif (n % 2 == 0):
        return 1
    else:
        for i in range(1, n, 2):
            for j in range(1, 5):
                summ += (i*i + j*(i+1))
        return summ

def main():
    print(find_diagonals(1001))

if __name__ == '__main__':
    main()