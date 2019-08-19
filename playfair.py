#A rudimentary and simple implementation of playfair cipher
cipher_matrix = [['l', 'q', 'u', 'x', 'z'],
['g', 'm', 'r', 'v', 'y'],
['d', 'h', 'n', 's', 'w'],
['b', 'e', 'i', 'j', 'o', 't'],
['a', 'c', 'f', 'k', 'p']]
bogus = ['x', 'y', 'z']
print('This is a program to implement playfair cipher')
plaintext = input('Please enter the message text')
plaintext = plaintext.lower()
#will treat for the last pair outside the loop
for i in range(len(plaintext) - 2):
    if plaintext[i] == plaintext[i+1]:
        if plaintext[i] != bogus[0] and plaintext[i+2] != bogus[0]:
            plaintext = plaintext[0:i] + bogus[0] + plaintext[i+1:]
        elif plaintext[i] != bogus[1] and plaintext[i+2] != bogus[1]:
            plaintext = plaintext[0:i] + bogus[1] + plaintext[i+1:]
        elif plaintext[i] != bogus[2] and plaintext[i+2] != bogus[2]:
            plaintext = plaintext[0:i] + bogus[2] + plaintext[i+1:]
#treating for last pair
i += 1
if plaintext[i] == plaintext[i+1]:
    if plaintext[i] != bogus[0]:
        plaintext = plaintext[:i] + bogus[0] + plaintext[i+1]
    elif plaintext[i] != bogus[1]:
        plaintext = plaintext[:i] + bogus[1] + plaintext[i+1]
i += 1
if len(plaintext)%2 != 0:
    if plaintext[i] != bogus[0]:
        plaintext = plaintext + bogus[0]
    elif plaintext[i] != bogus[1]:
        plaintext = plaintext + bogus[1]
print('preprocessed plaintext:', plaintext)
#preprocessing is done
#now getting to cipher
plaintext = list(plaintext)
ciphertext = plaintext
i = 0
first_char = [0, 0]
second_char = [0, 0]
while i<len(plaintext)-1:
    for j in range(5):
        if plaintext[i] in cipher_matrix[j]:
            first_char = [j, cipher_matrix[j].index(plaintext[i])]
        if plaintext[i+1] in cipher_matrix[j]:
            second_char = [j, cipher_matrix[j].index(plaintext[i+1])]
    #Same row
    print(first_char)
    print(second_char)
    if first_char[0] == second_char[0] and first_char[0] !=3:

        ciphertext[i] = cipher_matrix[first_char[0]][(first_char[1]+1)%5]
        ciphertext[i+1] = cipher_matrix[first_char[0]][(second_char[1]+1)%5]
    elif first_char[0] == second_char[0] and first_char[0] ==3:
        ciphertext[i] = cipher_matrix[first_char[0]][(first_char[1]+1)%6]
        ciphertext[i+1] = cipher_matrix[first_char[0]][(second_char[1]+1)%6]
    #Same column
    elif first_char[1] == second_char[1]:
        ciphertext[i] = cipher_matrix[(first_char[0]+1)%5][first_char[1]]
        ciphertext[i+1] = cipher_matrix[(second_char[0]+1)%5][first_char[1]]
    #Not same column and not same row
    else:
        #have to treat for 6th column differently
        if first_char[1] != 5 or second_char[1] != 5:
            ciphertext[i] = cipher_matrix[first_char[0]][second_char[1]]
            ciphertext[i+1] = cipher_matrix[second_char[0]][first_char[1]]
        #If either element is t, I'm not changing the elements

    i += 2
print('Ciphertext', ciphertext)
#Now to decrypt
decrypted = ciphertext
i = 0

c_first_char = [0, 0]
c_second_char = [0, 0]
while i<len(ciphertext)-1:
    for j in range(5):
        if plaintext[i] in cipher_matrix[j]:
            c_first_char = [j, cipher_matrix[j].index(plaintext[i])]
        if plaintext[i+1] in cipher_matrix[j]:
            c_second_char = [j, cipher_matrix[j].index(plaintext[i+1])]
    #Same row
    if c_first_char[0] == c_second_char[0] and c_first_char[0] !=3:
        decrypted[i] = cipher_matrix[c_first_char[0]][(c_first_char[1]-1)%5]
        decrypted[i+1] = cipher_matrix[c_first_char[0]][(c_second_char[1]-1)%5]
    elif c_first_char[0] == c_second_char[0] and c_first_char[0] ==3:
        decrypted[i] = cipher_matrix[c_first_char[0]][(c_first_char[1]-1)%6]
        decrypted[i+1] = cipher_matrix[c_first_char[0]][(c_second_char[1]-1)%6]
    #Same column
    elif first_char[1] == second_char[1]:
        decrypted[i] = cipher_matrix[(c_first_char[0]-1)%5][c_first_char[1]]
        decrypted[i+1] = cipher_matrix[(c_second_char[0]-1)%5][c_first_char[1]]
    #Not same column and not same row
    else:
        #have to treat for 6th column differently
        if first_char[1] != 5 or second_char[1] != 5:
            decrypted[i] = cipher_matrix[c_first_char[0]][c_second_char[1]]
            decrypted[i+1] = cipher_matrix[c_second_char[0]][c_first_char[1]]
        #If either element is t, I'm not changing the elements

    i += 2
print('Decrypted text', decrypted)