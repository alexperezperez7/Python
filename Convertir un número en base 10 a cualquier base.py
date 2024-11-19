number = input('Enter a number in base 10:')
number = int(number)
base = input('Enter the base to convert the number:')
base = int(base)

if base < 2 and base > 16:
    print('Please enter a base between 2 and 16')
else:
    if number == 0:
        print('The number', number, 'in base', base, 'is 0')
    else:
        digits = '0123456789ABCDEF'
        result = ''
        dividend = number
        
        while dividend > 0:
            remainder = dividend % base
            result = digits[remainder] + result
            dividend = dividend // base
    print('The number', number, 'in base', base, 'is:', result)
