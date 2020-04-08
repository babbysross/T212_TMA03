#!/bin/python3      
'''Dictates which interpreter should be used, useful for sytems with multiple Python versions'''

count = 0           '''Establishes the variable count as an integer with value 0'''

while count < 100:  '''Loops the following commands until count == 100'''

  print( count )    '''Prints the current value of count'''
  
  if count < 50:    '''If the value of count is less than 50, the following command runs'''
    count += 5      '''Adds 5 to the current value of count'''
  else:             '''If the value is equal or greater than 50, the following command runs'''
    count += 10     '''Adds 10 to the current value of count.'''