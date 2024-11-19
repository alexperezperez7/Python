number1 = input('Enter the first number:')
number1 = int(number1)
number2 = input('Enter the second number:')
number2 = int(number2)

i = 0

if number1 > number2:
    print('The number1 must be less than number2')
else:
    if number1 % 2 != 0:
        number1 += 1
    for i in range(number1, number2 +1, 2):
        result = i
        print('Even numbers between', number1, 'and', number2, 'are:', result)
