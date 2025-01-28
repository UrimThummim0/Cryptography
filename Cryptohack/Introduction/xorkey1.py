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

# Given data
ciphertext = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
xor_key = b"myXORkey"  # The key

# Repeat the key to match the length of the ciphertext
full_key = (xor_key * (len(ciphertext) // len(xor_key) + 1))[:len(ciphertext)]

# Decrypt the ciphertext
plaintext = bytes([c ^ k for c, k in zip(ciphertext, full_key)])

# Decode and print the flag
print(plaintext.decode())

