#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.menu = Menu(self.window)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Encerra o jogo

            self.menu.run()  # Renderiza o menu na tela
            pygame.display.update()  # Atualiza a tela

        pygame.quit()  # Encerra o pygame ao fechar o jogo
            
            #Checar eventos do pygame
            #for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.quit() #Fechar a janela do jogo
            #       quit() #Fechar o jogo