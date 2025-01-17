ciphertext = input("Enter a message to decrypt (ciphertext): ")

listed_ciphertext = list(ciphertext)
length = len(listed_ciphertext)

decrypted = []

keys = []
pointer = []
x=[]

def get_divisors(lenght):
    divisors = []
    for i in range(1, length + 1):
        if length % i == 0:
            divisors.append(i)
    return divisors

print(f"Divisors of {length}: {get_divisors(length)}")
