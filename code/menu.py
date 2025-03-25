#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu_fundo.png')
        self.rect = self.surf.get_rect(center=(window.get_width() // 2, window.get_height() // 2))  # Centraliza a imagem

    def run(self):
        self.window.blit(self.surf, self.rect)  
        pygame.display.flip()

