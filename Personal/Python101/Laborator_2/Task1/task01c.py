def task1c(words):
    '''
    words -> lista string-uri
    return -> lista string-uri

    Salvati cuvintele care sunt palindrom in "palindromes"
    '''

    palindromes = []

    ################### TO DO #########################
    
    palindrome = lambda x : x == "".join(reversed(x))
    
    palindromes = filter(palindrome, words)

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(palindromes)
