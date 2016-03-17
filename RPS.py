#!/usr/bin/python

import os, sys, random

def condition(u, v):
	user = 0
	computer = 0

	if u == v:
		print "It's a tie!"
	elif u == "rock" and v == "scissors":
		print "You win! :)"
		user += 1
	elif u == "rock" and v == "paper": 
		print "You lose! :("
		computer += 1
	elif u == "scissors" and v == "paper":
		print "You win! :)"
		user += 1
	elif u == "scissors" and v == "rock": 
		print "You lose! :("
		computer += 1
	elif u == "paper" and v == "rock":
		print "You win! :)"
		user += 1
	else: #choice == "paper" and computer_choice == "scissors": 
		print "You lose! :("
		computer += 1
	# Python can return multiple variables using tuples, dicts & lists to be returned 	
	return (user, computer)

print "Welcome to a game of Rock, Paper, Scissors!"

while 1:
	choice = raw_input("To begin, please type rock, paper or scissors \n")

	dice = random.randint(1,6)

	if dice <= 2:
		computer_choice = "rock"
	elif dice > 2 and dice <= 4:
		computer_choice = "paper"
	else:
		computer_choice = "scissors"	

	print "Your choice is", choice
	print "The computer's choice is", computer_choice

	(p1,p2) = condition(choice, computer_choice)

	print "The score is now You/Computer:", p1, "/", p2

	cont = raw_input("Would you like to continue playing? (yes/no) \n")
	if cont == "no":
		break
	else: 
		pass
	