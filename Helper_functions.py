# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:42:25 2022

@author: loklu
"""
import pygame



def draw_grid():
    screen = pygame.display.set_mode((500,500))

    
    white = (255,255,255)
    window_height = 500
    window_width = 500
    blocksize = int(500/5)
    for x in range(0,window_width,blocksize):
        for y in range(0,window_height,blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(screen,white,rect,1)