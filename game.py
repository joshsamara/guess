import sys, random, os, math
sys.path.append(".")
from words import *


def clear():
	os.system('clear')

def choose_letters():
	global letters
	global allwords
	global gametype
	gametype = "word"
	print "Play with a (3),(4),(5) letter Word or (N)umber?"
	letters = raw_input().lower()
	if letters in ["three", "3"]:
		letters = 3
		allwords = all_words_3
		print "3 letter words chosen"
	elif letters in ["four", "4"]:
		letters = 4
		allwords = all_words_4
		print "4 letter words chosen"
	elif letters in ["five", "5"]:
		letters = 5
		allwords = all_words_5
		print "5 letter words chosen"
	elif letters in ["n", "num", "numb", "number"]:
		print ""
		get_digits()
	else:
		print "Invalid choice."
		choose_letters()

def get_digits():
	global letters
	print "How many digits? Must be greater than 0. Suggested <= 5"
	letters = raw_input()
	try:
		letters=int(letters)
		math.sqrt(1/letters) #get rid of 0 and negatives 
		print "%d digit number chosen" % letters
		print ""
		get_num_type()
	except:
		print "Invalid choice."
		get_digits()

def get_num_type():
	global gametype
	print "Game type (A) or (B)?"
	print "A: Guess by digits"
	print "B: Greater or less than"
	gametype = raw_input().lower()
	if gametype == "a":
		gametype = "numba"
		print "Game type A chosen"
	elif gametype == "b":
		gametype = "numbb"
		print "Game type B chosen"
	else:
		print "Invalid choice."
		get_num_type()

def random_word():
	global choice
	global allwords
	global gametype
	global letters
	if gametype=="word":
		choice=random.choice(allwords)
	else:
		choice = ""
		for digit in range(0,letters):
			choice+=str(random.randint(0,9))

def choose_dif():
	global diff
	print "(E)asy or (H)ard?"
	diff = raw_input().lower()
	if diff in ["easy","e"]:
		diff = "E"
		print "Easy mode chosen."
	elif diff in ["hard", "h"]:
		diff = "H"
		print "Hard mode chosen."
	else:
		print "Invalid choice."
		choose_dif()

def remove_letter(word, position):
	return word[:position] +" "+word[(position+1):]

def make_guess():
	global attempts
	global choice
	global letters
	global wrongs
	global rights
	global past
	global gametype

	if "numb" in gametype:
		toprint = "number"
	else:
		toprint = "word"
	print "Guess a %s:" % toprint
	guess = raw_input().lower()
	if guess == "i give up!":
		print "You lose after %s attempts." % attempts
		print "The word was: %s" % choice
	elif guess == "$h0w m3!!1!":
		print "The word is: %s" % choice
		attempts += 9001
		raw_input()
		next()
	elif len(guess) != letters and gametype != "numbb":
		print "Invalid guess. Guesses must be %s characters." % letters
		make_guess()
	elif "numb" in gametype and (not (guess.isdigit()) or len(guess) > letters):
		print "Invalid guess. Must guess an integer <= the nubmer of digits."
		make_guess()
	else:
		attempts +=1
		if guess == choice:
			print "Correct! It took you %s attempts." % attempts
		else:
			if gametype != "numbb":
				wrongs = 0
				rights = 0
				temp_guess = guess
				temp_choice = choice
				for i in range(0,letters):
					if temp_guess[i] == temp_choice[i]:
						rights += 1
						temp_guess=remove_letter(temp_guess,i)
						temp_choice=remove_letter(temp_choice, i)
				for letter in temp_guess:
					if letter in temp_choice and letter != " ":
						wrongs += 1
						temp_choice=remove_letter(temp_choice, temp_choice.index(letter))
				past.append([guess, wrongs, rights])
			else:
				if int(guess) < int(choice):
					pos = "less"
				else:
					pos = "greater"
				past.append([guess, pos])
			next()


def next():
	global wrongs
	global rights
	global past
	global diff
	global letters
	global gametype
	clear()
	if diff == "E":
		after_guess = " "*max(1, letters - 5)
		first_len = len("Guess") + len(after_guess)
		if gametype != "numbb":
			print "Guess%s|  Wrongs  |  Rights  |" % after_guess
			print "============================%s" % ("="*len(after_guess))
			for item in past:
				print "%s%s|    %s     |     %s    |" %(item[0], " "*max(0,(first_len-len(item[0]))),item[1],item[2])
			print ""
		else:
			print "Guess%s|  Guess is lesser or greater  |"%after_guess
			print "=====================================%s" % ("="*len(after_guess))
			for item in past:
				print "%s%s|          %s" % (item[0]," "*max(0,(first_len-len(item[0]))),item[1])
	else:
		item = past[-1]
		if gametype != "numbb":
			print "Last Guess: %s. %s Wrong. %s Right" % (item[0], item[1], item[2])
		else:
			print "Last Guess: %s was %s" % (item[0], item[1])
	make_guess()

def play_again():
	global playing
	print "Would you like to play again? Y/N"
	answer = raw_input().lower()
	if answer in ["yes","y","ye","yea","yeah","yep","mhm"]:
		playing = True
	else:
		playing = False

# Not actually useful because you dont need a whole list to make a guess...
# def gen_num_list(digits):
# 	num_list = []
# 	for i in range(0,int(math.pow(10,digits))):
# 		num_string = str(i)
# 		if len(num_string) < digits:
# 			num_string = "0"*(digits-len(num_string))+num_string
# 		num_list.append(num_string)
# 	return num_list


clear()
print"""
=============================================================
=   *   *   *   *   *   *   *   *   *   *   *   *   *   *   =
=============================================================
=     ______                                          __    =
=    /      \                                        /  |   =
=   /$$$$$$  | __    __   ______    _______  _______ $$ |   =
=   $$ | _$$/ /  |  /  | /      \  /       |/       |$$ |   =
=   $$ |/    |$$ |  $$ |/$$$$$$  |/$$$$$$$//$$$$$$$/ $$ |   =
=   $$ |$$$$ |$$ |  $$ |$$    $$ |$$      \$$      \ $$/    =
=   $$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |$$$$$$  | __    =
=   $$    $$/ $$    $$/ $$       |/     $$//     $$/ /  |   =
=    $$$$$$/   $$$$$$/   $$$$$$$/ $$$$$$$/ $$$$$$$/  $$/    =
=                                                           =
=============================================================
=   *   *   *   *   *   *   *   *   *   *   *   *   *   *   = 
=============================================================
=   Game by: Josh Samara                                    =
=   Art by: http://patorjk.com/software/taag/               =
=============================================================

"""
raw_input()

#GAME START HERE
playing = True
while playing:
	clear()
	attempts=0
	past = []
	choose_letters()
	random_word()
	print ""
	choose_dif()
	print "Press enter to continue:"
	raw_input()
	clear()
	make_guess()
	play_again()
