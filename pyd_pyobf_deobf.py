#!/bin/python3
__import__('sys').setrecursionlimit(1000000000) 

# obfuscate variable
# pyobfuscate = ()  # replace pyobfuscate var
# or
# obfuscate = ""

### DEOBFUSCATE
import hashlib
from base64 import b85decode as b85
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
try:
    if not 'exec' == pyobfuscate[0][1]:
        print('Try Another Method :)')
        input('Press Enter to Exit')
        exit()
    try:
        try:
            def a(i):
                return unpad(AES.new(hashlib.sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0]).encode()).digest()[:24], AES.MODE_CBC, i[:AES.block_size]).decrypt(i[AES.block_size:]), AES.block_size).decode()
            print(a(pyobfuscate[1][2]))
        except:
            def a(i):
                return unpad(AES.new(hashlib.sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0][:-1]).encode()).digest()[:24], AES.MODE_CBC, i[:AES.block_size]).decrypt(i[AES.block_size:]), AES.block_size).decode()
            print(a(pyobfuscate[1][2]))
    except ValueError as e:
        print(e)
        input('Press Enter to Exit')
        exit()
except:
    def a(i, j):
        i = b85(i)
        j, c = b(j, i[:8])
        return AES.new(j, AES.MODE_CFB, c).decrypt(i[8:]).decode()

    def b(i, j):
        k = hashlib.pbkdf2_hmac('sha256', i.encode(), j, 100000)
        return (k[:16], k[16:])
    print(a(list(obfuscate.values())[0], list(obfuscate.keys())[0][1:-1]))