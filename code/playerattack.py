from code.entity import Entity
from code.const import ENTITY_SPEED
from code.entityFactory import EntityFactory
import pygame

class PlayerAttack(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        pass
