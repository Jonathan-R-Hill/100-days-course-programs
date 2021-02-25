weeks_in_year = 52
months_in_year = 12
days_in_year = 365



age = input('How old are you? ')
age_as_int = int(age)

days_till_ninty = (days_in_year * 90) - (age_as_int * days_in_year)
weeks_till_ninty = (weeks_in_year * 90) - (age_as_int * weeks_in_year)
months_till_ninty = (months_in_year * 90) - (age_as_int * months_in_year)

months_old = age_as_int * months_in_year
weeks_old = age_as_int * weeks_in_year
days_old = age_as_int * days_in_year

print(f"You are {months_old} months old and you have {months_till_ninty} months till you're 90")
print(f"You are {weeks_old} weeks old and have {weeks_till_ninty} weeks till you're 90")
print(f"You are {days_old} days old and you have {days_till_ninty} days till you turn 90")
