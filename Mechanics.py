# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:57:01 2022

@author: Lukas
"""


import pygame
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
    if any(state[4,:]) == 3:
        return "Player_1_won"
    if any(state[0,:]) == 3:
        return"Player_2_won"
    else:
        pass

def move_block(state,block,direct):
    Run = True
    block1 = [block[0]+direct[0],block[1]+direct[1]]
    while Run == True:
        block_pot = [block1[0]+direct[0],block1[1]+direct[1]]
        print(block_pot)
        if state[tuple(block_pot)] != 0:
            Run = False
            break
        if block_pot[0][0] == 4 or block_pot[1][0] == 4:
            block1 = block_pot
            Run = False
            break
        if block_pot[0][0] == 0 or block_pot[1][0] == 0:
            block1 = block_pot
            Run = False
            break
        else:
            block1 = block_pot
    state[tuple(block1)] = state[tuple(block)][0]
    state[tuple(block)] = 0
    return state

def move_block2(state,block,direct):
    Run = True
    block1 = [block[0]+direct[0],block[1]+direct[1]]
    while Run == True:
        block_pot = [block1[0]+direct[0],block1[1]+direct[1]]
        print(block_pot)
        if state[tuple(block_pot)] != 0:
            Run = False
            break
        if block_pot[0] == 4 or block_pot[1] == 4:
            block1 = block_pot
            Run = False
            break
        if block_pot[0] == 0 or block_pot[1] == 0:
            block1 = block_pot
            Run = False
            break
        else:
            block1 = block_pot
    state[tuple(block1)] = state[tuple(block)]
    state[tuple(block)] = 0
    return state