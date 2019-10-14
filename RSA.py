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


def  main():
    #large prime numbers
    #WRite code here
    p = int(input())
    q = int(input())
    
    n = p*q #Public
    print("\nPublic info, n:\n", n)
    phi = (p-1)*(q-1)
    for i in range(phi-1, 1, -1):
        if gcd(i, phi) == 1:
            e = i #Public key
            break
    
    inverse_tuple = multipli_inverse(e, phi, 1, 1)
    print('\nThis is the returned inverse tuple:\n', inverse_tuple)
    d = key_inverse_tuple[2] #private key
    
    #Message
    m = input("\nPlease enter message\n")
    m_list = list(m)
    
    #Encryption
    for i in range(len(m_list)):
        m_list[i] = ord(m_list[i])
        m_list[i] = (m_list[i]**e)%n
    print("Encrypted message", ''.join(m_list))

    #Decryption
    m_d = [0]*len(m_list)
    decrypted = ''
    for i in range(len(m_list)):
        m_d[i] = (m_list[i]**d)%n
        decrypted += chr(m_d[i])
    print("\nDecryptd message\n", decypted)

if __name__ == '__main__':
    main()
    