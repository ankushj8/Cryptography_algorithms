def egcd(a, b, x, y, g):
    '''
    egcd is short for extended greatest common divisor and is the extended euclidean algorithm to find the gcd and the numbers that satisfy the bezout theorem
    a*x + b*y = gcd
    '''
    #print('Numbers that gor receive by the function', a, b, x, y, g)
    if a == 0:
        x = 0
        y = 1
        g = b
        return a, b, x, y, g
    a1, b1, x1, y1, g = egcd(b%a, a, x, y, g)
    #print('Numbers that got received by the function call', a1, b1, x1, y1, g)
    x = y1 - (b//a) * x1
    y = x1
    return (a, b, x, y, g)

def main():
    print('This is a program to implement the affine cryptographic algorithm')
    print('This implementation does first the addition and then the multiplication for encryption and vice versa for decryption, another version of this algorithm would be possible where first you do multiplication and then the addition')
    plaintext = input('Please enter the message text to decrypt\n')
    plaintext = plaintext.lower()
    a_key = int(input('Please enter the key for the additive part\n'))
    m_key = int(input('Please enter the key for multiplicative part\n'))
    egcd_result = egcd(m_key, 26, 1, 1, -1)
    while (egcd_result[4] != 1):
        m_key = int(input('Please enter a valid key such that gcd of this key and 26 could be 1\n'))
        egcd_result = egcd(m_key, 26, 1, 1, -1)
    m_key_inverse = egcd_result[2]
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += chr(((ord(plaintext[i]) - 97 + a_key) * m_key) % 26 + 97)
    print('Ciphertext:', ciphertext)
    _ = input('Press a key to decrypt the message')
    decrypted = ''
    for i in range(len(ciphertext)):
        decrypted += chr((((ord(ciphertext[i]) - 97) * m_key_inverse) - a_key) % 26 + 97)
    print('Decrypted message:', decrypted)
    if decrypted == plaintext:
        print('Decryption successful')
if __name__ == '__main__':
    main()
