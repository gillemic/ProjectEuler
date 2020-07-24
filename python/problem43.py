import time
from itertools import permutations

start = time.time()

def generate_pandigitals():
  return permutations('0123456789')

def check_primes():
  total = 0
  primes = [17, 13, 11, 7, 5, 3, 2]
  perms = generate_pandigitals()

  for i in perms:
    if i[0] == '0':
      continue

    n = ''.join(list(i))
    valid = True

    for j in range(0, len(primes)):
      x = n[len(primes)-j:len(primes)-j+3]
      if int(x) % primes[j]:
        valid = False
        break

    if valid:
      print('Valid number: %s' % n)
      total += int(n)
  
  print("Total: %d" % total)

def main():
  check_primes()
  pass

if __name__ == '__main__':
  main()

print("Time elapsed: {} seconds".format(time.time() - start))