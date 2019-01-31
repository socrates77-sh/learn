import winreg


# def val2addr(val):
#     addr=''
#     for ch in val:
#         addr += ()

def printNets():
    net = '\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures\\Unmanaged'
    net = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\NetworkList\\Signatures'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)
    print(key)


def main():
    printNets()


if __name__ == '__main__':
    main()
