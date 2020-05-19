import time

#time at the start of program execution
start = time.time()

#for loop to loop till 5(10-1)^5
def find_solution(n):
    solution = 0
    for i in range(2, n*(9**n)+1):
        if sum([int(x)**n for x in str(i)]) == i:
            solution += i
            print(i)
    return solution

#printing the solution
def main():
    print(find_solution(5))

if __name__ == '__main__':
    main()

#time at the end of execution
end = time.time()

#printing the total execution time
print(end - start)