def func(note, nume_materie):
    """
    Trebuie sa creati un tuplu cu numele "pereche",
    in care veti tine, astfel, (media notelor, numele_materiei)
    exemplu: pereche = (...)
    """
    suma = 0

    ################### TO DO #########################
    
    for i in range (len(note)):
        suma += note[i]

    medie = suma/len(note)

    pereche = (medie, nume_materie)

    ###################################################

    return pereche
