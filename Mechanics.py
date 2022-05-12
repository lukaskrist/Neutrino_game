# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:57:01 2022

@author: loklu
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
            state[i] = [0,i]
            state[i+5] = [4,i]
    
def possible_positions(pos,state):
    possible = []
    if pos+[1,1] != state.any:
        possible.append('UR')
    if pos+[1,0] != state.any:
        possible.append('R')
    if pos+[-1,0] != state.any:
        possible.append('DR')
    if pos+[-1,-1] != state.any:
        possible.append('DL')
    if pos+[-1,0] != state.any:
        possible.append('L')
    if pos+[-1,1] != state.any:
        possible.append('UL')
    if pos+[0,1] != state.any:
        possible.append('U')
    if pos+[0,-1] != state.any:
        possible.append('D')
    return possible