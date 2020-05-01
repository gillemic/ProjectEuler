import time

start = time.time()

def first_sundays_since_1901(end_year):
    num_of_sundays = 0
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    thirty_day_months = ['April', 'June', 'September', 'November']
    year = 1901
    day = 1
    month = 1
    days_in_month = 31
    current_day = 1

    while (year < end_year + 1):
        for i in range(0, 12):
            if months[i] == 'February' and year % 4 != 0:
                days_in_month = 28
            elif months[i] == 'February' and year % 4 == 0:
                days_in_month = 29
            elif months[i] in thirty_day_months:
                days_in_month = 30
            else:
                days_in_month = 31

            if days_of_week[current_day] == 'Sunday':
                num_of_sundays += 1

            current_day = (current_day + (days_in_month % 7)) % 7

        year += 1
    
    print(num_of_sundays)

first_sundays_since_1901(2000)