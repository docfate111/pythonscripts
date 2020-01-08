import random
file=open(r"C:\Users\tdwil\OneDrive\Email attachments\Documents\Python Scripts\gamerz\Dictionary.txt", "r")
n=int(random.randrange(0, 45333))
lines=file.readlines()[:n]
actualWord=list(lines[-1])
del actualWord[-1]
#generates random word from dictionary file
def isWordGuessed(secretWord, lettersGuessed):
	count=0
	for i in range(len(secretWord)):
		if secretWord[i] in lettersGuessed:
			count+=1
	if count==len(secretWord):
		return True
	else:
		return False
def getGuessedWord(secretWord, lettersGuessed):
	str=['_']*len(secretWord)
	for i in range(len(secretWord)):
		if secretWord[i] in lettersGuessed:
			str[i]=secretWord[i]
	return ' '.join(str)
def getAvailableLetters(lettersGuessed):
	alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in lettersGuessed:
		if i in alphabet:
			alphabet.remove(i)
	return ' '.join(alphabet)
def hangman(secretWord):
	print("Loading word list from file...")
	print("45333 words loaded.")
	print("Welcome to the game Hangman!")
	print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
	print("-------------")
	lettersGuessed=""
	n=20
	while n>0:
		print("You have "+str(n)+" guesses left.")
		print("Available Letters: "+getAvailableLetters(lettersGuessed))
		guess=input("Please guess a letter: ")
		n-=1
		lettersGuessed+=guess
		if guess in secretWord:
			print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
			print("-------------") 
		elif getGuessedWord(secretWord, lettersGuessed)==secretWord:
			return "Congratulations, you won!"
		else:
			print("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed)) 
			print("-------------")
	if n==0:
		print("Sorry, you ran out of guesses. The word was "+str(secretWord))
hangman((''.join(actualWord)).lower())