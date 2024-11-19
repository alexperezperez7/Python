##Algorithm standard_deviation
##Inputs: numbers: array [integer]
##Output: real
##Constants:
##Variables: i: integer
##	     avg: real
##	     size: integer
##	     result: real
##Start
##	avg ← 0
##	result ← 0
##	size ← number of element of the array
##	for each value i between 1 and size do:
##		avg ← avg + numbers [i]
##	avg ← avg / size
##	for each value i between 1 and size do:
##		result ← result + pow (numbers [i] - avg,2)
##	result ← result / size
##	return sqrt (result)
##End


import math

numbers = [5, 8, 6, 2]

avg = 0
result = 0
size = len(numbers)

for i in range(1, size):
    avg = avg + numbers[i]
avg = avg / size
for i in range(1, size):
    result = result + (numbers[i] - avg)**2
result = result / size
print('The standard deviation is:', math.sqrt(result))
