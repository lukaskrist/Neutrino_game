# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:42:25 2022

@author: loklu
"""
import pygame


def draw_grid(state):
    '''
    Drawing the grid
    It includes the assets first, and then inserts them into rectangles
    This should be updated every frame/every update.

    Parameters
    ----------
    pos : the position of the neutrino
    state : the current state of the board. (all 10 caps -the )

    Returns
    -------
    a grid that is shown on the board

    '''
    screen = pygame.display.set_mode((1000,1000))
    team_1_cap = pygame.image.load('Assets/Ceres-Top.jpg').convert()
    team_2_cap = pygame.image.load('Assets/Ice.jpg').convert()
    neutrino = pygame.image.load('Assets/Neutrino.png').convert()
    possible = pygame.image.load('Assets/Possible.jpg').convert()
    
    white = (255,255,255)
    window_height = 1000
    window_width = 1000
    blocksize = int(1000/5)
    posi = [0,0]
    for x in range(0,window_width,blocksize):                                   #
        for y in range(0,window_height,blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(screen,white,rect,1)
            
            if state[tuple(posi)] == 3:
                screen.blit(neutrino,rect) 
            if state[tuple(posi)] == 1:
                screen.blit(team_1_cap,rect)
            if state[tuple(posi)] == 2:
                screen.blit(team_2_cap,rect)
            if state[tuple(posi)] < 0:
                screen.blit(possible,rect)
            
            
            posi[1] += 1
        posi[0] += 1
        posi[1] = 0 

    
def check_position(event):
    '''
    Checking the position of the mouse, and checking which block it is
    
    Parameters
    ----------
    event : mouse click that has a position on the board. 

    Returns
    -------
    posi : position of the block.

    '''
    window_height = 1000
    window_width = 1000
    blocksize = int(1000/5)
    posi = [0,0]
    
    for x in range(0,window_width,blocksize):                                   
        for y in range(0,window_height,blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            
            if rect.collidepoint(pygame.mouse.get_pos()):
                return posi
            posi[1] += 1
        posi[0] += 1
        posi[1] = 0
