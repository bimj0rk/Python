
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

    alfabet = {}

    for i in range(65, 90):
        alfabet[chr(i)] = ord(chr(i)) - 64

    alfabet[" "] = 0

    for i in range(len(string_message)):
        encoded_message[i] = string_message[i].key

    ###################################################

    return encoded_message