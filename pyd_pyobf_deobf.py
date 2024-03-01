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
    IIIlIlllIIlIllIIII = pyobfuscate
    if not 'exec' == pyobfuscate[0][1]:
        IlIllIllIlIl('Try Another Method :)')
        input('Press Enter to Exit')
        exit()
    try:
        try:

            def IIlIIIIIllIlllIIII(IIllIlllIllIllIIlI):
                return unpad(AES.new(hashlib.sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0]).encode()).digest()[:24], AES.MODE_CBC, IIllIlllIllIllIIlI[:AES.block_size]).decrypt(IIllIlllIllIllIIlI[AES.block_size:]), AES.block_size).decode()
            print(IIlIIIIIllIlllIIII(pyobfuscate[1][2]))
        except:

            def IIlIIIIIllIlllIIII(IIllIlllIllIllIIlI):
                return unpad(AES.new(hashlib.sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0][:-1]).encode()).digest()[:24], AES.MODE_CBC, IIllIlllIllIllIIlI[:AES.block_size]).decrypt(IIllIlllIllIllIIlI[AES.block_size:]), AES.block_size).decode()
            print(IIlIIIIIllIlllIIII(pyobfuscate[1][2]))
    except ValueError as lllIIIlIllIIllIlII:
        IlIllIllIlIl(lllIIIlIllIIllIlII)
        input('Press Enter to Exit')
        exit()
except:
    IIIlIlllIIlIllIIII = obfuscate

    def lIIIIIIllIlIIlIlIl(IIllIlllIllIllIIlI, IlllIlllIIIIlIIIll):
        IIllIlllIllIllIIlI = b85(IIllIlllIllIllIIlI)
        IlllIlllIIIIlIIIll, IlIlllllllIIlIIlII = llIIIIllIIIllIllIl(IlllIlllIIIIlIIIll, IIllIlllIllIllIIlI[:8])
        return AES.new(IlllIlllIIIIlIIIll, AES.MODE_CFB, IlIlllllllIIlIIlII).decrypt(IIllIlllIllIllIIlI[8:]).decode()

    def llIIIIllIIIllIllIl(lIllIIlIlIlIlIlIll, IlIIlIIIIIIIlIIllI):
        IllIllIllIIllllllI = hashlib.pbkdf2_hmac('sha256', lIllIIlIlIlIlIlIll.encode(), IlIIlIIIIIIIlIIllI, 100000)
        return (IllIllIllIIllllllI[:16], IllIllIllIIllllllI[16:])
    print(lIIIIIIllIlIIlIlIl(list(obfuscate.values())[0], list(obfuscate.keys())[0][1:-1]))