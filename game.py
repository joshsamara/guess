import sys, random, os
sys.path.append(".")
from words import *


def clear():
	os.system('clear')

def choose_letters():
	global letters
	global allwords
	print "How many letters - 3, 4 or 5?"
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




#GAME START HERE
clear()
choose_letters()
random_word()
print choice