##Algorithm calculate_total_cost_of_pencils
##Inputs: number_units: integer
##Output: real
##Constants:THRESHOLD = 1000
##	     CHEAP_PRICE = 0.85
##	     NORMAL_PRICE = 0.90
##Variables: result: real
##Start
##	if number_units >= THRESHOLD do:
##		result ← number_units * CHEAP_PRICE
##	else:
##		result ← number_units * NORMAL_PRICE
##	return result
##End


number_units = input('Enter a number of units:')
number_units = int(number_units)

THRESHOLD = 1000
CHEAP_PRICE = 0.85
NORMAL_PRICE = 0.90

if number_units >= THRESHOLD:
    result = number_units * CHEAP_PRICE
else:
    result = number_units * NORMAL_PRICE
print('The total cost is:', result)
