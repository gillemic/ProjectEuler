import time

start = time.time()

def champernowne(n):
    num_str = ''
    for i in range(1, n):
        num_str += str(i)

    product = int(num_str[0]) * int(num_str[9]) * int(num_str[99]) * int(num_str[999]) * int(num_str[9999]) * int(num_str[99999]) * int(num_str[999999])
    print(product)

def main():
    champernowne(1000000)
    pass

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))