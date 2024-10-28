def task(register):
    '''
    register -> dictionar
    return -> lista doar cu numele studentilor
    '''
    names = []

    ################### TO DO #########################
    check_grade = lambda grades : 1 if sum(grades)/len(grades) >= 8.5 else 0

    for st_names, grades in register.items():
        if(check_grade(grades)):
            names.append(st_names)
    ###################################################
    
    return names
