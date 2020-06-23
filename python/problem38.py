import time

start = time.time()

def find_pandigitals():
    largest = 0
    for i in range(1, 10000):
        multiplication = ''
        integer = 1

        while len(multiplication) < 9:
            multiplication += str(i*integer)
            integer += 1
        
        if ((len(multiplication) == 9) and (len(set(multiplication)) == 9) and ('0' not in multiplication)):
            if int(multiplication) > largest:
                largest = int(multiplication)
    
    print(largest)

def main():
    find_pandigitals()

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))