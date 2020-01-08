import math
def add(a, b):
    print(a+b)
def subtract(a, b):
    print(a-b)
def multiply(a, b):
    print(a*b)
def divide(a, b):
    print(a/b)
def exponent(a, b):
    print(a**b)
def root(a, b):
    c=1/b
    print(a**c)
def gcd(a, b):
    print (gcd(a, b))
def lcm(a, b):
    if a>=b:
        x=b
    else:
        x=a
    for item in range(1, x+1):
        num=item+1
        if a%num==0:
            if b%num==0:
                print(num)
                break
#yay recursions
def mult(a, b):
	if b==1:
		return a
	else:
		return a+mult(a, b-1)
def fact(a):
	if a==1:
		return a
	else:
		return a*fact(a-1)
def fib(a):
	if a==1:
		return a
	else:
		return a+fib(a-1)
def miniMaxSum(arr):
	big, sml, sum=0, 10000000000000000000000000000000, 0
	for i in range(len(arr)):
		for j in range(len(arr)):
			if j!=i:
				sum+=arr[j]
		if sum<sml:
			sml=sum
		if sum>big:
			big=sum
		sum=0
	print(str(sml)+" "+str(big))
#miniMaxSum([1, 2, 3, 4, 5])



#def maxwiseProduct(a,b):
    #if a 