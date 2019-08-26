print('Rail Fence Cipher with 2 rows so as to make it keyless')
plaintext = input('Message text:')
n = len(plaintext)
encrypted = ''
for i in range(n):
	if n%2 == 0:
		if i<n//2:
			encrypted += plaintext[2*i]
		else:
			encrypted += plaintext[2*(i%(n//2))+1]
	else:
		if i<(n//2)+1:
			encrypted += plaintext[2*i]
		else:
			encrypted += plaintext[2*((i-1)%(n//2))+1]
print('Encrypted message:', encrypted)
'''matrix implementation for encryption
enc_mat = ['0']*n
temp = ['0']*n
enc_mat = [enc_mat, temp]
for i in range(n):
	enc_mat[i%2][i] = plaintext[i]
encrypted = ''
for i in range(n):
	if enc_mat[0][i] != '0':
		encrypted += enc_mat[0][i]
for i in range(n):
	if enc_mat[1][i] != '0':
		encrypted += enc_mat[1][i]
print('Encrypted message', encrypted)
'''

#Now to decrypt
n = len(encrypted)
decrypted = ''
pair = 0
for i in range(n):
	if n%2 == 0:
		if i%2 == 0:
			decrypted += encrypted[pair]
		else:
			decrypted += encrypted[(n//2)+pair]
			pair += 1
	else:
		if i%2 == 0:
			decrypted += encrypted[pair]
		else:
			decrypted += encrypted[((n//2)+1)+pair]
			pair += 1
print('Decrypted message', decrypted)
