import time

start = time.time()

def generate_primes(n):
  sieve = [True] * n
  for i in range(3, int(n**0.5)+1, 2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)

  return [2] + [i for i in range(3,n,2) if sieve[i]]

def find_prime_streak(prime_list):
  length = 0
  highest = 0
  lastj = len(prime_list)
  for i in range(len(prime_list)):
    for j in range(i+length, lastj):
      sol = sum(prime_list[i:j])
      if sol < 1000000:
        if sol in prime_list:
          length = j-i
          highest = sol
      else:
        lastj = j+1
        break

  print(highest)

def main():
  primes = generate_primes(1000000)
  find_prime_streak(primes)
  pass

if __name__ == '__main__':
  main()

print("Time elapsed: {} seconds".format(time.time() - start))