#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from abc import ABC, abstractmethod

class Entity(ABC): # Classe abstrata
    def __init__(self, name:str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/'+ name + '.png') # Buscar imagens do fundo do asset
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
