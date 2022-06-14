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
        
def check_if_won(state):
    if len(possible_positions(state,np.where(state == 3))) == 0:
        return "won"
    if any(state[4,:]) == 3:
        return "Player_1_won"
    if any(state[0,:]) == 3:
        return"Player_2_won"
    else:
        pass
    
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

