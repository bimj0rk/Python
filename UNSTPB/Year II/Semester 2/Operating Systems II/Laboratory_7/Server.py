import socket
import threading
import time
exit_flag = True

def caesarEncrypt(message, shift){
    encryptedMessage = ""
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            encryptedMessage += " "
        elif char.isupper():
            encryptedMessage += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            encryptedMessage += chr((ord(char) + shift - 97) % 26 + 97)
    return encryptedMessage
}

def connect(conn):
    global flag
    while flag:
        received = conn.recv(1024)
        if not received.decode():
            break
        if received == ' ':
            pass
        elif received == "exit":
            break
        else:
            print("Client>>>   " + received.decode())
    flag = False


def sendMsg(conn):
    while flag:
        sendMsg = input().encode('utf-8')
        sendMsg = caesarEncrypt(sendMsg, 3)
        if sendMsg == ' ':
            pass
        else:
            conn.sendall(sendMsg)


def main():
    flag = True
    startTime = time.monotonic()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 11111))
    s.listen()
    (conn, addr) = s.accept()
    thread1 = threading.Thread(target=connect, args=([conn]))
    thread2 = threading.Thread(target=sendMsg, args=([conn]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()
