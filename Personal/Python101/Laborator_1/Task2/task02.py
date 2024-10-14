def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """

    nume_formatat = {}

    ################### TO DO #########################

    for i in range(len(nume_complete)):
        lista_nume = nume_complete[i].split(" ")
        lista_prenume = lista_nume[1].split("-")
        
        nume_formatat[0] = lista_nume[0]
        nume_formatat[1] = lista_prenume[0]
        nume_formatat[2] = lista_prenume[1]
            
    ###################################################

    return nume_formatat

    