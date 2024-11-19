#Algorithm gcd
#Inputs: a: integer
#         b: integer
#Output: integer
#Constants:
#Variables: i: integer
#             limit: integer
#Start
#    if a < b do:
#        limit <-- a
#    else:
#        limit <-- b
#    for each value i between limit and 2 do:
#        if (a mod i = 0 and b mod i = 0) do:
#            return i
#    return 1
#End

a = input('Enter the first number:')
a = int(a)
b = input('Enter the second number:')
b = int(b)

result = 1
limit = min(a,b)

for i in range(limit, 1, -1):
    if a%i == 0 and b%i == 0:
        result = i
        break
print('The greatest common divisor of', a, 'and', b, 'is', result)
