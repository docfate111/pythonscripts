def createMatrix(k):
	input=removeDuplicate(k)
	alphabet="abcdefghiklmnopqrstuvwxyz"
	for i in input:
		if i not in alphabet:
			input+=i
	arr=[[0 for i in range(5)] for y in range(5)]
	for p in range(5):
		a=0
		for i in input[a:a+5]:
			arr[p][a%5]=i
		a+=5
	return arr
def removeDuplicate(input):
	ans="" #code to remove duplicate letters
	for i in input:
		for j in input:
			if i!=j:
				ans+=i
	return ans
if __name__=='__main__':
	print(removeDuplicate("secretMessage"))

