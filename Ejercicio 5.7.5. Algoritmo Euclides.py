#Algorithm Euclides
#Inputs: n: integer
#        m: integer
#Output: integer
#Constants:
#Variables: r: integer
#Start
#while n > 0 do:
#   r <-- m mod n
#   if r = 0 do:
#       return n
#   m <-- n
#   n <-- r
#return 1
#End

n = input('Please enter the first number:')
n = int(n)
m = input('Please enter the second number:')
m = int(m)

result = 1
while n > 0:
    r = m % n
    if r == 0:
        result = n
        break
    m = n
    n = r
print('The greatest common divisor is', result)
