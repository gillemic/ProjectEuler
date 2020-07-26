import time
import math

start = time.time()

def is_pentagonal(n):
  #formula for finding pentagon nums
  if (1+(24*n+1)**0.5) % 6 == 0:
    return True
  return False

def is_hexagonal(n):
  #formula for finding hexagonal nums
  if (1+(8*n + 1)**0.5) % 4 == 0:
    return True
  return False

def find_nums():
  #generate triangle nums starting at 286th term, 100,000 was arbitrary limit- could be anything
  triangle_nums = [i*(i+1)/2 for i in range(286, 100000)]

  #iterate through triangle nums and check if they are also pentagonal and hexagonal
  for n in triangle_nums:
    if (is_pentagonal(n) and is_hexagonal(n)):
      index = triangle_nums.index(n)
      print("Next num: %d at index %d" % (n, index+286))
      return

def main():
  find_nums()

if __name__ == '__main__':
  main()

print("Time elapsed: {} seconds".format(time.time() - start))