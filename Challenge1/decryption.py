"""
------------------------------------------------------------------------------------------------------------------------------------
This is a decryption function that takes in a ciphertext and a key. 
It applies a specific formula to reorder the characters in the ciphertext based on the key, and returns the decrypted text.
Specifically, the formula (key + 1) * (n - 1) - key is used to determine the new position of each character in the ciphertext,
where n is the original position of the character. The function then reorders the characters accordingly and returns the resulting
decrypted text.
------------------------------------------------------------------------------------------------UrimThummim0------------------------
"""
#YFwoJeELOvlDVrOlNBDConouLwhdCC mkIjsYeKsuaGsDbSRJymLJVOaYNQRrgKBSifPOdnCbUleWCbf

retrieved_plaintext = []
decaled_numbers = []
filtered_retrieved_plaintext = []

def decrypt(ciphertext, key):
    """
    Decodes a given ciphertext using a given key.

    The decryption formula is: (key + 1) * (n - 1) - key, where n is the nth character in the ciphertext.
    The decrypted plaintext is then given by the nth character in the ciphertext, where n is the result of the formula,
    unless the result is out of range, in which case the nth character is discarded.

    Args:
        ciphertext (str): The ciphertext to be decrypted.
        key (int): The key to use for decryption.

    Returns:
        str: The decrypted plaintext.
    """
    global retrieved_plaintext, decaled_numbers, filtered_retrieved_plaintext
    retrieved_plaintext = []
    decaled_numbers = []
    filtered_retrieved_plaintext = []
    
    n = 0
    for char in ciphertext:
        n += 1
        formula = (key + 1) * (n - 1) - key
        retrieved_plaintext.append(char)
        if 1 <= formula <= len(ciphertext):
            decaled_numbers.append(formula)
    for i in range(len(decaled_numbers)):
        filtered_retrieved_plaintext.append(retrieved_plaintext[decaled_numbers[i] - 1])

    decrypted_plaintext = ''.join(filtered_retrieved_plaintext)
    return decrypted_plaintext

# Brute-force to find possible keys
def brute_force_decrypt(ciphertext):
    for key in range(1, 11):  # Adjust range as needed
        decrypted_text = decrypt(ciphertext, key)
        print(f"Key={key}: {decrypted_text}")

# Input ciphertext
ciphertext = input("Enter a message to decrypt (ciphertext): ")
possible_decryptions = brute_force_decrypt(ciphertext)
print("Possible decryption:", possible_decryptions)