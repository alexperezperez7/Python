##Algortihm maximum
##Inputs: numbers: array [integer]
##Output: integer
##Constants:
##Variables: i: integer
##	     result: integer
##	     size: integer
##Start
##	result ← numbers [0] 
##El corchete indica la posición del elemento number, es decir en este caso cogería el número que se encuentra en la 1ª posición.
##	i ← 1
##	size ← number of elements of numbers
##while i < size do:
##	if result < numbers [i]
##		result ← numbers [i]
##	i ← i + 1
##	return result
##End


numbers = [3, 5, 8, 9, 2]

result = numbers[0]
i = 1
size = len(numbers)

while i < size:
    if result < numbers[i]:
        result = numbers[i]
    i += 1
print('The minimum number is:', result)
