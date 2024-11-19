number = input('Please enter the integer value:')
number = int(number)
value = number
result = ''

if number == 0:
    result == '0'
else:
    while number > 1:
        remainder = number % 2
        number = int(number / 2)
        #number = number // 2
        result = str(remainder) + result
    result = '1' + result
print(value, 'as binary is written:', result)
