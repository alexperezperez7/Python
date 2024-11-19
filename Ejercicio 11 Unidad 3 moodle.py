size = input('Enter the size of the square:')
size = int(size)

if size <= 0:
    print('The size must be more bigger.')
else:
    for i in range(size):
        print("*" * size)
