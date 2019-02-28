message = input('please enter your message').lower()
key = (int)(input('please enter a number between 1 and  25'))
if key < 1 :
	key = 1
elif key >25:
	key = 25
alphabet = 'abcdefghijklmnopqrstuvwxyz'

newmessage =''

for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		newposition = (position + key) % 26
		newmessage += alphabet[ newposition ]
	else :
		newmessage += character
print( newmessage )
