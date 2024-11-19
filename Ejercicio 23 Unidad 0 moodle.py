##media = suma de los números / n
##Algorithm average
##Inputs: numbers: array [integer]
##Output: real
##Constants:
##Variables: i: integer
##	     size: integer
##	     result: real
##Start
##	result ← 0 //Al resultado le damos valor 0 porque es una sumatoria, vamos a sumar
##	size ← number of element of the array
##	for each value i between 1 and size do:
##		result ← result + numbers [i]
##		//En el for no hay que incrementar i + 1, ya lo hace el each value
##	return result / size
##End

numbers = [5, 8, 3, 6]

result = 0
sum = sum(numbers)
size = len(numbers)

average = sum / size

print('The average is:', average)
