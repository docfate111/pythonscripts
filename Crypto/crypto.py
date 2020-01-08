import math
import detectEnglish
import cryptomath
def reverseCipherenc(input):
    str=""
    for i in range(0, len(input)):
        str=str+input[len(input)-i-1]
    return str
#also knwon as the shift cipher
def CaesarCipherEnc(input, key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    newAlphabet=alphabet[key:]+alphabet[:key-1]
    st=""
    for item in range(len(input)):
        for j in range(25):
          if input[item]==alphabet[j]:
            st+=newAlphabet[j]
    return st
def CaesarCipherDec(input, key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    newAlphabet=alphabet[key:]+alphabet[:key-1]
    st=""
    for item in range(len(input)):
        for j in range(25):
          if input[item]==newAlphabet[j]:
            st+=alphabet[j]
    print(st)
def bruteforceCaesarCipherDec(input):
    s=""
    for i in range(26): 
        s+=CaesarCipherDec(input, i)
        print(str(i)+":"+s)
def transpositionCipherEnc(input, key):
    s=""
    for n in range(key):
        for i in range(len(input)):
            if i%key==n:
                s+=input[i]
    print(s)
def transpositionCipherDec(key, m):
	message=str(m)
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list of strings
    # The number of "columns" in our transposition grid:
	numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid will need:
	numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
	numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    # Each string in plaintext represents a column in the grid.
	plaintext = [''] * numOfColumns
    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
	column = 0
	row = 0
	for symbol in message:
		plaintext[column] += symbol
		column += 1 # Point to next column.
        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
		if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
			column = 0
			row += 1
	return ''.join(plaintext)
def bruteforceTransCipher(m):
	message=str(m)
	for key in range(1, len(str(message))):
		print("Trying key: "+str(key))
		decryptedText=transpositionCipherDec(key, message)
		if detectEnglish.isEnglish(decryptedText):
			print()
			print("possible decryption:")
			print("Key %s: %s" % (key, decryptedText[:100]))
			print()
			print("Enter D if done, anything else to continue:")
			response = input("> ")
def affineCipherEnc(input, a, b):
	#make sure keys a and b are both relatively prime otherwise the mod inverse won't exist
	alphabet="abcdefghijklmnopqrstuvwxyz"
	s=""
	for j in range(len(input)):
		for i in range(26):
			if input[j]==alphabet[i]:
				n=(i*a+b)%26
				s+=alphabet[n]
	print(s)
def affineCipherDec(input, a, b):
	alphabet="abcdefghijklmnopqrstuvwxyz"
	s=""
	c=int(cryptomath.findModInverse(a, 26))
	for j in range(len(input)):
		for i in range(26):
			if input[j]==alphabet[i]:
				n=((i-b)*c)%26
				s+=alphabet[n]
	print(s)
def bruteforceAffineDec(m):
	message=str(m)
	for a in range(26):
		for b in range(26):
			if cryptomath.gcd(a, 26)==1:
				print("  ")
				userInput=input("type enter to continue and e to exit")
				print("  ")
				if userInput=="e":
					break
				d=str(affineCipherDec(message, a, b))
def subCipherEnc(newAlphabet, stringToencrypt):
	newAlphabet=newAlphabet.lower()
	alphabet="abcdefghijklmnopqrstuvwxyz"
	s=""
	for i in range(0, len(stringToencrypt)):
		for j in range(26):
			if stringToencrypt[i]==alphabet[j]:
				s+=newAlphabet[j%26]
	print(s)
def subCipherDec(newAlphabet, stringToencrypt):
	newAlphabet=newAlphabet.lower()
	alphabet="abcdefghijklmnopqrstuvwxyz"
	s=""
	for i in range(0, len(stringToencrypt)):
		for j in range(26):
			if stringToencrypt[i]==newAlphabet[j]:
				s+=alphabet[j%26]
	print(s)
def vigenereCipherEnc(message, key):
	alphabet="abcdefghijklmnopqrstuvwxyz"
	s=""
	nums=[]
	newKey=""
	for i in range(int(len(message)/len(key))):
		newKey+=key
	newKey+=newKey[:(len(message)%len(key))]
	for k in range(len(newKey)):
		for i in range(26):
			if newKey[k]==alphabet[i]:
				nums.append(i)
	for k in range(len(message)):
		for i in range(26):
			if alphabet[i]==message[k]:
				s+=alphabet[(nums[k]+i)%26]
	print(s)
def vigenereCipherDec(message, key):
	alphabet="abcdefghijklmnopqrstuvwxyz"
	s=""
	nums=[]
	newKey=""
	for i in range(int(len(message)/len(key))):
		newKey+=key
	newKey+=newKey[:(len(message)%len(key))]
	for k in range(len(newKey)):
		for i in range(26):
			if newKey[k]==alphabet[i]:
				nums.append(i)
	for k in range(len(message)):
		for i in range(26):
			if alphabet[i]==message[k]:
				s+=alphabet[(i-nums[k]+26)%26]
	print(s)
def oneTimePadEnc(message):
	alphabet="abcdefghijklmnopqrstuvwxyz"
	s=""
	key=""
	nums=[]
	for i in range(len(message)):
		nums.append(random.randrange(26))
	for k in range(len(nums)):
		key+=alphabet[nums[k]]
	for k in range(len(message)):
		for i in range(26):
			if message[k]==alphabet[i]:
				s+=alphabet[(nums[k]+i)%26]
	print("this is the key: "+key+" and this is the message: "+s)
def oneTimePadDec(message, key):
	alphabet="abcdefghijklmnopqrstuvwxyz"
	s=""
	nums=[]
	for i in range(len(key)):
		for j in range(26):
			if key[i]==alphabet[j]:
				nums.append(j)
	for i in range(len(message)):
		for j in range(26):
			if message[i]==alphabet[j]:
				s+=alphabet[(j-nums[i]+26)%26]
	print(s)
def main():
	#to include symbols change alphabet strings to include them
    #a=CaesarCipherEnc(input, 2)
    CaesarCipherDec("jollzl", 7)
	#lol realized .find() method exists could make all of these algorithms more efficient
    '''bruteforceCaesarCipherDec(input)
	transpositionCipherEnc("secret messages", 6)
	bruteforceTransCipher("s gemecesrsesta")
    transpositionCipherDec(6, "tsheicsriest")
    reverseCipherenc("word")
	affineCipherEnc("supersecretmessage", 7, 3)
	affineCipherDec("znefszfrsfgjfzzdtf", 7, 3)
	bruteforceAffineDec("znefszfrsfgjfzzdtf")
	subCipherEnc("VJZBGNFEPLITMXDWKQUCRYAHSO", "attackatdawn")
	subCipherDec("VJZBGNFEPLITMXDWKQUCRYAHSO", "vccvzivcbvax")
	vigenereCipherEnc("commonsenseisnotsocommon", "pizza")
	vigenereCipherDec("rwllocadmstqrmoianbobunm", "pizza")
	oneTimePadEnc("secretmessage")
	oneTimePadDec("smadddpjbpkpn", "aiymzkdfjxkjj")'''
main()