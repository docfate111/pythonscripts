low=0
high=100
print('Please think of a number between 0 and 100!')
i=""
while i!='c':
	guess=(low+high)//2
	print("Is your secret number "+str(guess)+"?")
	i=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if i=='h':
		high=guess
	if i=='l':
		low=guess
	else:
		print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: '+str(guess))