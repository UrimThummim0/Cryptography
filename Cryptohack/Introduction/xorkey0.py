"""
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
"""

import base64

ciphertext = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

bytes_string = bytes.fromhex(ciphertext)
print(bytes_string)

for i in range(256):
    plaintext = bytes(a ^ i for a in bytes_string)
    if b"crypto" in plaintext:
        print(i, plaintext)
    else:
        continue