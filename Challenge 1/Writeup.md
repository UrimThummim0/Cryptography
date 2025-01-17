### Writeup: Decrypt Function with Brute-Force Capability

#### Overview
This script implements a decryption algorithm that takes a ciphertext and a key as input. It uses a specific formula to rearrange the characters in the ciphertext and produce a decrypted plaintext. The script also includes a brute-force function to try multiple keys and identify possible decryptions when the key is unknown.

---

#### Function: `decrypt(ciphertext, key)`
**Purpose:**
To decrypt a given ciphertext using a mathematical formula that determines the reordering of characters based on their position and the provided key.

**Inputs:**
- `ciphertext` (str): The encrypted text to be decrypted.
- `key` (int): The numerical key used to guide the decryption process.

**Outputs:**
- Returns the decrypted plaintext as a string.

**Decryption Process:**
1. Initialize global variables:
   - `retrieved_plaintext`: Stores characters of the ciphertext in their original order.
   - `decaled_numbers`: Stores the positions calculated by the formula.
   - `filtered_retrieved_plaintext`: Stores the characters reordered based on `decaled_numbers`.

2. Iterate over each character in the ciphertext. For each character:
   - Calculate the new position using the formula:
     
     \[
     \text{formula} = (\text{key} + 1) \times (n - 1) - \text{key}
     \]
     
     Where \( n \) is the current position (1-based index) of the character in the ciphertext.
   - Append the character to `retrieved_plaintext`.
   - If the calculated position (`formula`) is within the range of the ciphertext, store it in `decaled_numbers`.

3. Using `decaled_numbers`, reorder the characters from `retrieved_plaintext` and store them in `filtered_retrieved_plaintext`.

4. Convert `filtered_retrieved_plaintext` into a single string and return it as the decrypted plaintext.

**Code Example:**
```python
def decrypt(ciphertext, key):
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
```

---

#### Function: `brute_force_decrypt(ciphertext)`
**Purpose:**
To attempt decryption of a ciphertext using a range of keys, outputting all possible results.

**Inputs:**
- `ciphertext` (str): The encrypted text to be decrypted.

**Outputs:**
- Prints the decrypted plaintext for each tested key.

**Brute-Force Process:**
1. Iterate through a range of potential keys (1 to 10 by default).
2. For each key, call the `decrypt` function and store or print the result.
3. Display all potential decryptions to the user.

**Code Example:**
```python
def brute_force_decrypt(ciphertext):
    for key in range(1, 11):  # Adjust range as needed
        decrypted_text = decrypt(ciphertext, key)
        print(f"Key={key}: {decrypted_text}")
```

---

#### Execution Flow
1. The user inputs a ciphertext to decrypt.
2. The `brute_force_decrypt` function attempts to decrypt the ciphertext using all possible keys in the specified range.
3. All decrypted texts corresponding to the tested keys are displayed, allowing the user to identify the correct plaintext visually.

**Example Execution:**
```plaintext
Enter a message to decrypt (ciphertext): YFwoJeELOvlDVrOlNBDConouLwhdCCmkIjsYeKsuaGsDbSRJymLJVOaYNQRrgKBSifPOdnCbUleWCbf
Key=1: ExampleOutput1
Key=2: ExampleOutput2
Key=3: ExampleOutput3
...
```

---

#### Key Points
1. The decryption formula calculates the reordered positions of the characters based on the key.
2. The brute-force function provides a simple yet effective way to recover plaintext when the key is unknown.
3. The script is flexible, allowing adjustments to the key range or validation criteria for plaintext.

#### Limitations
1. Without any criteria to validate the plaintext (e.g., known patterns or words), the correct decryption might not be immediately obvious.
2. For a large range of possible keys, the brute-force approach may become time-consuming.

---

#### Suggested Improvements
1. **Validation Function:** Incorporate a function to detect meaningful patterns in the decrypted text, such as checking for common words or character distributions.
2. **Dynamic Key Range:** Allow the user to specify the range of possible keys to reduce unnecessary computations.
3. **Error Handling:** Add checks to handle invalid inputs (e.g., non-string ciphertext or non-integer keys).

