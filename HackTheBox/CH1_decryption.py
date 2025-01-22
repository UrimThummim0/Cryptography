def decrypt(ciphertext, key):
    return ''.join(ciphertext[(key + 1) * (n - 1) - key - 1] 
                   for n in range(1, len(ciphertext) + 1) 
                   if 1 <= (key + 1) * (n - 1) - key <= len(ciphertext))

def brute_force_decrypt(ciphertext):
    for key in range(1, 11):  # Adjust range as needed
        print(f"Key={key}: {decrypt(ciphertext, key)}")

# Input ciphertext
ciphertext = input("Enter a message to decrypt (ciphertext): ")
brute_force_decrypt(ciphertext)