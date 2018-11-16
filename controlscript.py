#!/usr/bin/env python
from scapy.layers.inet import *

def PreceivePacket():
     rcvPkt=sniff(iface='ctr-wlan0')
     packet=rcvPkt.show()
     return packet




if __name__=='__main__':
    PreceivePacket()
