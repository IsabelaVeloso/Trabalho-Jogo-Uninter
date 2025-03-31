
import pygame
from code.entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.is_jumping = False
        self.jump_speed = -15  
        self.gravity = 0.9  
        self.velocity_y = 0 
        self.ground_level = position[1] 
        self.default_sprite = name  

    def move(self, events):
        keys = pygame.key.get_pressed()

        # Movimento para os lados
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        # Pulo
        if not self.is_jumping:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.is_jumping = True
                    self.velocity_y = self.jump_speed 

        if self.is_jumping:
            self.velocity_y += self.gravity  
            self.rect.y += self.velocity_y

            if self.rect.y >= self.ground_level:
                self.rect.y = self.ground_level
                self.is_jumping = False

    def attack(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                self.name = 'Player1_ataque'  # Muda para sprite de ataque
                self.is_attacking = True

            elif event.type == pygame.KEYUP and event.key == pygame.K_0:
                self.name = self.default_sprite  # Volta ao sprite original
                self.is_attacking = False
