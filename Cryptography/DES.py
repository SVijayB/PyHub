import base32hex
import hashlib
from Cryptodome.Cipher import DES
from secrets import token_bytes

# install the above libraries using pip3 install <library name>
# pip3 install pycryptodome
# pip3 install base32hex

key = token_bytes(8)

h=b'T&Z\xa33\x16\x99\xfb'

def encrypt(msg):
    cipher = DES.new(h, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(h, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt(input('Enter a message: '))

plaintext = decrypt(nonce, ciphertext, tag)

print(f'Cipher text: {ciphertext}')

if not plaintext:
    print('Message is corrupted!')
else:
    print(f'Plain text: {plaintext}')
