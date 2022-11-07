burgerheight = 2.75

def fromimperial():
    global burgerheight
    print('Mile (M), Nautical Mile (NM), Yard (Y), Feet (F), Inches (I)')
    determiner = input('')
    if determiner == 'M' or determiner == 'm':
        print('Enter Mile Number: ')
        miles = input('')
        toyards = float(miles) * 1760
        tofeet = toyards * 3
        toinches = float(tofeet) * 12
        toburger = toinches / burgerheight
        print('Yards: ' + str(toyards) + ' | Feet: ' + str(tofeet) + ' | Inches: ' + str(toinches))
        print('\n')
        print(str(miles) + ' miles is roughly ' + str(toburger) + ' burgers stacked vertically')
    elif determiner == 'NM' or determiner == 'nm':
        print('Enter Nautical Mile Number: ')
        miles = input('')
        nmiles = float(miles) * 1.151
        toyards = float(nmiles) * 1760
        tofeet = toyards * 3
        toinches = float(tofeet) * 12
        toburger = toinches / burgerheight
        print('Yards: ' + str(toyards) + ' | Feet: ' + str(tofeet) + ' | Inches: ' + str(toinches))
        print('\n')
        print(str(miles) + ' nautical miles is roughly ' + str(toburger) + ' burgers stacked vertically')
    elif determiner == 'Y' or determiner == 'y':
        print('Enter Yard Number:')
        yardy = input('')
        tofeet = float(yardy) * 3
        toinches = float(tofeet) * 12
        toburger = toinches / burgerheight
        print('Feet: ' + str(tofeet) + ' | Inches: ' + str(toinches))
        print('\n')
        print(str(yardy) + ' yards is roughly ' + str(toburger) + ' burgers stacked vertically')
    elif determiner == 'F' or determiner == 'f':
        print('Enter Foot Number: ')
        feets = input('')
        toinches = float(feets) * 12
        toburger = toinches / burgerheight
        print('Inches: ' + str(toinches))
        print('\n')
        print(str(feets) + ' feet is roughly ' + str(toburger) + ' burgers stacked vertically')
    elif determiner == 'I' or determiner == 'i':
        print('Enter Inch Number: ')
        inches = input('')
        toburger = float(inches) / burgerheight
        print(str(inches) + ' inches is roughly ' + str(toburger) + ' burgers stacked vertically')
    else:
        print('Invalid Entry, Re-Launch To Try Again')

def frommetric():
    global burgerheight
    print('Millimeter (MM), Centimeter (C), Meter (M), Kilometer (K)')
    determiner = input('')
    if determiner == 'MM' or determiner == 'mm':
        print('Enter Milimeter Number:')
        mm = input('')
        toinches = float(mm) / 25.4
        toburger = toinches / burgerheight
        print(str(mm) + ' is roughly ' + str(toburger) + ' burgers stacked vertically')
    elif determiner == 'C' or determiner == 'c':
        print('Enter Centimeter Number')
        c = input('')
        tomil = float(c) * 10
        toinches = tomil / 25.4
        toburger = toinches / burgerheight
        print(str(c) + ' centimeters is roughly ' + str(toburger) + ' burgers stacked vertically')
    elif determiner == 'M' or determiner == 'm':
        print('Enter Meter Number:')
        m = input('')
        tocent = float(m) * 100
        tomil = tocent * 10
        toinches = float(tomil) / 25.4
        toburger = toinches / burgerheight
        print(str(m) + ' meters is roughly ' + str(toburger) + ' burgers stacked vertically')
    elif determiner == 'K' or determiner == 'k':
        print('Enter Kilometer Number:')
        k = input('')
        tomet = float(k) * 1000
        tocent = tomet * 100
        tomil = tocent * 10
        toinches = float(tomil) / 25.4
        toburger = toinches / burgerheight
        print(str(k) + ' kilometers is roughly ' + str(toburger) + ' burgers stacked vertically')
    else:
        print('Invalid Entry, Re-Launch To Try Again')

def fromburger():
    print('Enter Burger Amount:')
    burgercount = input('')
    burgerusable = float(burgercount)
    theinches = burgerusable * burgerheight
    thefeet = theinches * 12
    theyards = thefeet * 3
    themiles = theyards * 1760

print('Convert To (T) or From Burger (F)')
whatone = input('')
if whatone == 't' or whatone == 'T':
    print('Imperial (I) or Metric (M)')
    unity = input('')
    if unity == 'I' or unity == 'i':
        try:
            fromimperial()
        except Exception as e:
            print('Well an error occurred, probably entering letters and other non numbers where the numbers should go...')
            print(e)
    elif unity == 'M' or unity == 'm':
        try:
            frommetric()
        except Exception as e:
            print('Well an error occurred, probably entering letters and other non numbers where the numbers should go...')
            print(e)
    else:
        print('Unrecognized Unit')
elif whatone == 'f' or whatone == 'F':
    try:
        fromburger()
    except Exception as e:
        print('Well an error occurred, probably entering letters and other non numbers where numbers are supposed to go...')
        print(e)
else:
    print('Option not recognized.  ' + str(whatone))
