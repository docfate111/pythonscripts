import math #for quickmaths
def md5(message):
	message = bytearray(message, 'utf8') #move input into mutable type
	#add the length of the message in binary to it
	orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff
	#add 1 in hex for padding
	message.append(0x80)
	#padding again but this time with zeroes
	while len(message)%512!=448:
		message.append(0)
	message+=orig_len_in_bits.to_bytes(8, byteorder='little')
	#initialize 4 word md buffer of 32bit registers:
	a0=0x67452301   
	b0=0xefcdab89   
	c0=0x98badcfe   
	d0=0x10325476
	#functions for later:
	def F(x, y, z):
		return (x&y)|((~x)&z)
	def G(x, y, z):
		return (x&z)|(y&(~z))
	def H(x, y, z):
		return (x^y)^z
	def I(x, y, z):
		return y^(x|(~z))
	#define leftrotate function:
	def leftrotate(x, c):
		return (x << c)|(x >> (32-c))
	#initialize some vectors:
	s=[7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5, 9, 14, 20, 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23, 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
	#Use binary integer part of the sines of integers (Radians) as constants to generate shift amount:
	K=[int(abs(math.sin(i+1))*2**32)&0xFFFFFFFF for i in range(64)]
	for j in range(0, len(message), 64):
		chunk=message[j:j+64]
		A=a0
		B=b0
		C=c0
		D=d0
		#main loop:
		for i in range(64):
			if i<=19:
				f=F(B, C, D)
				g=i
			elif i<=31:
				f=G(B, C, D)
				g=((5*i)+1)%16
			elif i<=47:
				f=H(B, C, D)
				g=((3*i)+5)%16
			elif i<=63:
				f=I(B, C, D)
				g=(7*i)%16
			f=f+A+K[i]+int.from_bytes(chunk[4*g:4*g+4], byteorder='little')
			A=D
			D=C
			C=B
			B+=leftrotate(f, s[i])
			#append to chunk's hash to result so far:
			A=(a0+A)&0xffffffff
			B=(b0+B)&0xffffffff
			C=(c0+C)&0xffffffff
			D=(d0+D)&0xffffffff
	#returning little endian:
	return hex(int(str(A)+str(B)+str(C)+str(D)))
if __name__=='__main__':
	i=input("What phrase would you like to encrypt with MD5 hashing algorithm? ")
	print(md5(i))
	#for some reason the output is always the same
	