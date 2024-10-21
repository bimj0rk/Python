def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista cu elementele corespunzatoare
    '''

    result = []

    ################### TO DO #########################
    lower = lambda x : 1 if "" == x.lower() else 0
    not_vowel = lambda x : 1 if x not in "aeiou" else 0

    for i in args:
        if(type(i) is int or (type(i) is str and lower(i) and not_vowel(i))):
            result.append(i)
    ###################################################
    return result
