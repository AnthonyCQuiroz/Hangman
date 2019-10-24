# Anthony Quiroz 


mystery = list("mississippi")
guessList = list("___________")

guess = input("Guess a letter: ")

index = 0
for letter in mystery:
	if letter == guess:
		guessList[index] = guess 
	index += 1
print(guessList)



secret = []
# how to create a list _ in place of letter


	# how to check if a letter is in a word 
letter = input("Type a letter: ")
if letter in mystery:
	print("Letter is in the word: ")
else:
	print("Letter is not in the word")
	
#how to replace items in a list 

mystery = list("mississippi")
guessList = list("___________")

guess = input("Guess a letter: ")

index = 0
for letter in mystery:
	if letter == guess:
		guessList[index] = guess 
	index += 1
print(guessList)

# how to keep track of misses
secret = "mississippi"
misses = list(secret)
misses = 0


hangList = [ 
'''
     +===+
     O   |
         |
         |
        ===''' ,
'''
     +===+
     O   |
     |   |
         |
        === ''',
'''
     +===+
     O   |
    /|   |
         |
        === ''',
'''
     +===+
     O   |
    /|\\  |
         |
        === ''',
'''
     +===+
     O   |
    /|\\  |
    /    |
        === ''',
'''
     +===+
     O   |
    /|\\  |
    / \\  |
        ==='''

        ]

while misses < 7:
	print(hangList[misses])
	guess = input("Guess a letter: ")
	if guess in secret:
		# loop through secret and find all the matching letters
		print("That letter is in the secret word")
	else:
		misses = misses + 1 
