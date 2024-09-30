# in-class coding from Monday, September 30

def calculate_days(years, months, days):
    num_days = 365 * years + 30 * months + days
    if years > 4:
        num_days += 1
    return num_days


if __name__ == '__main__':
    yrs = 22
    mos = 3
    days = 23
    length_of_time = calculate_days(yrs, mos, days)
    print(length_of_time)
    length2 = calculate_days(mos, days, yrs)
    print(length2)




#    calculate_days(yrs, mos, days) = 5 only thing you
# can't do with a function call

