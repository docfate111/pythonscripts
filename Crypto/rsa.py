import random
import math
#generates list of primes:
def primes_up_to(limit):
    is_prime = [False] * 2 + [True] * (limit - 1) 
    for n in range(int(limit**0.5 + 1.5)): # stop at ``sqrt(limit)``
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]
def generateKeys(k, e):
	#trying to make the keys more random by changing n around
	a=random.randint(k, 2*k)
	b=random.randint(k, 3*k)
	x=primes_up_to(k*(k-1))[a]
	y=primes_up_to(k*(k-2))[b]
	#2048 bit numbers=>4096bit n
	totient=(x-1)*(y-1)
	n=x*y
	#the totient must be coprime with n
	return totient, n
def extendedEucl(e, totient):
	#extended Euclidean algorithm to find modular inverses:
	new_totient, other_tot=totient, totient
	a, b=e, 1
	while a!=1:
		x, y=a, b
		a,b =new_totient%x, other_tot-(new_totient//x)*y
		new_totient, other_tot=x, y
		if b<=0:
			b+=totient
	return b
	#b is d or the decryption/private key
def encrypt(m, e, n):
	return (m**e)%n
def decrypt(c, d, n):
	return (c**d)%n
if __name__=='__main__':
	m=input("Secret number: ")
	e=input("Encryption number: ")
	#convert message instead if you want
	print("Private key D: "+extendedEucl(e, generateKeys(400, e)[0]))
	print("Encrypted number: "+str(encrypt(m, e, generateKeys(400, e)[1])))
	print("Public keys: ")
	print("E: "+str(e)+"\n"+"N: "+generateKeys(400, e)[1])
	print(decrypt(encrypt(m, e, generateKeys(400, e)[1])), extendedEucl(e, generateKeys(400, e)[0]))
	