def egcd(a, b, x, y, g):
    '''
    This is a utility function to calculate gcd because determinant and 26 need to be co-prime
    '''
    if a == 0:
        y = 1
        x = 0
        g = b
        return (a, b, x, y, g)
    
    a1, b1, x1, y1, g = egcd(b%a, a, 1, 1, 1)
    x = y1 - (b//a)*x1
    y = x1
    return (a, b, x, y, g)

def func_key_matrix():
    '''
    Utility function to take input key matrix
    '''
    key_matrix = []
    print('Please enter the rows of the key matrix\nThree comma separated numbers in a line')
    key_matrix.append(list(map(int, input('Enter the first row\n').split())))
    key_matrix.append(list(map(int, input('Enter the second row\n').split())))
    key_matrix.append(list(map(int, input('Enter the third row\n').split())))
    #initialising the co-factor matrix
    co_matrix = [ [0 for i in range(3)] for i in range(3) ]
    #Calculating the co-factor matrix
    for i in range(3):
        for j in range(3):
            co_matrix[i][j] = key_matrix[(i+1)%3][(j+1)%3]*key_matrix[(i+2)%3][(j+2)%3] - key_matrix[(i+1)%3][(j+2)%3]*key_matrix[(i+2)%3][(j+1)%3]
    #Calculating the determinant
    det = key_matrix[0][0]*co_matrix[0][0] + key_matrix[0][1]*co_matrix[0][1] + key_matrix[0][2]*co_matrix[0][2]
    print(det)
    #Getting the bezout coefficients
    bez_cof = egcd(det, 26, 1, 1, 1)
    #Calculating the Adjoint of the matrix which is the transpose of the co factor matrix
    co_matrix_t = [ [0 for i in range(3)] for i in range(3) ]
    for i in range(3):
        for j in range(3):
            co_matrix_t[i][j] = co_matrix[j][i]
    return key_matrix, det, co_matrix, co_matrix_t, bez_cof

#Hill Cipher using 3*3 matrix key matrix
def main():
    print('This is a program to implement hill cipher')
    plaintext = input('Please enter message text\n')
    plaintext = plaintext.lower()
    plain_len = len(plaintext)
    if plain_len%3 == 1:
        plaintext += 'xx'
        plain_len += 2
    if plain_len%3 ==2:
        plaintext += 'x'
        plain_len += 1
    #Getting the key matrix
    key_matrix, det, co_matrix, co_matrix_t, bez_cof = func_key_matrix()
    print('Key matrix', key_matrix,'\nDeterminant', det, '\nCo factor matrix', co_matrix, '\nAdjoint', co_matrix_t, '\nBezout equation coefficients', bez_cof)
    #Bezout coefficients
    while bez_cof[4] != 1 and bez_cof[4] != -1:
        print('Wrong inputs, Enter values such that the determinant and 26 can be co prime')
        key_matrix, det, co_matrix, co_matrix_t, bez_cof = func_key_matrix()
        print('Key matrix', key_matrix,'\nDeterminant', det, '\nCo factor matrix', co_matrix, '\nAdjoint', co_matrix_t, '\nBezout equation coefficients', bez_cof)

    #Getting the determinant's multiplicative inverse with 26
    key_inv = bez_cof[2]
    #When gcd is -1, we have to inverse the sign of bezout coefficient to get multiplicative inverse
    if bez_cof[4] == -1:
        key_inv = -key_inv
    ciphertext = []
    cipher_vector = [0]*3
    plain_vector = [0]*3
    plain_text = list(plaintext)
    
    #Starting the loop
    i = 0
    while i<plain_len:
        plain_vector[0] = ord(plain_text[i]) - 97
        plain_vector[1] = ord(plain_text[i+1]) - 97
        plain_vector[2] = ord(plain_text[i+2]) - 97
        for j in range(3):
            #For running product
            prod = 0
            for k in range(3):
                prod += key_matrix[j][k]*plain_vector[k]
            cipher_vector[j] = prod%26
        
        ciphertext.append(chr(cipher_vector[0] + 97))
        ciphertext.append(chr(cipher_vector[1] + 97))
        ciphertext.append(chr(cipher_vector[2] + 97))
        i += 3
    print('Ciphertext:', ''.join(ciphertext))
    print('Now to decrypt')
    decrypted = []
    decrypted_vector = [0]*3
    i =0
    while i<plain_len:
        cipher_vector[0] = ord(ciphertext[i]) - 97
        cipher_vector[1] = ord(ciphertext[i+1]) - 97
        cipher_vector[2] = ord(ciphertext[i+2]) - 97
        
        for j in range(3):
            prod = 0
            for k in range(3):
                prod += co_matrix_t[j][k]*cipher_vector[k]
            decrypted_vector[j] = (prod * key_inv)%26
        decrypted.append(chr(decrypted_vector[0] + 97))
        decrypted.append(chr(decrypted_vector[1] + 97))
        decrypted.append(chr(decrypted_vector[2] + 97))
        i += 3
    decrypted_string = ''.join(decrypted)
    print('Decrypted text:', decrypted_string)
    if decrypted_string == plaintext:
        print('Decryption successful')
if __name__ == '__main__':
    main()
