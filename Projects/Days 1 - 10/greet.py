"""
def hi():
    a = input('Enter a name: ')
    b = input('Enter a name: ')
    c = input('Enter a name: ')
    
    print(f"Hi {a}")
    print(f"Hi {b}")
    print(f"Hi {c}")
"""

name = input("What's your name? ")
location = input('Where are you from? ')
def greet(name, location):
    print(f"Welcome to the party {name} from {location}")

greet(name = name, location = location)

