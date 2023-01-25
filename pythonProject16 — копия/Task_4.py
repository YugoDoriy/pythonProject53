flag = 'SomeRandomResultWhichCannotBeEnterByUser'
sum_range = 0
number_1 = 0
number_2 = 0
while flag:
    number = int(input('Enter number: '))
    if number == 7:
        print('Good bye')
        flag = 0
    elif number != 7 and flag == 'SomeRandomResultWhichCannotBeEnterByUser':
        sum_range += number
        result_range = f'The sum of all numbers are {sum_range}'
        max_digit = number
        result_max_digit = f'The maximum digit are {max_digit}'
        min_digit = number
        result_min_digit = f'The minimum digit are {min_digit}'
        print(result_range)
        print(result_max_digit)
        print(result_min_digit)
        flag = bool(input('Will you try again? '
                          '[Yes] - [Any key] + [Enter] to continue : '))
    elif number != 7 and flag:
        sum_range += number
        result_range = f'The sum of all numbers are {sum_range}'
        if number > max_digit:
            max_digit = number
            result_max_digit = f'The maximum digit are {max_digit}'
        if number < min_digit:
            min_digit = number
            result_min_digit = f'The minimum digit are {min_digit}'
        print(result_range)
        print(result_max_digit)
        print(result_min_digit)
        flag = bool(input('Will you try again? '
                          '[Yes] - [Any key] + [Enter] to continue : '))