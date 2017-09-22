name = input('Please type your name and pres Enter. ')
print('Hi,' + name + 'this program will convert integer numbers between three base')

while True:
    print('\n Your input options are: Quit, Binary, Decimal, Hexadecimal')
    command = input('Type the first letter of your choice and press Enter.')
    if len(command) < 1:
        # check prevents a crash when indexing to 1st charater continue
        command = command[0]
    if command in ['q', 'Q']:
        # exit the loop, which will quit the program
        break
    elif command in ['b', 'B']:
        mode = 'binary'
        base = 2
    elif command in ['d', 'D']:
        mode = 'decimal'
        base = 10
    elif command in ['h', 'H']:
        mode = 'hexadecimal'
        base = 16
    else:
        print('unrecognized option!')
        # restart at the top of the loop
        continue

    number_text = input('Type the ' + mode + ' integer number to convert:')
    # use exception handling since the conversion would crash on many inputs:
    try:
        # convert string to an integer of specified base:
        n = int(number_text, base)

    except ValueError:
        print('Invalid integer input. Try again.')
        continue

    print('in binary      {0: b}'.format(n))
    print('in decimal     {0: d}'.format(n))
    print('in hexadecimal {0: x}'.format(n))

print('all done now, bye!')