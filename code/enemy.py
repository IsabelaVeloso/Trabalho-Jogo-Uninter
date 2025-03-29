#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH

class Enemy(Entity):
   
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.to_remove = False #teste

    def move(self, ): 
        self.rect.centerx -= ENTITY_SPEED[self.name] # Velocidade do inimigo
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
            self.to_remove = True #teste
