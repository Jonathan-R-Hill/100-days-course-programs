# Original code:
"""
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
"""

# Fixed bug (edited code)
number = int(input("Which number do you want to check?"))

if number % 2 == 0: # bug was here it was just a "=" instead of "=="
    print("This is an even number.")
else:
    print("This is an odd number.")