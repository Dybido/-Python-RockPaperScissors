#!/usr/bin/python

import os,sys, random

print "Welcome to a game of Rock, Paper, Scissors!"

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

if choice == "rock" and computer_choice == "rock":
	print "It's a tie!"
elif choice == "rock" and computer_choice == "scissors":
	print "You win! :)"
elif choice == "rock" and computer_choice == "paper": 
	print "You lose! :("

if choice == "scissors" and computer_choice == "scissors":
	print "It's a tie!"
elif choice == "scissors" and computer_choice == "paper":
	print "You win! :)"
else: 
	print "You lose! :("

if choice == "paper" and computer_choice == "paper":
	print "It's a tie!"
elif choice == "paper" and computer_choice == "rock":
	print "You win! :)"
else: 
	print "You lose! :("
