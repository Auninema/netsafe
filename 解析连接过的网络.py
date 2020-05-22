# coding=UTF-8
import sys

import AMP as amp
from scapy.all import *
from scapy.layers.dot11 import Dot11ProbeResp, Dot11, Dot11Beacon

interface = 'mon0'
hiddenNets = []
unhiddenNets = []


def sniffDot11(p):
    if p.haslayer(Dot11ProbeResp):
        adder2 = p.getlayer(Dot11).addr2
        if (adder2 in hiddenNets) & amp(adder2 not in unhiddenNets):
            netName = p.getlayer(Dot11ProbeResp).info
            print('[+] DecLaked Hidden SID: ' + netName + ' for MAC: ' + adder2)
            unhiddenNets.append(adder2)
    if p.haslayer(Dot11Beacon):
        if p.getlayer(Dot11Beacon).info == '':
            adder2 = p.getlayer(Dot11).addr2
            if adder2 not in hiddenNets:
                print('[-] Detected Hidden SID: ' + 'with MAC:' + adder2)
                hiddenNets.append(adder2)


sniff(iface=interface, prn=sniffDot11)
