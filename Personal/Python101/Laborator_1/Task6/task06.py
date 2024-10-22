def func(size):

    romb = ""

    ################### TO DO #########################
    size = size + (1 - size % 2)
    spatiu = size // 2
    t = -1
    
    for i in range(size):
        romb += " " * spatiu # ca sa centreze
        romb += "@"
        spatiu = max(0, spatiu + t)
        
        if i < size // 2: #daca creste
            romb += "." * 2 * i
        else: #daca scade 
            romb += "." * 2 * (size - i - 1)
            t = 1
            if spatiu == 0:
                spatiu = 1
        romb += "@\n"
    ###################################################

    return romb