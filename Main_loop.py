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

def main():
    #Run until quit
    pygame.init()
    
    running = True
    global screen
    screen.fill(black)
    CLOCK = pygame.time.Clock()
    while running:
        draw_grid()
        for event in pygame.event.get():
            if event.type == K_ESCAPE:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
        
        
        
        pygame.display.update()
    screen.fill(black)
    
    pygame.quit()
    
main()