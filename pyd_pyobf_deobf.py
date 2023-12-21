#!/bin/python3

# obfuscate variable
obfuscate = ""


### DEOBFUSCATE
try:
    import random, base64, zlib, sys, string
    from Crypto.Cipher import AES, PKCS1_OAEP
    from Crypto.Hash import SHA256
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
    from Crypto.Signature import pkcs1_15
    from Crypto.Util.Padding import pad, unpad
    from Crypto.Cipher import AES
    import binascii

    class AESEncryption:

        def __init__(self, key: bytes) -> None:
            self.key = key

        @classmethod
        def from_nbits(cls, nbits: int=256):
            cls.iv = iv
            cls.key = keys
            cls.mode = mode
            return cls(keys)

        def encrypt(self, message: bytes) -> bytes:
            cipher = AES.new(self.key, self.mode, self.iv)
            ciphered_data = cipher.encrypt(pad(message, AES.block_size))
            return ciphered_data

        def decrypt(self, message: bytes) -> bytes:
            cipher = AES.new(self.key, self.mode, self.iv)
            decrypted_data = unpad(cipher.decrypt(message), AES.block_size)
            return decrypted_data
    MESSAGE_LONG = get_random_bytes(100100)
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    bb = _encrypt[125:]
    keys = base64.b85decode(bb)
    iv = _pubkey[100:]
    mode = AES.MODE_CBC
    aes = AESEncryption.from_nbits(256)
    encrypted_msg = aes.encrypt(_lambda)
    passkey2 = 'Obfuscated by https://pyobfuscate.com'
    if not _key == passkey2:
        print('Decryption Key Do not Match or Missing AES Salt 256')
        sys.exit()
    print(zlib.decompress(aes.decrypt(_lambda)).decode())
except:
    import base64, os, hashlib, random
    from Crypto.Cipher import AES

    def aes_decrypt(encrypted_data, key):
        encrypted_data = base64.b85decode(encrypted_data)
        salt = encrypted_data[:8]
        key, iv = derive_key_and_iv(key, salt)
        cipher = AES.new(key, AES.MODE_CFB, iv)
        data = cipher.decrypt(encrypted_data[8:])
        return data.decode()

    def derive_key_and_iv(password, salt):
        dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        key = dk[:16]
        iv = dk[16:]
        return (key, iv)
    print(aes_decrypt(list(obfuscate.values())[0], list(obfuscate.keys())[0][1:-1]))