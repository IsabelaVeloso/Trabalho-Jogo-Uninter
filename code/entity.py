#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from abc import ABC, abstractmethod
from code.const import ENTITY_HEALTH, ENTITY_DAMAGE

class Entity(ABC): # Classe abstrata
    def __init__(self, name:str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/'+ name + '.png').convert_alpha() # Buscar imagens do fundo do asset
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    @abstractmethod
    def move(self, ):
        pass
