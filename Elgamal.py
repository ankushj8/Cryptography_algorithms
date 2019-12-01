# Elgamal cryptosystem
# A group has a primitive root if it's order is of the form 2, 4, p^a, or 2p^a, where p is an odd prime and a>=1 
# That is why to keep things simple, we are considering groups having only prime number as order
# Using group of modulus n over multiplication

from random import randrange

def multipli_inverse(a, b, x, y):
    #a*x + b*y = gcd
    #we have to find x
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
    n = int(input('''Enter order of the "prime" group(Pick a value larger than 26)\n'''))
    d = int(input('Select a private key such that it is greater than 0 and less than {}-1\n'.format(n)))
    for i in range(2, n):
        if (i**(n-1))%n == 1:
            e1 = i # generator
            break
    print('Generator(e1)', e1)
    e2 = (e1**d)%n
    print('e2:', e2)

    message = input('Enter message\n')
    message = message.lower()
    mes_len = len(message)
    mes_list = []
    for i in range(mes_len):
        mes_list.append(ord(message[i])-96)
    print(mes_list)

    # Encryption
    print('Encryption')
    r = randrange(100)
    c1 = (e1**r)%n
    c2 = []
    for i in range(mes_len):
        c2.append((mes_list[i]*(e2**r))%n)
    print('Public information:')
    print('Generator(primitive root)(e1)', e1)
    print('e2', e2)
    print('c1', c1)
    print('c2', c2)

    # Decryption
    print('Decryption')
    dec_meg = []
    decrypted = ''
    for i in range(mes_len):
        mul_inv = multipli_inverse(c1**d, n, 0, 0)
        mul_inv = mul_inv[2]
        dec_meg.append((c2[i]*mul_inv)%n)
        decrypted += chr(dec_meg[i] + 96)
    print('Decrypted characters\' numbers:', dec_meg)
    print('Decrypted message:', decrypted)
    if decrypted == message:
        print('Encryption - Decryption successful')
if __name__ == '__main__':
    main()
