flag = True
while flag:
    number = int(input('Enter number: '))
    if number > 0 and number != 7:
        print('Number is positive')
        flag = bool(input('Will you try again? '
                          '[Yes] - [Any key] + [Enter] to continue : '))
    elif number < 0:
        print('Number is negative')
        flag = bool(input('Will you try again? '
                          '[Yes] - [Any key] + [Enter] to continue : '))
    elif number == 0:
        print('Number is equal to zero')
        flag = bool(input('Will you try again? '
                          '[Yes] - [Any key] + [Enter] to continue : '))
    elif number == 7:
        print('Good bye')
        flag = False
