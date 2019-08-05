print("This is a program to implement additive cipher\n")
plaintext = input("Please enter the message text\n")
plaintext = plaintext.lower()
key = int(input("Please enter the key to convert to ciphertext\n"))
ciphertext = ''
for i in range(len(plaintext)):
    ciphertext += chr((ord(plaintext[i]) - 97 + key) % 26 + 97)
print(ciphertext)
_ = input("Press any key to decrypt\n")
decrypted = ''
for i in range(len(plaintext)):
    decrypted += chr((ord(ciphertext[i]) - 97 - key) % 26 + 97)
print('Decrypted message', decrypted)
if decrypted == plaintext:
    print("Decryption succesfull")