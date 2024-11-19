def election_campaign_tuple(names):
    '''Print the message Dear <first name>, vote for me.

    names (tuple): Tuple with the name of candidates.

    Output: Print a message for each candidate
    '''
    for name in names:
        print('Dear', name, 'vote for me.')
