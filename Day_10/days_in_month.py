year = int(input("Enter the year you want to check"))
month = input("Enter the month you want to check")


def leap_year_check(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    if month == 'February' and leap_year_check(year):
        return 29
    elif month == 'February' and not leap_year_check(year):
        return 28
    elif month == ('January' or 'March' or 'May' or 'July' or 'August' or 'October' or 'December'):
        return 31
    else:
        return 30


print(days_in_month(year, month))
