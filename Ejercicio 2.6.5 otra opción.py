lower_limit = input('Please enter the lower limit:')
lower_limit = int(lower_limit)
upper_limit = input('Please enter the upper limit:')
upper_limit = int(upper_limit)

i = lower_limit
print('Calculating even numbers between', lower_limit, 'and', upper_limit)
if i % 2 == 1:
    i += 1
while i <= upper_limit:
    print(i)
    i += 2

