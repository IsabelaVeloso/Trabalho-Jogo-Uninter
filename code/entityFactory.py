#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH

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