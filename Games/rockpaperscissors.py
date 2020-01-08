import random
userPoints=0
computerPoints=0
cont=0
print("Rock paper scissors game")
options=["rock", "paper", "scissors"]
while cont==0:
	userInput=input("Rock, paper, or scisors? (all input must be lowercase with proper spelling")
	computerChosen=options[random.randint(0, 2)]
	if userInput=="rock":
		if computerChosen=="rock":
			print("Rock and Rock. Play again")
		if computerChosen=="paper":
			userPoints+=1
			print("Paper beats rock. You won this round")
		if computerChosen=="scissors":
			computerPoints+=1
			print("Scissors beats rock. You lost this round")
	if userInput=="scissors":
		if computerChosen=="rock":
			computerPoints+=1
			print("Scissors beats rock. You lost this round ")
		if computerChosen=="scissors":
			print("Scissors and scissors. You won this round ")
		if computerChosen=="paper":
			computerPoints+=1
			print("Scissors beats paper. You lost this round ")
	if userInput=="paper":
		if computerChosen=="paper":
			print("Paper and Paper. Play again ")
		if computerChosen=="rock":
			userPoints+=1
			print("Paper beats rock. You won this round ")
		if computerChosen=="scissors":
			computerPoints+=1
			print("Scissors beats paper. You lost this round ")
	else:
		print("invalid input try again")
	print("your points:"+str(userPoints)+"  computerPoints:"+str(computerPoints))	
	n=input("continue? type yes to continue or anything else for no ")
	if n is not "yes":
		break
print("good game")

