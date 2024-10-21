def task1a(nums):
    '''
    nums -> vector int
    return -> vector int

    Dublati elementele care se divid cu 6, iar pe cele 
    care nu se divid, triplati-le folosind functionale
    '''

    result = []

    ################### TO DO #########################
    divide = lambda x : x % 6 == 0
    double = lambda x : x * 2
    triple = lambda x : x * 3
    
    y = lambda x : double(x) if divide(x) else triple(x)
    
    result = map(y, nums)
    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(result)
