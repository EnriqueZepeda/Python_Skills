### Excercise 1 ###
#name = input('Please enter your name: ')
#print('Greetings ' + name)

### Excesrise 2 ###
hours = input('How many hours do you work per day?\n')
rate = input('How much do you get paid per hour?\n')
print('Hours: ' + hours)
print('Rate: '+ rate)

hours = float(hours)
rate = float(rate)
pay = round(hours*rate,2)

print('Pay:',pay)

### Excersise 5 ###
celsius = input('What\'s the temperture in degrees Celsius?\n')
print('°C: ' + celsius)

celsius = float(celsius)

farenheit = celsius*1.8 + 32

print('°F:',farenheit)

