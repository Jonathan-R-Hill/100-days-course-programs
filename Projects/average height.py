heights = input("Input a bunch of heights spaced out: ").split()

# Converts the input list to intigers
for i in range(0, len(heights)):
    heights[i] = int(heights[i])
print(heights)

total = 0

# Adds togeather everything in the list
for i in heights:
    total += i

# Divides total by how many inputs were in the list to get the average
average = total / len(heights)
print(f'The Average height is: {average}')