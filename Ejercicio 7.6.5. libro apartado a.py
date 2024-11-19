def is_prime(elem):
    '''Check if the element is prime or not

    elem (integer): number integer

    Output (boolean): True if the number is prime and False if the number not is prime
    '''
    if elem < 2:
        return False
    for i in range(2, elem):
        if elem % i == 0:
            return False
        return True

def filter_primes(my_list):
    '''Extract a prime numbers from a given list

    my_list (list): a sequence of numbers integers

    Output (list): a sequence with prime numbers
    '''
    result = []
    for number in my_list:
        if is_prime(number):    #check wheter number is prime
            result.append(number)
    return result
