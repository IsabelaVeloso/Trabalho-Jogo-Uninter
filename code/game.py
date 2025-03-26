#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # Padronizar as dimensões
        self.menu = Menu(self.window)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Encerrar o jogo

            self.menu.run() 
            pygame.display.update()  # Atualizar a tela

        pygame.quit()  # Encerrar o jogo
            
