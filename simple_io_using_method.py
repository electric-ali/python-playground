#!/usr/bin/python3
# Prints two string output which is given by the user as input using a method.

def take_input():
	x = input("Type your input here: ")
	return x

prompted = "Your 1st Text: {} and 2nd Text: {}"
print(prompted.format(take_input(),take_input()))