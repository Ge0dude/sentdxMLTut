#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:52:05 2017

@author: brendontucker
"""

import random 
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def rolldice():
    roll = random.randint(1,100)
    if roll == 100:
#        print (roll) 
#        print( 'You lost')
        return False
    elif roll <= 50:
#        print (roll) 
#        print ('You lost')
        return False
    elif 100 > roll >= 51:
#        print (roll) 
#        print ('You win')
        return True
        
def simpleBettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    wX = []
    vY = []
    
    currentWager = 1
    
    while currentWager <= wager_count:
        if rolldice(): #if True is resturned this will execute
            value = value + wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value = value - wager  #value -= wager why didn't that work, why
            #did I have to write it out?
            wX.append(currentWager)
            vY.append(value)
            
            
        currentWager += 1
    #print('Funds:', value)
    plt.plot(wX, vY)
        
for x in range(100):
    simpleBettor(10000, 100, 100)
       
        
        
        
        
        
        
        
        
#    
#for x in range(100):
#    result = rolldice()
#    print(result)
    
    
#testing to see how often 100 shows up
#resultList = []
#for x in range(1000):
#    result = rolldice()
#    resultList.append(result)
#    
#for y in resultList:
#    if y == 100:
#        print('yak')
