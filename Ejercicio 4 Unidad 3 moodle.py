number = input('Enter the number:')
number = int(number)
base = ('Enter the base:')
base = int(base)

if base < 2 or base > 36:
    print('The base must be betwen 2 and 36')
else:
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    if number == 0:
        result = '0'
    else:
        original_number = number
        while number > 0:
            remainder = number % base
            result = digits[remainder] + result
            number = number // base
    print('The original number', original_number, 'in base', base, 'is:', result)
