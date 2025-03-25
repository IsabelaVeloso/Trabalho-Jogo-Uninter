#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))

    def run(self):
       print('Inicio')
       print('Fim')
       print('Inicio do loop do fechamento')
       while True:
           menu = Menu(self.window)
           menu.run
           pass
       
            #Checar eventos do pygame
            #for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #       pygame.quit() #Fechar a janela do jogo
            #       quit() #Fechar o jogo