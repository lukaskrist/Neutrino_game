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
screen = pygame.display.set_mode((1000,1000))
turn = "player_1_1"
black = (0,0,0)
from Helper_functions import *
from Mechanics import *

def main():
    #Run until quit
    pygame.init()

    running = True
    global screen, turn
    pygame.display.init()
    screen.fill(black)
    #CLOCK = pygame.time.Clock()
    pos,state = start()
    
    
    
    while running:
        draw_grid(pos,state)
        for event in pygame.event.get():
            
            ###
            if event.type == K_ESCAPE:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
            
            ###
            if turn == "player_1_1":
                a = check_if_won(pos, state)
                if a == "won":
                    running = False
                    winner = "player_2"
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    pos_click = check_position(event)
                    for possible in possible_positions(pos, state):
                        if possible == pos_click:
                            pos = possible
                            
                            turn = "player_1_2"
                            continue
                        
                #turn = "player_2"
            if turn == "player_1_2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    turn = "player_2_1"

            if turn == "player_2_1":
                a = check_if_won(pos, state)
                if a == "won":
                    running = False
                    winner = "player_1"
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    pos_click = check_position(event)
                    
                    for possible in possible_positions(pos, state):
                        if possible == pos_click:
                            pos = possible
                            
                            turn = "player_1_2"
   
                    
            
            if turn == "player_2_2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    turn = "player_1_1"

        
        pygame.display.update()
    screen.fill(black)
    
    pygame.quit()
    
main()