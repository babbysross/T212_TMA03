#!/bin/python3
# T212 TMA03 Question 11

def farecalc():                                                             #function to calculate fare
    base =  4.7                                                             #define base fare 
    prev = float(input('Please input today\'s prevailing rate fare: £'))    #ask to input prevailing rate and store as float
    while prev < 0 :                                                        #while loopt for negative inputs
        prev = input('The prevailing rate must be positive: £')             #ask for positive input
    dist = float(input('Please input the distance travelled in miles: '))   #ask to input prevailing rate and store as float
    while dist < 0:                                                         #while loopt for negative inputs
        dist = input('Distance travelled should be positive: ')             #ask to input prevailing rate and store as float
    calcdist = dist - 1                                                     #calculate distance charged at prevailing rate
    farecalc.total = base + (prev*calcdist)                                 #calculate total fare
    print(f'The total fare is £ {farecalc.total:.2f}')                      #print total fare, to 2 decimal places
    repeatme()                                                              #trigger repeat function

def repeatme():                                                             #function to rerun or end script
    repeat = input('\nWould you like to calculate another fare?(y/n): ')    #ask to rerun or end script
    if repeat.lower() == 'y':                                               #if statement for positive input
        farecalc()                                                          #run fare calculation function again
    elif repeat.lower() == 'n':                                             #elseif statement for negative input
        quit()                                                              #terminate script
    else:                                                                   #else statement
        print('Please input a correct response(y/n): ')                     #request a valid response
        repeatme()                                                          #rerun repeatme function

farecalc()                                                                  #intialise script