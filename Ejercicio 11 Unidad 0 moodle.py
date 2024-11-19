#Fib(n) = fib(n-1) + fib(n-2)
#Algorithm Fibonacci
#Inputs: number: integer
#Output: integer
#Constants:
#Variables: result: integer
#           i: integer
#           last1 (fibonacci una posición antes): integer
#	    last2 (fibonacci dos posiciones antes): integer
#Start
#last1 ← 1
#last2 ← 0
#if number = 0 do:
#    return last2
#if number = 1 do:
#    return last1
#for each value i between 2 and number do:
#    result ← last1 + last2
#    last2 ← last1
#    last1 ← result
#return result 
#End

number = 2
last1 = 1
last2 = 0
if number == 0:
    print('Fibonacci is', last2)
if number == 1:
    print('Fibonacci is', last1)
for i in range(2, number):
    result = last1 + last2
    last2 = last1
    last1 = result
print('Fibonnaci is', result)
