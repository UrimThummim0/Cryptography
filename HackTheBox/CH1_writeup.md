# Writeup: Decrypting a Cipher

## Overview
The provided Python code demonstrates a method for decrypting a ciphered text using a brute force approach. It consists of two main functions:

1. `decrypt(ciphertext, key)` - A function that performs decryption based on a mathematical pattern determined by a given key.
2. `brute_force_decrypt(ciphertext)` - A function that iteratively tries various keys to decrypt the ciphertext, aiming to identify the correct decryption key and result.

The input is expected as a ciphertext string, and the output is the potential plaintext for a range of keys.

---

## Code Breakdown

### 1. **`decrypt(ciphertext, key)` Function**
This function is the core of the decryption logic. It reconstructs the plaintext by selecting characters from the ciphertext based on an index pattern derived from the key.

#### Implementation Details
- **Input:**
  - `ciphertext`: A string representing the encrypted message.
  - `key`: An integer used to calculate character indices.

- **Logic:**
  - The formula `(key + 1) * (n - 1) - key` calculates the index of the character to extract for each position `n` in the plaintext.
  - The function ensures indices are valid (`1 <= ... <= len(ciphertext)`).

- **Output:**
  - Returns the reconstructed plaintext for the provided key.

#### Code Example:
```python
def decrypt(ciphertext, key):
    return ''.join(ciphertext[(key + 1) * (n - 1) - key - 1]
                   for n in range(1, len(ciphertext) + 1)
                   if 1 <= (key + 1) * (n - 1) - key <= len(ciphertext))
```

### 2. **`brute_force_decrypt(ciphertext)` Function**
This function attempts decryption using multiple keys, aiming to identify the correct one.

#### Implementation Details
- **Input:**
  - `ciphertext`: A string representing the encrypted message.

- **Logic:**
  - Iterates through potential keys within a defined range (`1 to 10` by default).
  - Calls the `decrypt` function for each key and prints the result.

- **Output:**
  - Displays the decryption attempt for each key.

#### Code Example:
```python
def brute_force_decrypt(ciphertext):
    for key in range(1, 11):  # Adjust range as needed
        print(f"Key={key}: {decrypt(ciphertext, key)}")
```

### User Interaction
The script prompts the user to input a ciphertext string and then applies `brute_force_decrypt` to print possible plaintext outputs for keys in the range 1 to 10.

#### Example Usage:
```text
Enter a message to decrypt (ciphertext): encryptedmessage
Key=1: attempt1
Key=2: attempt2
...
Key=10: attempt10
```

---

## Limitations
1. **Key Range:**
   - The key range is hardcoded to `1-10`. If the valid key lies outside this range, it will not be found.
   - Adjust the range as needed by modifying the loop in `brute_force_decrypt`.

2. **Cipher Assumptions:**
   - The decryption formula assumes a specific encryption pattern. If the ciphertext does not follow this pattern, the output will be meaningless.

3. **No Validation:**
   - There is no mechanism to identify the correct plaintext automatically. It requires manual interpretation of the outputs.

