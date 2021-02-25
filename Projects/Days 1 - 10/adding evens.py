total = 0
# starts at 1 and ends at 100. Adds any numbers to total that a divisable by 2
for i in range(1, 101):
    if i % 2 == 0:
        total += i
    
print(total)

# Same as above without the if statement
""""
for i in range(1, 101, 2):
    total += i
"""