##Algorithm sort_array
##Inputs: numbers: array
##Output: array
##Constants:
##Variables: i: integer
##	     j: integer
##	     size: integer
##	     result: integer
##	     temp: real
##Start
##size ← number of element of the array
##for each value i from 0 to size-1 do: 
##for each value j from 0 to size-1-i do: 
##if numbers [j] > numbers [j+1] then:
##temp ← numbers [j]
##numbers [j] ← numbers [j+1] 
##numbers [j+1] ← temp
##	return numbers
##End


numbers = [5, 8, 9, 2]

size = len(numbers)

for i in range(0, size-1):
    for j in range(0, size-1-i):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
print(numbers)
