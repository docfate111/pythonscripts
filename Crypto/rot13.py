alphabet="abcdefghijklmnopqrstuvwxyz"
user_input=input("Enter a string:")
shiftby=int(input("Enter a number to shift by:"))
output=""
for i in range(len(user_input)):
	character=user_input[i]
	location_of_character=alphabet.find(character)
	new_location=location_of_character+shiftby
	output+=alphabet[(new_location)%26]
print(output)
	
	