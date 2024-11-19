def vectorial_product(x1, y1, z1, x2, y2, z2):
    '''Calculate the vectorial product of two vectors.
    x1 (integer): first coordenate of first vector
    y1 (integer): second coordenate of first vector
    z1 (integer): third coordenate of first vector
    x2 (integer): first coordenate of second vector
    y2 (integer): second coordenate of second vector
    z2 (integer): third coordenate of second vector
    Output (integer), (integer), (integer): coordenates of result vector'''
    x3 = (y1 * z2) - (z1 * y2)
    y3 = (z1 * x2) - (x1 * z2)
    z3 = (x1 * y2) - (y1 * x2)
    return x3, y3, z3
