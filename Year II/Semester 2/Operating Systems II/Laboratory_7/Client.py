import sys
import socket
import threading
import time
from typing import re

def caesarDecrypt(message, shift):
    decryptedMessage = ""
    for i in range(len(message)):
        char = message[i]
        if char == " ":
            decryptedMessage += " "
        elif char.isupper():
            decryptedMessage += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decryptedMessage += chr((ord(char) - shift - 97) % 26 + 97)
    return decryptedMessage

def connect(s):
    while True:
        recievedMsg = s.recv(1024)
        if not recievedMsg:
            break
        if recievedMsg == '':
            break
        else:
            print("Server>>>  "+str(recievedMsg))
        if not flag:
            break

def receive(s):
    global flag
    while True:
        sentMsg = input().encode('utf-8')
        sentMsg = caesarDecrypt(sentMsg, 3)
        if sentMsg == '':
            pass
        if sentMsg.decode() == 'exit':
            print("wan exit")
            break
        else:
            s.sendall(sentMsg)
    flag = False


def main():
    startTime = time.monotonic()
    if 3 != len(sys.argv):
        print("usage: %s [ip adress][port] " % sys.argv[0])
        sys.exit(0)
    flag = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((sys.argv[1], int(sys.argv[2])))
    thread1 = threading.Thread(target=connect, args=([s]))
    thread2 = threading.Thread(target=receive, args=([s]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

if __name__ == '__main__':
    main()