#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.const import COLOR_DARK_GREEN, COLOR_GREEN, COLOR_ORANGE

from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.timeout = 20000 # 20 segundos
        self.name = name
        self.game_mode = game_mode  
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Fundopt'))
        
        if game_mode == MENU_OPTION[0]: # opção do menu que aparece o player 1 [0]
            self.entity_list.append(EntityFactory.get_entity('Player1'))
        elif game_mode in [MENU_OPTION[1]]: # opção do menu que aparece o player 2 [1]
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        
    def run(self, ):
        pygame.mixer_music.load('./asset/Level.wav') # Buscar áudio no asset
        pygame.mixer_music.play(-1) # Tocar em loop
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect) # Criação do retangulo e imagem
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # textos aparecem na tela (tempo, atalização e entidades)        
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', text_color=COLOR_DARK_GREEN, text_pos=(10, 5))
            pygame.display.flip()
            
        pass

# Definições do texto
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="aharoni kalin", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)        
                