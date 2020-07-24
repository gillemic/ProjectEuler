import time

start = time.time()

def is_pentagonal(n):
    """function to check if the number
    is pentagonal number or not"""
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

def check_sums():
  flag = True

  # while loop iterator
  i = 1

  # while loop
  while flag:
    for j in range(1, i):
      a = i*(3*i-1)//2
      b = j*(3*j-1)//2
      if is_pentagonal(a+b) and is_pentagonal(a-b):
        print(a-b)
        flag = False
        break
    i += 1

def main():
  check_sums()
  pass

if __name__ == '__main__':
  main()

print("Time elapsed: {} seconds".format(time.time() - start))