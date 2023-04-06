import time

def cowsAndBulls(initialNumber: int, guessedNumber: int):
    cows: int = 0
    bulls: int = 0
    for i in range(len(str(initialNumber))):
        if str(initialNumber)[i] == str(guessedNumber)[i]:
            cows += 1
        else:
            bulls += 1
    return cows, bulls

def main():
    initialNumber = int(input("Enter the initial number: "))
    startTimer = time.time()
    guessedNumber = int(input("Enter the guessed number: "))
    stopTimer = time.time()
    cows: int
    bulls: int
    cows, bulls = cowsAndBulls(initialNumber, guessedNumber)
    print("Cows: ", cows)
    print("Bulls: ", bulls)
    print("It took you ", stopTimer - startTimer, " seconds to guess")

if __name__ == '__main__':
    main()