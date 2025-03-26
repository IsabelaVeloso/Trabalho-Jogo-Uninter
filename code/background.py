#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from code.const import WIN_WIDTH
from code.const import ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        
        
    def move(self, ): # Fundo da fase dinamico
        self.rect.centerx -= ENTITY_SPEED[self.name] # Velocidade 
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
       
