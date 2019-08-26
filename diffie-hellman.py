import random
print('Diffie-hellman key exchange')
#A key exchange protocol between alice and bob
#Big prime numbers
g = 15485863
n = 179424673
#Alice has private key x
x = random.randint(10**4, 10**5)
#Bob has private key y
y = random.randint(10**4, 10**5)
print('Alice\'s key, x:', x, '\nBob\'s Key, y:', y)

a = (g**x)%n
b = (g**y)%n
print('message received by bob:', a, '\nmessage received by alice:', b)

alice = (b**x)%n
bob = (a**y)%n
print('computed shared key with alice:', alice, '\ncomputed shared key with bob:', bob)