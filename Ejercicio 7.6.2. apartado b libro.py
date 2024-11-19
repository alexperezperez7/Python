def dominó_string(string):
    '''Check if the files fit together

    string (str): String with the numbers
    
    Output (boolean): True if the files fit together and False if not
    '''
    file1, file2 = string.split()
    num1, num2 = map(int, file1.split('-'))
    num3, num4 = map(int, file2.split('-'))
    if num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4:
        return True
    else:
        return False
