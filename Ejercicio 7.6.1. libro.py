def is_sorted_tuple(my_tuple):
    '''Checks wheter a given tuple is sorted or not in ascending order

    my_tuple(tuple): a sequence of elements
    
    Output(boolean): True whe all the elements in the tuple are sorted in ascending order
    '''
    previous = None
    for elem in my_tuple:
        if previous == None:
            previous = elem
        elif elem < previous:
            return False
        previous = elem
    return True
    
    
