number1 = input('Enter the first number:')
number1 = int(number1)
number2 = input('Enter the second number:')
number2 = int(number2)

result_gcd = 1
limit = min(number1,number2)

for i in range(limit, 1, -1):
    if number1%i == 0 and number2%i == 0:
        result_gcd = i
        break

result_gcd = i
mcm = abs(number1 * number2) // result_gcd
print('The minimum common multiple is:', mcm)
