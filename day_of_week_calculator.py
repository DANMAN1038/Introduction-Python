def dateConversion(month, day, year):
    if month == 1:
        month = 13
        return month
    elif month == 2:
        month = 14
        return month
    day_of_week = ((day + 5 + (26*(month + 1)//10)) + ((5 * (year % 100))//4) + ((21 * (year//100))//4))%7
    if day_of_week == 0:
        week_day = "Monday"
        return week_day
    if day_of_week == 1:
        week_day = "Tuesday"
        return week_day
    if day_of_week == 2:
        week_day = "Wednesday"
        return week_day
    if day_of_week == 3:
        week_day = "Thursday"
        return week_day
    if day_of_week == 4:
        week_day = "Friday"
        return week_day
    if day_of_week == 5:
        week_day = "Saturday"
        return week_day
    if day_of_week == 6:
        week_day = "Sunday"
        return week_day
def main():
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    year = int(input("Enter year: "))
    print(day, "/", month, "/", year, "is a", dateConversion(day, month, year))
    
