import random

names = ['John', 'Angela', 'Lilly', 'Jenny', 'Kane', 'Michael']

rand = random.randint(0, len(names)-1)

print(f"{names[rand]} is paying for dinner")