# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:57:12 2022

@author: loklu
"""

import pygame
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#set up window
screen = pygame.display.set_mode((500,500))

black = (0,0,0)
from Helper_functions import *
from Mechanics import *

def main():
    #Run until quit
    pygame.init()
    
    running = True
    global screen
    pygame.display.init()
    screen.fill(black)
    CLOCK = pygame.time.Clock()
    pos,state = start()
    team_1_cap = pygame.image.load('Assets/Ceres-Top.jpg').convert()
    team_2_cap = pygame.image.load('Assets/Ice.jpg').convert()
    while running:
        draw_grid()
        for event in pygame.event.get():
            if event.type == K_ESCAPE:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
            if event.type == KEYDOWN:                                           #Hvis man vælger en event KEYDOWN, checker den mulige positioner
                possible_positions(pos, state)                                  #Skal ændres til tryk på feltet
                
            check_if_won(pos, state)
        
        
        
        pygame.display.update()
    screen.fill(black)
    
    pygame.quit()
    
main()