def check_float(str_val):
    try:
        return float(str_val)
    except ValueError:
        return 'Incorrect input format'


def compare_strings(str_one, str_two):
    ''' simple class that compare the first string is either equal or greater or lesser than second string '''
    val_one = check_float(str_one)
    val_two = check_float(str_two)

    if val_one == val_two:
        return '{} is equal to {}'.format(val_one, val_two)
    elif val_one > val_two:
        return '{} is greater than {}'.format(val_one, val_two)
    else:
        return '{} is lesser than {}'.format(val_one, val_two)


if __name__ == '__main__':
    str_one = input('Enter first string Number: ')
    str_two = input('Enter second string Number: ')

    print(compare_strings(str_one, str_two))
