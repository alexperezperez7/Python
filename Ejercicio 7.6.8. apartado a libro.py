def list_reverse(my_list):
    '''Reverts the given sequence of elements

    my_list (list): A sequence of elements

    Output (list)
    '''
    size = len(my_list) - 1
    for i in range(size):
        last_element = my_list.pop()
        my_list.insert(i, last_element)
    return my_list
