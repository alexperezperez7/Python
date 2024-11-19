#Algorithm gcd
#Inputs: a: integer
#         b: integer
#Output: integer
#Constants:
#Variables: i: integer
#             limit: integer
#             result: integer
#Start
#    result <-- 1
#    if a < b do:
#        limit <-- a
#    else:
#        limit <-- b
#    for each value i between 2 and limit do:
#        if (a mod i = 0 and b mod i = 0) do:
#            result <-- i
#    return result
#End

a = input('Enter the first number:')
a = int(a)
b = input('Enter the second number:')
b = int(b)

result = 1
limit = min(a,b)

for i in range(2, limit + 1):
    if a%i == 0 and b%i == 0:
        result = i
print('The great common divisors of', a, 'and', b, 'is', result)
