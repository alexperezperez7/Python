n = input('Please enter a number')
n = int(n)
result = 0

for j in range(1, n+1):
    for i in range(1, j+1):
        result = result + j * i**2
print(result)
