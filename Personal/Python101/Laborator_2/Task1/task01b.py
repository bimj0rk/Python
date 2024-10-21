def task1b(phrase):
    '''
    phrase -> string
    return -> string

    Transformati in litere mari vocalele din fraza
    si salvati rezultatul in "new_phrase"
    '''

    new_phrase = ""

    ################### TO DO #########################
    e_vocala = lambda x : x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'
    upper = lambda x : x.upper()
    
    y = lambda x : x if not e_vocala(x) else upper(x) 
    new_phrase = map(y, phrase)
    ###################################################

    # Nu modificati valoarea de retur a functiei
    return ''.join(list(new_phrase))
