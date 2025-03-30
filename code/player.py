import pygame
from code.entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.is_jumping = False
        self.jump_speed = -10  # Velocidade inicial do pulo (negativo para subir)
        self.gravity = 0.5  # Efeito da gravidade
        self.velocity_y = 0  # Velocidade vertical do player
        self.ground_level = position[1]  # Guarda a posição inicial
        self.default_sprite = name  # Guarda o sprite original

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
                    self.velocity_y = self.jump_speed  # Aplica força para cima

        # Aplicando gravidade ao pulo
        if self.is_jumping:
            self.velocity_y += self.gravity  # Aumenta a velocidade descendente
            self.rect.y += self.velocity_y

            # Se tocar o chão, para de cair
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