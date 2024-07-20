key = "vigenereciphersareprettycool"
plaintext = ""

table = [
    "abcdefghijklmnopqrstuvwxyz",
    "bcdefghijklmnopqrstuvwxyza",
    "cdefghijklmnopqrstuvwxyzab",
    "defghijklmnopqrstuvwxyzabc",
    "efghijklmnopqrstuvwxyzabcd",
    "fghijklmnopqrstuvwxyzabcde",
    "ghijklmnopqrstuvwxyzabcdef",
    "hijklmnopqrstuvwxyzabcdefg",
    "ijklmnopqrstuvwxyzabcdefgh",
    "jklmnopqrstuvwxyzabcdefghi",
    "klmnopqrstuvwxyzabcdefghij",
    "lmnopqrstuvwxyzabcdefghijk",
    "mnopqrstuvwxyzabcdefghijkl",
    "nopqrstuvwxyzabcdefghijklm",
    "opqrstuvwxyzabcdefghijklmn",
    "pqrstuvwxyzabcdefghijklmno",
    "qrstuvwxyzabcdefghijklmnop", 
    "rstuvwxyzabcdefghijklmnopq", 
    "stuvwxyzabcdefghijklmnopqr", 
    "tuvwxyzabcdefghijklmnopqrs", 
    "uvwxyzabcdefghijklmnopqrst", 
    "vwxyzabcdefghijklmnopqrstu", 
    "wxyzabcdefghijklmnopqrstuv", 
    "xyzabcdefghijklmnopqrstuvw",
    "yzabcdefghijklmnopqrstuvwx",
    "zabcdefghijklmnopqrstuvwxy",
]


#repeat the key for as many characters as are in the plaintext
def generate_full_key(plaintext, key):
    if len(plaintext) <= len(key):
        return key[:len(plaintext)]
    else:
        while len(key) < len(plaintext):
            key += key
        return key[:len(plaintext)]

# Encryption function
def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        col = table[ord(key[i])-97]  
        row = col[ord(plaintext[i])-97]
        ciphertext+=row
    return ciphertext

# Decryption Function
def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        row = table.index(table[ord(key[i])-97])
        for j in range(0,26):
            if table[j][row] == ciphertext[i]:
                plaintext+=chr(j+97)
                break
    return plaintext

plaintext = input("Enter plaintext: ")
plaintext = plaintext.lower()
plaintext = plaintext.replace(" ", "")

key = generate_full_key(plaintext, key)

ciphertext = encrypt(plaintext,key)
print("Ciphertext = ", ciphertext)

print("Plaintext decrypted from ciphertext = ", decrypt(ciphertext,key))