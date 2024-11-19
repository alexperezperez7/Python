import math

a = 1
b = -3
c = 4

##Primero calculamos el discriminante que es la parte que está dentro de la raíz cuadrada.
discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + sqrt(discriminant)) / (2*a)
    x2 = (-b - sqrt(discriminant)) / (2*a)
    print('The solutions are:', x1, 'and', x2)
if discriminant == 0:
    x = -b / (2*a)
    print('There is a double solution: x = ', x)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(- discriminant) / (2*a)
    x1 = real_part + imaginary_part
    x2 = real_part - imaginary_part
    print('The complex solutions are:', x1, 'and', x2)
    
