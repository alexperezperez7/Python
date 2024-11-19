a = 3
b = 7
c = 2
d = 1
e = 8
f = 4

determinate = a*e - b*d

if determinate == 0:
    print('The system have not solution unique')
else:
    x = (c*e - b*f)/determinate
    y = (a*f - c*d)/determinate
    print('x:', x, 'y:', y)
