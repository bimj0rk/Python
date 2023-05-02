def scytaleEncrypt(message, key):
    message += ' ' * (len(message) % key)
    noColumns = len(message) // key

    encryptedMessage = ''
    for col in range(noColumns):
        for row in range(key):
            encryptedMessage += message[row * noColumns + col]

    return encryptedMessage

def scytaleDecrypt(message, key):
    noColumns = len(message) // key
    decryptedMessage = ''
    for row in range(key):
        for col in range(noColumns):
            decryptedMessage += message[row + col * key]

    decryptedMessage = decryptedMessage.rstrip()

    return decryptedMessage

def main():
    message = input('Enter the message: ')
    key = int(input('Enter the key: '))

    encryptedMessage = scytaleEncrypt(message, key)
    print('Encrypted message: ' + encryptedMessage)

    decryptedMessage = scytaleDecrypt(encryptedMessage, key)
    print('Decrypted message: ' + decryptedMessage)

if __name__ == '__main__':
    main()