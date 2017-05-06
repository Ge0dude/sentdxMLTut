#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:52:05 2017

@author: brendontucker
"""

import random 

def rolldice():
    roll = random.randint(1,100)
    if roll == 100:
        print (roll) 
        print( 'You lost')
        return False
    elif roll <= 50:
        print (roll) 
        print ('You lost')
        return False
    elif 100 > roll >= 51:
        print (roll) 
        print ('You win')
        return True
        
def simpleBettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    currentWager = 0
    
    while currentWager < wager_count:
        if rolldice(): #if True is resturned this will execute
            value += wager
            
        else:
            value =- wager
            
        currentWager += 1
        print('Funds:', value)
        
simpleBettor(10000, 100,100)
       
        
        
        
        
        
        
        
        
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
