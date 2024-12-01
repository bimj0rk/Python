# Functie care returneaza un dictionar cu cuvintele valide si punctajele lor, impreuna cu o lista de tupluri care contine cuvintele cu cel mai mare punctaj si punctajul acestora.
def scrabble_words(letters, words):
    valid_words = {}
    max_score_words = []

    letter_scores = {
        'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10
    }

    for word in words:
        test = letters.copy()
        is_valid = True
        for letter in word:
            if letter in test:
                test.remove(letter)
            else:
                is_valid = False
                break
        
        if is_valid:
            valid_words[word] = sum([letter_scores[letter] for letter in word])

    
    if valid_words:
        max_score = max(valid_words.values())
        max_score_words = [[word, score] for word, score in valid_words.items() if score == max_score]  

    # Write code here
    return valid_words, max_score_words

if __name__ == '__main__':
    letters = input().strip().split()
    words = input().strip().split()
    valid_words, max_score_words = scrabble_words(letters, words)
    print("Cuvintele valide si punctajele lor:")
    print(valid_words)
    print("\nCuvintele cu cel mai mare punctaj:")
    print(max_score_words)