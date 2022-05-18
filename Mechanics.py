# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:57:01 2022

@author: Lukas
"""


import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()

def start(pos = None,state = None):
    if pos == None:
        pos = [2,2]
    
    if state == None:
        state = []
        for i in range(5):
            state.append([0,i])
            state.append([4,i])
    return pos,state
    
def possible_positions(pos,state):
    possible = []
    if pos+[1,1] != any(state):
        possible.append([1,1])
    if pos+[1,0] != any(state):
        possible.append([1,0])
    if pos+[-1,0] != any(state):
        possible.append([-1,0])
    if pos+[-1,-1] != any(state):
        possible.append([-1,-1])
    if pos+[-1,0] != any(state):
        possible.append([-1,0])
    if pos+[-1,1] != any(state):
        possible.append([-1,1])
    if pos+[0,1] != any(state):
        possible.append([0,1])
    if pos+[0,-1] != any(state):
        possible.append([0,-1])
    return possible

def check_if_won(pos,state):
    if len(possible_positions(pos, state)) == 0:
        return "won"
    if pos[1] == 4 or pos[1] == 0:
        return "won"
    else:
        pass