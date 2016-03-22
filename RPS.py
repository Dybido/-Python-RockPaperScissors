#!/usr/bin/python

import os, sys, random, re

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

u=0
v=0

while 1:
	choice = raw_input("To begin, please type rock, paper or scissors \n")
	#Cleaning input by removing non-alphabetical characters and converting all to lowercase
	choice = choice.lower()
	choice = re.sub('[\W\d]*', '', choice)
	weapons = ["rock", "paper", "scissors"]

	#random.choice is good for choosing a random element from a list 
	computer_choice = random.choice(weapons)

	print "Your choice is", choice
	print "The computer's choice is", computer_choice

	(p1,p2) = condition(choice, computer_choice)

	u += p1
	v += p2

	print "The score is now You/Computer:", u, "/", v

	cont = raw_input("Would you like to continue playing? (yes/no) \n")
	if cont == "no":
		print "The final score is", u, "/", v
		break
	else: 
		pass
	