# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:24:46 2022

@author: loklu
"""
def reward(end):
    if end == "win":
        return 1
    else:
        return -1

visited = []
def search(state,game,nnet):
    if game == "win":
        rew = reward("win")
    else:
        rew = reward("loss")
        
        
        
    if state not in visited:
        visited.add(state)
        