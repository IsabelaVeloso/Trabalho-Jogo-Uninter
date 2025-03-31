import pygame
import sys
import random
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY
from code.const import COLOR_DARK_GREEN, COLOR_ORANGE
from code.entitymediator import EntityMediator
from code.player import Player
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.enemy import Enemy
from code.Score import Score # teste

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.start_time = pygame.time.get_ticks()  # Marca o tempo inicial do jogo
        self.name = name
        self.game_mode = game_mode  
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Fundopt'))
        self.enemy_count = 0  # Contador de inimigos
        self.enemy_generation_time = 0  # Tempo para geração de inimigos
        self.last_enemy_x = WIN_WIDTH  # Inicia com a posição x inicial do primeiro inimigo
        
        if game_mode == MENU_OPTION[0]:  # opção do menu que aparece o player 1 [0]
            self.entity_list.append(EntityFactory.get_entity('Player1'))
        elif game_mode in [MENU_OPTION[1]]:  # opção do menu que aparece o player 2 [1]
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        
        self.set_random_enemy_timer()

    def set_random_enemy_timer(self):
        # Tempo aleatório entre 1.5s e 4s
        self.enemy_generation_time = pygame.time.get_ticks() + random.randint(1500, 4000)
        
    # Método que verifica se o jogador perdeu
    def check_player_loss(self):
        player = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)
        enemies = [ent for ent in self.entity_list if isinstance(ent, Enemy)]

        if player:
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):  # Verifica colisão com qualquer inimigo
                    return True  # Jogador perdeu
        return False

    def display_game_over(self):
        # Exibe "YOU LOSE" por 1 segundo antes de ir para a tela de pontuação
        font = pygame.font.SysFont("aharoni kalin", 100)
        text = font.render("YOU LOSE", True, COLOR_DARK_GREEN)
        text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.window.blit(text, text_rect)
        pygame.display.flip()

        pygame.time.wait(1000)  # Exibe por 1 segundo antes de ir para a tela de pontuação
        
        # Depois de "YOU LOSE", chama o método de salvar a pontuação
        player_score = [EntityMediator.give_score()]  # Obtém o score
        score_screen = Score(self.window)
        score_screen.save(self.game_mode, player_score)

    def run(self):
        pygame.mixer_music.load('./asset/Level.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela a cada frame

            # Calcula o tempo de jogo em segundos e milissegundos
            elapsed_time_ms = pygame.time.get_ticks() - self.start_time
            elapsed_seconds = elapsed_time_ms // 1000  # Segundos inteiros
            elapsed_milliseconds = elapsed_time_ms % 1000  # Milissegundos restantes

            # Atualiza o tempo de sobrevivência no EntityMediator
            EntityMediator.survival_time = elapsed_seconds

            events = pygame.event.get()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                
                if isinstance(ent, Player):
                    ent.move(events)
                    ent.attack(events)
                else:
                    ent.move()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Gerar inimigos com tempo aleatório
                if pygame.time.get_ticks() > self.enemy_generation_time:
                    if self.enemy_count < 3:
                        distance_min = 200
                        enemy_x = self.last_enemy_x + distance_min + random.randint(100, 200)
                        if enemy_x > WIN_WIDTH:
                            enemy_x = WIN_WIDTH

                        enemy_height = WIN_HEIGHT - 100

                        if self.game_mode == MENU_OPTION[0]:
                            new_enemy = EntityFactory.get_entity('Enemy')
                        elif self.game_mode == MENU_OPTION[1]:
                            new_enemy = EntityFactory.get_entity('Enemy2')

                        new_enemy.rect.x = enemy_x
                        new_enemy.rect.y = enemy_height

                        self.entity_list.append(new_enemy)
                        self.enemy_count += 1

                        self.last_enemy_x = new_enemy.rect.x

                        self.set_random_enemy_timer()

            self.level_text(
                text_size=14, 
                text=f'Tempo sobrevivido: {elapsed_seconds}.{elapsed_milliseconds:03d}s',
                text_color=COLOR_DARK_GREEN, 
                text_pos=(10, 5)
            )

            score = EntityMediator.give_score()
            self.level_text(
                text_size=14,
                text=f'Score: {score}s',
                text_color=COLOR_DARK_GREEN,
                text_pos=(10, 15)
            )
            
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # Se o jogador perdeu, chama o game over
            if self.check_player_loss():
                self.display_game_over()
                return None

    # Definições do texto
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="aharoni kalin", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
 