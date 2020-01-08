def reflect(px, py, qx, qy):
	rx=2*qx-px
	ry=2*qy-py
	print(rx)
	print(ry)
def numOfHandshakes(n):
	h=0
	for i in range(n):
		h+=i
	print(h)
def numOfprimeFactors(n):
	count=0
	for i in range(n):
		if n%i==0:
			count+=1
	print(count)
def SieveOfEratosthenes(n):
	not_prime = []
	for i in range(2, n+1):
		if i not in not_prime:
			primes.append(i)
			#print(i)
			for j in range(i*i, n+1, i):
				not_prime.append(j)
if __name__=="__main__":
	#reflect(7, 8, 9, 1)
	#numOfHandshakes(5)
	#numOfprimeFactors(12)
	primes=[]
	SieveOfEratosthenes(1000000)
	print(primes)