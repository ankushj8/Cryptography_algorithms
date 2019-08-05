def gcd(a, b):
    #without loss of generality we can take the absolute
    #value of a and b. as gcd(a, b) == gcd(|a|, |b|)
    a = abs(a)
    b = abs(b)
    while (a!=0 or b!=0):
        if a == b:
            return a
        elif a < b:
            b = b - a
        elif b < a:
            a = a - b
    if a  == 0:
        return b
    else:
        return a

def multipli_inverse(a, b, x, y):
    #a*x + b*y = gcd
    #we have to find x
    #a is supposed to be the key and b is the no 26
    #x is multiplicative inverse of a and y is of b
    #print('Just at the start of function', a, b, x, y)
    if a == 0:
        x= 0
        y =1
        return (0, b, 0, 1)
    a1, b1, x1, y1 = multipli_inverse(b%a, a, x, y)
    #print('After function call inside the function', a1, b1, x1, y1)
    return a, b, y1 - (b//a) * x1, x1


def main():
    print('This is a program to implement multiplicative cipher')
    plaintext = input('Please enter the message text\n')
    plaintext = plaintext.lower()
    key = int(input('Please enter the key\n'))

    while (gcd(key, 26) != 1):
        key = int(input('Please enter a valid key so that gcd of key and 26 could be 1'))

    key_inverse_tuple = multipli_inverse(key, 26, 1, 1)
    print('This is the returned key inverse tuple:', key_inverse_tuple)
    key_inverse = key_inverse_tuple[2]
    print('This is the key inverse:', key_inverse)
    
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += chr(((ord(plaintext[i]) - 97) * key) % 26 + 97)
    print('Ciphertext:\n' + ciphertext)
    _ = input('Please enter a key to decrypt the message')
    
    decrypted = ''
    for i in range(len(ciphertext)):
        decrypted += chr(((ord(ciphertext[i]) - 97) * key_inverse) % 26 + 97)
    print('Decrypted message:',decrypted)
    if decrypted == plaintext:
        print('Decryption succesfull')


if __name__ == '__main__':
    main()