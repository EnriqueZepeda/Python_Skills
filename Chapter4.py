### Excercise 1,2,3 ####
#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()
#def print_lyrics():
#    print('Hace algún tiempo')
#    print('en ese lugar')
#
#repeat_lyrics()

# Excercise #
def computepay():
    h = input("Enter Hours:")
    r = input("Enter Rate:")
    try:
        h = float(h)
        r = float(r)
    except:
        print("Error!")
        return
    
    if h > 40:
        pay = r*(40 + 1.5*(h-40))
    else:
    	pay = r*h
        
    print("Pay",pay)

computepay()

### Excercise 6 ###
#def computepay(hours,rate):
#    try:
#        hours = float(hours)
#        rate = float(rate)
#    except:
#        print('Error! Please enter a numeric input')
#        quit()
#        
#    if hours > 40:
#        pay = round(40*rate + (hours-40)*1.5*rate,2)
#    else:
#        pay = round(hours*rate,2)
#    
#    print('Pay:',pay)
#
#computepay(45,10)

### Excersise 7 ###
def computepay(score):
    try:
        score = float(score)
    except:
        print('Error! Please type a valid grade')
        return
    
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print('Error, bad score')

computepay(0)
computepay(0.5)
computepay(0.75)
computepay(0.85)
computepay(1.0)

computepay('perfect')
computepay(1.1)

