##Como pasar un número de base 10 a base 2. Por ejemplo el número 17:
##17/2 = 8 y resto 1.
##Ahora el resultado lo dividimos entre 2:
##8/2 = 4 y resto 0
##Otra vez el resultado entre 2:
##4/2 = 2 y resto 0
##Otra vez:
##2/2 = 1 y resto 0
##
##El número 17 en binario sería: (El primer número es el último resultado de la última división y los demás restos del último al primero) 10001
##
##Algorithm binary_conversion
##Inputs: number: integer
##Output: text
##Constants:
##Variables: dividend: integer
##           remainder: integer
##           result: text
##
##Start
##	if number = 0 do:
##		return ‘0’
##	result ← ‘’ //Cadena de texto vacía
##	dividend ← number
##	while dividend > 1  do:
##		remainder ← dividend mod 2
##		dividend ← (integer) dividend / 2 
##El paréntesis indicando el tipo de dato hace que si el resultado es real, con decimales, que se quede solo con la parte entera.
##		result ← (text) remainder + result
##result ← ‘1’ + result //Este 1 es el del cociente de la última división
##return result		
##End


number = input('Enter a number:')
number = int(number)

if number == 0:
    print('The number in binary is', 0)
    
result = ''
dividend = number

while dividend > 1:
    remainder = dividend % 2
    dividend = int(dividend) // 2
    result = str(remainder) + result
result = '1' + result
print('The number in binary is', result)
