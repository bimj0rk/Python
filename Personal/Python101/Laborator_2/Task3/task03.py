def task(register):
    '''
    register -> dictionar
    return -> lista doar cu numele studentilor
    '''
    names = []

    ################### TO DO #########################
    check_grade = lambda x : 1 if sum(x.values())/len(x.values()) >= 8.5 else 0

    for i in register:
        if(check_grade(register.get(i))):
            print(i)
            names.append(register.get(i))
    ###################################################
    
    return names
