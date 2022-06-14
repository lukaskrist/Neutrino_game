# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:24:46 2022

@author: loklu
"""
import pygame
import numpy as np

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

screen = pygame.display.set_mode((1000,1000))
turn = "player_1_1"
black = (0,0,0)

start = np.zeros((5,5))
start[:,4] = int(1)
start[:,0] = int(2)
start[2,2] = int(3)

from Helper_functions import *
from Mechanics import *

def main():
    pygame.init()

    running = True
    global screen, turn
    pygame.display.init()
    screen.fill(black)
    turn = "player_1_1"
    #CLOCK = pygame.time.Clock()
    state = start
    while running == True:
        draw_grid(state)
        
        for event in pygame.event.get():
            
            ###
            if event.type == K_ESCAPE:
                pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if turn == "player_1_1":
                a = check_if_won(state)
                if a == "won":
                    running = False
                    print("won")
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_click = check_position(event)
                    neutrino = np.where(state == 3)
                    for possible in possible_positions(state,neutrino):
                        if ([neutrino[0]+possible[0],neutrino[1]+possible[1]]) == pos_click:
                            state = move_block(state,neutrino,possible)
                            turn = "player_1_2"
                            continue
            if turn == "player_1_2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_click = check_position(event)
                    if state[tuple(pos_click)] == 1:
                        neutrino = pos_click
                        turn = "player_1_3"
                        continue
                    
            if turn == "player_1_3":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_click = check_position(event)
                    for possible in possible_positions(state,neutrino):
                        if ([neutrino[0]+possible[0],neutrino[1]+possible[1]]) == pos_click:
                            state = move_block2(state,neutrino,possible)
                            turn = "player_2_1"
                            continue
            if turn == "player_2_1":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_click = check_position(event)
                    neutrino = np.where(state == 3)
                    for possible in possible_positions(state,neutrino):
                        if ([neutrino[0]+possible[0],neutrino[1]+possible[1]]) == pos_click:
                            state = move_block(state,neutrino,possible)
                            turn = "player_2_2"
                            continue
            if turn == "player_2_2":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_click = check_position(event)
                    if state[tuple(pos_click)] == 2:
                        neutrino = pos_click
                        turn = "player_2_3"
                        continue
                    
            if turn == "player_2_3":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_click = check_position(event)
                    for possible in possible_positions(state,neutrino):
                        if ([neutrino[0]+possible[0],neutrino[1]+possible[1]]) == pos_click:
                            state = move_block2(state,neutrino,possible)
                            turn = "player_1_1"
                            continue
            pygame.display.update() 
            
    pygame.quit()
                    
        
        
        
main()

