scores = input("Input a bunch of scores spaced out: ").split()

# Converts the input list to intigers
for i in range(0, len(scores)):
    scores[i] = int(scores[i])
print(scores)

"""
print(f'The highest score is: {max(scores)}')
print(f'The lowest score is: {min(scores)}')
"""

score = 0

# Same as max function above done in a loop
for i in range(len(scores)):
    if scores[i] > score:
        score = scores[i]

print(f'the highest score is: {score}')