# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:57:01 2022

@author: Lukas
"""


import numpy as np
    
def possible_positions(state,block):
    possible = []
    if block[0] != 4 and block[1] != 4:
        if state[tuple([block[0]+1,block[1]+1])] == 0:
            possible.append([1,1])
    if block[0] != 4:
        if state[tuple([block[0]+1,block[1]+0])] == 0:
            possible.append([1,0])
    if block[1] != 4:
        if state[tuple([block[0]+0,block[1]+1])] == 0:
            possible.append([0,1])
    
    if block[0] != 0 and block[1] != 4:
        if state[tuple([block[0]-1,block[1]+1])] == 0:
            possible.append([-1,1])
    if block[0] != 4 and block[1] != 0:
        if state[tuple([block[0]+1,block[1]-1])] == 0:
            possible.append([1,-1])
    if block[0] != 0 and block[1] != 0:
        if state[tuple([block[0]-1,block[1]-1])] == 0:
            possible.append([-1,-1])
    if block[0] != 0:
        if state[tuple([block[0]-1,block[1]+0])] == 0:
            possible.append([-1,0])
    if block[1] != 0:
        if state[tuple([block[0]+0,block[1]-1])] == 0:
            possible.append([0,-1])
        
    return possible
def check_if_won(state):
    if len(possible_positions(state,np.where(state == 3))) == 0:
        return "won"
    if np.where(state == 3)[1] == 0:
        return "Player_1_won"
    if np.where(state == 3)[1] == 4:
        return"Player_2_won"
    else:
        return None

poss = [0,1,2,3,4]

def move_block(state,block,direct):
    Run = True
    block1 = [block[0],block[1]]
    i = 1
    while Run == True:
        block_pot = [block1[0]+direct[0],block1[1]+direct[1]]
        
        if block_pot[0] not in poss or block_pot[1] not in poss:
            break
        if state[tuple(block_pot)] != 0:
            Run = False
            break
        else:
            block1 = block_pot
        i = i+1
        if i > 5:
            break

    state[tuple(block1)] = state[tuple(block)][0]
    state[tuple(block)] = 0
    return state

def move_block2(state,block,direct):
    Run = True
    block1 = [block[0],block[1]]
    while Run == True:
        block_pot = [block1[0]+direct[0],block1[1]+direct[1]]
        if block_pot[0] not in poss or block_pot[1] not in poss:
            break        
        if state[tuple(block_pot)] != 0:
            Run = False
            break
        else:
            block1 = block_pot

    state[tuple(block1)] = state[tuple(block)]
    state[tuple(block)] = 0
    return state