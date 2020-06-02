import time

start = time.time()

def is_pandigital(n, s=9):
    n = str(n)
    return len(n) == s and not '123456789'[:s].strip(n)

def find_pandigital(n):
    p = set()
    for i in range(2,  60):
        start = 1234 if i < 10 else 123 
        for j in range(start, 10000//i):
            if is_pandigital(str(i) + str(j) + str(i*j)): 
                p.add(i*j)
    print("Sum of products: " + str(sum(p)))
    print(p)

def main():
    find_pandigital(5)

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))