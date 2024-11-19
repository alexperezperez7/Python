def dominó_tuple(file1, file2):
    '''Check if the files fit together

    file1 (tuple): a tuple with two numbers integers
    file2 (tuple): a tuple with two number integers

    Output (boolean): True if the files fit together and False if not
    '''
    num1, num2 = file1
    num3, num4 = file2
    if num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4:
        return True
    else:
        return False
