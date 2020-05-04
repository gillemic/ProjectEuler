''' You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? '''

import time
import sys

start = time.time()

def first_sundays_since_1901(end_year):
    num_of_sundays = 0
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    thirty_day_months = ['April', 'June', 'September', 'November']
    year = 1901
    days_in_month = 31
    current_day = 1

    while (year < end_year + 1):
        for i in range(0, 12):
            if months[i] == 'February' and (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)):
                days_in_month = 28
            elif months[i] == 'February' and year % 4 == 0:
                days_in_month = 29
            elif months[i] in thirty_day_months:
                days_in_month = 30
            else:
                days_in_month = 31

            if days_of_week[current_day] == 'Sunday':
                print(months[i] + " 1st, " + str(year) + " was on a Sunday")
                num_of_sundays += 1

            current_day = (current_day + (days_in_month % 7)) % 7

        year += 1
    
    print("\nTotal Sundays: " + str(num_of_sundays) + "\n")

def main():
    if len(sys.argv) > 1 and int(sys.argv[1]) > 1901:
        n = int(sys.argv[1])
    else:
        n = 2000

    first_sundays_since_1901(n)

if __name__ == '__main__':
    main()

print("Time elapsed: " + str(time.time() - start) + " seconds")


'''
> python3 problem19.py

Total Sundays: 171
Time elapsed: 0.06399989128112793 seconds

'''