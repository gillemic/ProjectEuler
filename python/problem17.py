''' If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage. '''

import time

start = time.time()

def word_num(n):
    if n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'
    elif n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'
    elif n == 20:
        return 'twenty'
    elif 20 < n < 30:
        return 'twenty-' + word_num(n - 20)
    elif n == 30:
        return 'thirty'
    elif 30 < n < 40:
        return 'thirty-' + word_num(n - 30)
    elif n == 40:
        return 'forty'
    elif 40 < n < 50:
        return 'forty-' + word_num(n - 40)
    elif n == 50:
        return 'fifty'
    elif 50 < n < 60:
        return 'fifty-' + word_num(n - 50)
    elif n == 60:
        return 'sixty'
    elif 60 < n < 70:
        return 'sixty-' + word_num(n - 60)
    elif n == 70:
        return 'seventy'
    elif 70 < n < 80:
        return 'seventy-' + word_num(n - 70)
    elif n == 80:
        return 'eighty'
    elif 80 < n < 90:
        return 'eighty-' + word_num(n - 80)
    elif n == 90:
        return 'ninety'
    elif 90 < n < 100:
        return 'ninety-' + word_num(n - 90)
    elif n == 100:
        return 'one hundred'
    elif 100 < n < 200:
        return 'one hundred and ' + word_num(n - 100)
    elif n == 200:
        return 'two hundred'
    elif 200 < n < 300:
        return 'two hundred and ' + word_num(n - 200)
    elif n == 300:
        return 'three hundred'
    elif 300 < n < 400:
        return 'three hundred and ' + word_num(n - 300)
    elif n == 400:
        return 'four hundred'
    elif 400 < n < 500:
        return 'four hundred and ' + word_num(n - 400)
    elif n == 500:
        return 'five hundred'
    elif 500 < n < 600:
        return 'five hundred and ' + word_num(n - 500)
    elif n == 600:
        return 'six hundred'
    elif 600 < n < 700:
        return 'six hundred and ' + word_num(n - 600)
    elif n == 700:
        return 'seven hundred'
    elif 700 < n < 800:
        return 'seven hundred and ' + word_num(n - 700)
    elif n == 800:
        return 'eight hundred'
    elif 800 < n < 900:
        return 'eight hundred and ' + word_num(n - 800)
    elif n == 900:
        return 'nine hundred '
    elif 900 < n < 1000:
        return 'nine hundred and ' + word_num(n - 900)
    elif n == 1000:
        return 'one thousand'

total_chars = 0

for i in range(1000):
    num_string = word_num(i+1)
    count = len(num_string.replace('-', '').replace(' ', ''))
    print(num_string)
    print(count)
    total_chars += count

print("Total characters: " + str(total_chars))

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> python3 problem17.py
Total characters: 21124
Time elapsed: 0.8109941482543945 seconds

'''