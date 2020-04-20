import time

start = time.time()


def collatz_sequence(num):
    numList = []
    numList.append(num)
    while True:
        if num == 1:
            numList.append(1)
            return numList
        elif num % 2 == 0:
            num = num // 2
            numList.append(num)

        elif num % 2 == 1:
            num = 3*num + 1
            numList.append(num)

        


def main():
    num = 2
    longest = 1
    while num < 1000000:
        sequence = collatz_sequence(num)
        if len(sequence) > longest:
            starting_num = num
            longest = len(sequence)
        num += 1
    
    print(longest)
    print(starting_num)

if __name__ == '__main__':
    main()

print("Time elapsed: " + str(time.time() - start) + " seconds")
