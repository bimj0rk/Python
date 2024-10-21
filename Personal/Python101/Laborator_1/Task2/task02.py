def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """

    nume_formatat = ()
    
    nume_familie = list()
    prenume_1 = list()
    prenume_2 = list()

    ################### TO DO #########################

    for nume in nume_complete:
        nume_familie_x = nume.split(" ")
        prenume = nume_familie_x[1].split("-")
        
        nume_familie.append(nume_familie_x[0])
        prenume_1.append(prenume[0])
        prenume_2.append(prenume[1])   
        
    nume_formatat = (nume_familie, prenume_1, prenume_2)
            
    ###################################################

    return nume_formatat

    