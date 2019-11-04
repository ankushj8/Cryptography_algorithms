# This is implementation of rabin miller cryptosystem
# that uses chinese remainder theorem

def multipli_inverse(a, b, x, y):
    #a*x + b*y = gcd
    #we have to find x
    #x is multiplicative inverse of a and y is of b
    if a == 0:
        x= 0
        y =1
        return (0, b, 0, 1)
    a1, b1, x1, y1 = multipli_inverse(b%a, a, x, y)
    #print('After function call inside the function', a1, b1, x1, y1)
    return a, b, y1 - (b//a) * x1, x1

def CRT(a, b, c, d):
	tuple_ = multipli_inverse(c, d, 1, 1)
	c_multi = tuple_[2]%d
	d_multi = tuple_[3]%c
	return int(a*d*d_multi + b*c*c_multi)
def main():

	print("Enter the private keys that should be large prime numbers\n")
	p = int(input("p: "))
	q = int(input("q: "))
	n = p*q
	print("Public key :", n)

	message = input("Enter the plaintext\n")
	message = message.lower()
	message_arr = []
	for i in range(len(message)):
		message_arr.append(ord(message[i]) - 97)

	encrypted = []
	for i in range(len(message_arr)):
		temp = (message_arr[i]**2)%n
		encrypted.append(temp)

	tempo1 = []
	tempo2 = []
	tempo3 = []
	tempo4 = []
	for i in range(len(message_arr)):
		tempo1.append(int((encrypted[i]**( (p+1) //4) ) % p))
		tempo2.append(int(-(encrypted[i]**( (p+1) //4) ) % p))
		tempo3.append(int((encrypted[i]**( (q+1) //4) ) % q))
		tempo4.append(int(-(encrypted[i]**( (q+1) //4) ) % q))

	plaintext1 = []
	plaintext2 = []
	plaintext3 = []
	plaintext4 = []

	for i in range(len(message_arr)):
		plaintext1.append(chr(CRT(tempo1[i], tempo3[i], p, q)%n+97))
		plaintext2.append(chr(CRT(tempo1[i], tempo4[i], p, q)%n+97))
		plaintext3.append(chr(CRT(tempo2[i], tempo3[i], p, q)%n+97))
		plaintext4.append(chr(CRT(tempo2[i], tempo4[i], p, q)%n+97))

	print("Posible characters are(at least one would be correct from each line)\n")
	print("".join(plaintext1))
	print("".join(plaintext2))
	print("".join(plaintext3))
	print("".join(plaintext4))

if __name__ == '__main__':
	main()
