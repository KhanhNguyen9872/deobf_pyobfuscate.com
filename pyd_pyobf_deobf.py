#!/bin/python3
__import__('sys').setrecursionlimit(1000000000) 

# obfuscate variable
# pyobfuscate = ()  # replace pyobfuscate var
# or
# httpspyobfuscatecom

### DEOBFUSCATE
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad
import hashlib
from base64 import b85decode as b85
try:

    def d(b, p):
        c = b85(b.encode('utf-8'))
        r = AES.new(PBKDF2(p, c[:16], dkLen=32, count=1000000), AES.MODE_GCM, nonce=c[16:32])
        return r.decrypt_and_verify(c[48:], c[32:48]).decode('utf-8')
    print(d(pyc + pye, httpspyobfuscatecom))
except:

    def a(i):
        return unpad(AES.new(hashlib.sha256(str(list(pyobfuscate)[0][0] + list(pyobfuscate)[1][0][:-1]).encode()).digest()[:24], AES.MODE_CBC, i[:AES.block_size]).decrypt(i[AES.block_size:]), AES.block_size).decode()
    print(a(pyobfuscate[1][2]))