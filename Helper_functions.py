# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:42:25 2022

@author: loklu
"""
import pygame



def draw_grid(pos,state):
    '''
    Drawing the grid, using the position of the neutrino
    and the current state of the board. 
    It includes the assets first, and then inserts them into rectangles
    This should be updated every frame/every update.
    position is not the best definition
    '''
    screen = pygame.display.set_mode((1000,1000))
    team_1_cap = pygame.image.load('Assets/Ceres-Top.jpg').convert()
    team_2_cap = pygame.image.load('Assets/Ice.jpg').convert()
    neutrino = pygame.image.load('Assets/Neutrino.png').convert()
    
    white = (255,255,255)
    window_height = 1000
    window_width = 1000
    blocksize = int(1000/5)
    
    posi = [0,0]
    for x in range(0,window_width,blocksize):                                   #
        for y in range(0,window_height,blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(screen,white,rect,1)
            
            #First draw the neutrino in the middle
            if posi == pos:
                screen.blit(neutrino,rect)            
            
            #Draw the two team's caps
            for i in range(10):
                if posi == state[i]:
                    if i < 5:
                        screen.blit(team_1_cap, rect)
                    else:
                        screen.blit(team_2_cap,rect)

            
            posi[1] += 1
        posi[0] += 1
        posi[1] = 0
            
