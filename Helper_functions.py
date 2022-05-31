# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:42:25 2022

@author: loklu
"""
import pygame



def draw_grid(pos,state):
    screen = pygame.display.set_mode((1000,1000))
    team_1_cap = pygame.image.load('Assets/Ceres-Top.jpg').convert()
    team_2_cap = pygame.image.load('Assets/Ice.jpg').convert()
    neutrino = pygame.image.load('Assets/Neutrino.png').convert()
    
    white = (255,255,255)
    window_height = 1000
    window_width = 1000
    blocksize = int(1000/5)
    
    posi = [0,0]
    for x in range(0,window_width,blocksize):
        for y in range(0,window_height,blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(screen,white,rect,1)
            if posi == any(state[0:5]):
                screen.blit(team_1_cap,rect)
            if posi == any(state[5:-1]):
                screen.blit(team_2_cap,rect)
            if posi == pos:
                screen.blit(neutrino,rect)
            
            posi[1] += 1
        posi[0] += 1
        posi[1] = 0
            
            
