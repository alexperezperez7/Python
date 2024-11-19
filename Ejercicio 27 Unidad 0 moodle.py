##BMI = peso / altura^2
##
##Algorithm BMI
##Inputs: weight: real
##Output: string
##Constants:
##Variables: result: real
##	     height: real
##	     category: string
##Start
##	result ← weight / pow(height,2)
##	return result
##	if result < 18.5 do:
##		category ← “underweight”
##		return category
##	else if result >= 18.5 and result <= 24.9 do:
##		category ← “normal”
##		return category
##	else if result >= 25 and result <= 29.9 do:
##		category ← “overweight”
##		return category
##	else
##		category ← “obese”
##	return category
##End


weight = input('Enter your weight:')
weight = float(weight)
height = input('Enter your height:')
height = float(height)

result = weight / (height**2)
if result < 18.5:
    category = 'underweight'
    print('Your category is', category)
if result >= 18.5 and result <= 24.9:
    category = 'normal'
    print('Your category is', category)
if result >= 25 and result <= 29.9:
    category = 'overweight'
    print('Your category is', category)
if result >= 30:
    category = 'obese'
    print('Your category is', category)
