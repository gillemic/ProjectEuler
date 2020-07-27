import time

start = time.time()

def generate_non_primes(n):
    # sieve of eratosthenes, but return the non-primes starting at 9
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [i for i in range(9,n,2) if not sieve[i]]

def generate_primes(n):
    # sieve of eratosthenes
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def generate_twice_squares(n):
  return [2*(i**2) for i in range(1, n)]

def find_stuff():
  primes = generate_primes(10000)
  non_primes = generate_non_primes(10000)
  twice_squares = generate_twice_squares(50)
  
  # iterate through non_prime odd numbers
  for i in non_primes:
    #start True
    conjecture = True
    j = k = 0
    for j in primes:
      if i < j:
        break
      for k in twice_squares:
        if i < (j + k):
          break
        #iterate primes and twice squares, checking that they are below i, and if any combo is equal to i: the conjecture becomes false
        if (j + k == i):
          conjecture = False

    #if no combos result in i, the conjecture is disproved
    if conjecture:
      print(primes.index(j), twice_squares.index(k))
      return i

  print("None found. Try a bigger number?")

def main():
  print(find_stuff())
  pass

if __name__ == '__main__':
  main()

end = time.time() - start

print("Time elapsed: %f seconds" % end)