print('Keyed transposition cipher')
plaintext = input('Enter message:')
key = list(map(int, input('Enter key array of length 5:').split()))
n = len(plaintext)
plaintext += 'x'*(5-n%5)
n = len(plaintext)
print('\nEncrypting...')
encrypted = ''
for i in range(n):
    batch = i//5
    encrypted += plaintext[batch*5 + key[i%5]]
print('Encrypted:', encrypted)

print('\nDecrypting...')
decrypted = ''
n = len(encrypted)
for i in range(n):
    batch = i//5
    decrypted += encrypted[batch*5 + key.index(i%5)]
print(decrypted)