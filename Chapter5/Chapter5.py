### Ejercicio 1 ###
total = 0
count = 0
average = None
number = None
while number != 'done':
    number = input('Enter data:')
    if number == 'done':
        print('Total:', total)
        print('Count:', count)
        print('Averae:', average)
        break
    try:
        number = float(number)
    except:
        print('invalid input')
        continue
    total = total + number
    count = count + 1
    average = total/count
    
### Ejercicio 2 ###
minimum = None
maximum = None
number = None
while number != 'done':
    number = input("Enter data:")
    if number == 'done':
        print(minimum)
        print(maximum)
        break
    try:
        number = float(number)
    except:
        print('invalid input')
        continue
    if minimum is None:
        minimum = number
        maximum = number
        
    if number < minimum:
        minimum = number
    elif number > maximum:
        maximum = number
