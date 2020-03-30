start = 1
maxim = 100

sum_of_squares = 0
square_of_sums = 0

for i in range(start, maxim+1):
	sum_of_squares += i * i
	square_of_sums += i

final = square_of_sums * square_of_sums

print(str(final) + " " + str(sum_of_squares))
print(final - sum_of_squares)