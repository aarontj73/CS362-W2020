# -*- coding: utf-8 -*-
"""
author: johnsaar (Aaron Johnson)
date: 1/15/20
"""
import testUtility
import Dominion
import random
from collections import defaultdict


##########################
# Base game data to edit #
##########################

player_names = testUtility.getPlayerNames()

nV = testUtility.setNumVictory(player_names)

nC = -10 + 10 * len(player_names)

box= testUtility.getBoxes(nV)

supply_order = testUtility.setSupplyOrder()

####################
# Initializes game #
####################
supply, players = testUtility.initializeData(player_names, nV, nC, box, supply_order)

#initialize the trash
trash = []


#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)