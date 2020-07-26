import time
import math

start = time.time()

def is_triangle(n):
  square_root = math.floor(math.sqrt(n*2))
  if (square_root*(square_root+1) == n*2):
    return True
  return False

def is_pentagonal(n):
  if (1+(24*n+1)**0.5) % 6 == 0:
    return True
  return False

def is_hexagonal(n):
  if (1+(8*n + 1)**0.5) % 4 == 0:
    return True
  return False

def find_nums():
  flag = True
  i = 40756
  triangle_nums = [i*(i+1)/2 for i in range(286, 100000)]
  for n in triangle_nums:
    if (is_pentagonal(n) and is_hexagonal(n)):
      print("Next num: %d" % n)
      return

def main():
  find_nums()

if __name__ == '__main__':
  main()

print("Time elapsed: {} seconds".format(time.time() - start))