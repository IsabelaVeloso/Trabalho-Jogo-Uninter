#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player
from code.enemy import Enemy

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position= (0,0)):
        match entity_name:
            case 'Fundopt': 
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(name=f'Fundopt{i}', position=(0, 0)))   # Imagens de fundo 
                    list_bg.append(Background(name=f'Fundopt{i}', position=(WIN_WIDTH, 0)))  
                return list_bg    
            case 'Player1':
                return Player('Player1', (10, 230)) # Dimensão player1 na tela
            case 'Player2':
                return Player('Player2', (10, 230)) # Dimensão player2 na tela            
            case 'Enemy':
                return Enemy('Enemy', (WIN_WIDTH, 230)) # Começando antes da tela e na mesma altura do player
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH, 230)) # Começando antes da tela e na mesma altura do player
