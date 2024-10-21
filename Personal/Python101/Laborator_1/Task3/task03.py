
def func(string_message):
    """ 
    Puneti rezultatul codificarii mesajului in "encoded_message"

    HINT!
    chr() si ord() sunt functii implicite care "jongleaza" cu caracterele
    ASCII si codificarile lor. Astfel, daca pentru litera 'A', avem codificarea
    65, iar pentru 'B' avem 66, atunci:
    
    chr(65) = 'A'   ||   chr(66) = 'B'  
    ord('A') = 65   ||   ord('B') = 66

    ANOTHER HINT!
    Poti folosi dictionarele.
    """
    
    encoded_message = ""
    ################### TO DO #########################

    alfabet = {' ': 0}
    
    for i in range(65, 90):
        alfabet[chr(i)] = ord(chr(i)) - 64


    for i in string_message:
        n = str(alfabet[i])
        encoded_message += n
    
    ###################################################

    return encoded_message