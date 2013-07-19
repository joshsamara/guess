import sys, random, os
sys.path.append(".")
from words import *


def clear():
	os.system('clear')

def choose_letters():
	global letters
	global allwords
	print "How many letters: 3, 4 or 5?"
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
	else:
		print "Invalid choice."
		choose_letters()

def random_word():
	global choice
	global allwords
	choice=random.choice(allwords)

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
	print "Guess a word:"
	guess = raw_input().lower()
	if len(guess) != letters:
		print "Invalid guess. Guesses must be %s letters." % letters
		make_guess()
	else:
		attempts +=1
		if guess == choice:
			print "Correct! It took you %s attempts." % attempts
		else:
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
			next()

			
def next():
	global wrongs
	global rights
	global past
	global diff
	global letters
	clear()
	if diff == "E":
		print "Guess  |  Wrongs  |  Rights  |"
		print "=============================="
		if letters == 3:
			spaces = "  "
		elif letters == 4:
			spaces = " "
		else:
			spaces = ""
		for item in past:
			print "%s  |    %s     |     %s    |" %(item[0]+spaces,item[1],item[2])
		print ""
	else:
		item = past[-1]
		print "Last Guess: %s. %s Wrong. %s Right" % (item[0], item[1], item[2])
	make_guess()

def play_again():
	global playing
	print "Would you like to play again? Y/N"
	answer = raw_input().lower()
	if answer in ["yes","y","ye","yea","yeah","yep","mhm"]:
		playing = True
	else:
		playing = False

#GAME START HERE
playing = True
while playing:
	clear()
	attempts=0
	past = []
	choose_letters()
	random_word()
	choose_dif()
	print "Press enter to continue:"
	raw_input()
	clear()
	print choice
	make_guess()
	play_again()
