#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.menu import Menu
from code.level import Level
from code.Score import Score
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.const import MENU_OPTION

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # Padronizar as dimensões
        self.menu = Menu(self.window)

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                level = Level(self.window, "Nivel1", menu_return)
                level_return = level.run()
                if level_return:
                    score.save(menu_return)
                
            elif menu_return == MENU_OPTION[2]:
                score.show()

            
            elif menu_return == MENU_OPTION[3]:
                pygame.quit() # Fechar a janela do jogo
                quit() # Fechar o jogo
            else:
                pass

           
