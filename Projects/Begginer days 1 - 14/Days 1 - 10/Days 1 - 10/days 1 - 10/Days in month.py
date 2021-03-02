year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        
        elif year % 400 == 0:
            return True
        
        else:
            return False
        
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      
    if is_leap(year) == True:
        month_days[1] = 29
    
    else:
        month_days[1] = 28
    
    days = month_days[month - 1]
    
    total_days = 0
    for i in month_days:
        total_days += i
    
    return (f"Month {month} has {days} days in it. There are {total_days} in that year")

print(days_in_month(year, month))
  

