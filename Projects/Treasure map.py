row1 = ['🧳', '🧳', '🧳']
row2 = ['🧳', '🧳', '🧳']
row3 = ['🧳', '🧳', '🧳']

map1 = [row1, row2, row3]
print(f"{row1} 1\n{row2} 2\n{row3} 3\n")

position = input('Where do you want to put the treasure? enter 2 numbers (1-3) split by a comma: ')

pos = position.split(',')

if pos[0] == '1':
    if pos[1] == '1':
        row1[0] = '💼'
        
    elif pos[1] == '2':
        row1[1] = '💼'
        
    elif pos[1] == '3':
        row1[2] = '💼'
        
elif pos[0] == '2':
    if pos[1] == '1':
        row2[0] = '💼'
        
    elif pos[1] == '2':
        row2[1] = '💼'
        
    elif pos[1] == '3':
        row2[2] = '💼'

elif pos[0] == '3':
    if pos[1] == '1':
        row3[0] = '💼'
        
    elif pos[1] == '2':
        row3[1] = '💼'
        
    elif pos[1] == '3':
        row3[2] = '💼'
        
print(f"{row1}\n{row2}\n{row3}\n")