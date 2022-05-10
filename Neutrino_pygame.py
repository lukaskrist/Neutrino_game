# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:57:12 2022

@author: loklu
"""

import pygame


#set up window
screen = pygame.display.set_mode((500,500))



black = (0,0,0)
white = (255,255,255)
window_height = 500
window_width = 500
def draw_grid():
    blocksize = int(500/5)
    for x in range(0,window_width,blocksize):
        for y in range(0,window_height,blocksize):
            rect = pygame.Rect(x, y, blocksize, blocksize)
            pygame.draw.rect(screen,white,rect,1)


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
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
        
        pygame.display.update()
    screen.fill(black)
    
    pygame.display.flip()
    
main()