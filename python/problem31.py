import time

start = time.time()

def find_combos(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0]*n

    for coin in coins:
        for i in range(coin, n+1):
            ways[i] += ways[i-coin]

    print("Ways to make change = {}".format(ways[n]))

def main():
    find_combos(400)

if __name__ == '__main__':
    main()

print("Time elapsed: {} seconds".format(time.time() - start))