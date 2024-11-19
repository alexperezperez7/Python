##BMI = peso / altura^2
##
##Algorithm BMI
##Inputs: weight: real
##Output: real
##Constants:
##Variables: result: real
##	     height: real
##Start
##	result ← weight / pow(height,2)
##	return result
##End

weight = input('Enter your weight:')
weight = float(weight)
height = input('Enter your height:')
height = float(height)

result = weight/(height**2)
print('Your BMI is:', result)
