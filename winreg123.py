# coding=UTF-8

import _winreg

def val2addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x "% ord(ch))
        addr = addr.strip(" ").replace(" ",":")[0:17]
    return addr

def printNets():
    net = "SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, net)
    print '\n[*] Networks You have Joined.'
    for i in range(100):
        try:
            guid = _winreg.EnumKey(key, i)
            netKey = _winreg.OpenKey(key, str(guid))
            (n, addr, t) = _winreg.EnumValue(netKey, 5)
            (n, name, t) = _winreg.EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print '[+] ' + netName + ' ' + macAddr
            _winreg.CloseKey(netKey)
        except:
            break

def main():
    printNets()
if __name__ == "__main__":
    main()