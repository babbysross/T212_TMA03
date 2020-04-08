#!/bin/python3

# This program simulates rolling a six sided dice 1000 times.
# It counts the total number of times even and odd numbers
# come up for each roll of the dice, and prints the results.
# It has a syntax error and a semantic error.

# importing random number generator
import random

# Setting the initial values for the simulation
roll = 0 # The number of times the dice is rolled
even = 0 # Counter for even numbers
odd =  0 # Counter for odd numbers

while roll < 1000:
  
  dice = random.randint(1, 6) # returns a value between 1 and 6
  
  # even numbers divided by 2 give an integer result
  # odd numbers divided by 2 give a non-integer value
  
  if dice/2 == int(dice/2):
    even += 1
  else:
    odd += 1
  
  roll += 1
  
print("Odd count  = ", odd)
print("Even count = ", even)