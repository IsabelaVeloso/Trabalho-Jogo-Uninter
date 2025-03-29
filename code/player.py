#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.is_jumping = False #teste
        self.jump_height = 50  # Altura do pulo
        self.ground_level = self.rect.y  # Guarda a posição inicial

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        # Movimento para os lados
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
            
         # Pular ao pressionar espaço
        if pressed_key[pygame.K_SPACE]:
            self.rect.y = self.ground_level - self.jump_height  # Mantém na altura do puloa
        else:
            self.rect.y = self.ground_level