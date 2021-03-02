number = input('Enter a number: ')

total = 0
  
for i in range(len(number)):
    if number[i] == '.' or number[i] == ',':
        pass
    
    else:
        total += float(number[i])
    
print(int(total))