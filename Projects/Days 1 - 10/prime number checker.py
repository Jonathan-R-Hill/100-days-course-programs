
number = int(input("Enter a number to check: "))

is_prime = ""

"""
Loop to go through the input / number( given as input) 
up to the number chosen.
if it finds another number that divides into it eg:
    
    (6) where 3 * 2 = 6 it will break the loop
    and change {is_prime} to  "is not prime"
 """
 
for i in range(2, number):
    if number % i == 0:
        is_prime = "is NOT a Prime number"
        break
    else:
        is_prime = "IS a Prime number"

print(f"The number: {number} {is_prime}")