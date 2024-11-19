def is_sorted_tuple(my_tuple):
    '''Checks wheter a given tuple is sorted or not in ascending order

    my_tuple(tuple): a sequence of elements
    
    Output(boolean): True whe all the elements in the tuple are sorted in ascending order
    '''
    i = 1
    while i < len(my_tuple):
        if my_tuple[i] < my_tuple[i-1]:
            return False
        i += 1
    return True
