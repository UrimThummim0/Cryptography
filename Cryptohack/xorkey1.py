"""
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!


0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
"""
# Given ciphertext
ciphertext = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
known_plaintext = b"crypto{"

list_ = list(known_plaintext)
list__ = list(ciphertext)

#shift the key until crypto{ is found
for i in range(len(known_plaintext)):
    list__[i] = list__[i] ^ list_[i]   

key = (bytes(list__).decode())
print(key)


