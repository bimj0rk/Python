def verify_translation(cuvant, traducere):
    vocale_pasareasca = {
        'a': 'apa',
        'e': 'epe',
        'i': 'ipi',
        'o': 'opo',
        'u': 'upu'
    }
    
    traducere_buna = ""
    
    for letter in cuvant:
        if letter in vocale_pasareasca:
            traducere_buna += vocale_pasareasca[letter]
        else:
            traducere_buna += letter
    
    if traducere_buna == traducere:
        return True
    else:
        return False

if __name__ == "__main__":
    
    cuvant = input()
    traducere = input()
    
    print(verify_translation(cuvant, traducere))
