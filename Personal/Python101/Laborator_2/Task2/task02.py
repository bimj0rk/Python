def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista cu elementele corespunzatoare
    '''

    result = []

    ################### TO DO #########################
    lower = lambda x : 1 if x == x.lower() else 0
    not_vowel = lambda x : 1 if x not in "aeiou" else 0
    not_word = lambda x : 1 if len(x) == 1 else 0
    not_symbol = lambda x : 1 if x in "abcdefghijklmnopqrstuvwxyz" else 0

    string_verificare = lambda x : 1 if type(x) is str and lower(x) and not_vowel(x) and not_word(x) and not_symbol(x) else 0

    for i in args:
        if(type(i) is int or string_verificare(i)):
            result.append(i)
    ###################################################
    return result
