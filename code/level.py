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

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.start_time = pygame.time.get_ticks()  # Marca o tempo inicial do jogo
        self.name = name
        self.game_mode = game_mode  
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Fundopt'))
        self.enemy_count = 0  # Contador de inimigos
        
        if game_mode == MENU_OPTION[0]:  # opção do menu que aparece o player 1 [0]
            self.entity_list.append(EntityFactory.get_entity('Player1'))
        elif game_mode in [MENU_OPTION[1]]:  # opção do menu que aparece o player 2 [1]
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        
        self.set_random_enemy_timer()

    def set_random_enemy_timer(self):
        pygame.time.set_timer(EVENT_ENEMY, random.randint(1500, 4000))  # Ritmo aleatório entre 1.5s e 4s
        
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

            # Captura todos os eventos da rodada
            events = pygame.event.get()  

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Desenha entidades
                
                if isinstance(ent, Player):
                    ent.move(events)  # Passa os eventos para capturar teclas
                    ent.attack(events)  # Passa os eventos para capturar ataques
                else:
                    ent.move()  # Outras entidades podem não precisar de eventos
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    if self.enemy_count < 3:
                        last_enemy = next((e for e in reversed(self.entity_list) if isinstance(e, Entity) and 'Enemy' in str(type(e))), None)
                        if last_enemy is None or last_enemy.rect.x < WIN_WIDTH - 200:  # Distância mínima de 200px
                            if self.game_mode == MENU_OPTION[0]:
                                self.entity_list.append(EntityFactory.get_entity('Enemy'))
                            elif self.game_mode == MENU_OPTION[1]:
                                self.entity_list.append(EntityFactory.get_entity('Enemy2'))
                            self.enemy_count += 1
                            self.set_random_enemy_timer()

            # Renderiza o tempo sobrevivido com segundos e milissegundos
            self.level_text(
                text_size=14, 
                text=f'{self.name} - Tempo sobrevivido: {elapsed_seconds}.{elapsed_milliseconds:03d}s',
                text_color=COLOR_DARK_GREEN, 
                text_pos=(10, 5)
            )

            # Exibe o score (tempo de sobrevivência)
            score = EntityMediator.give_score()  # Obtém o tempo de sobrevivência como score
            self.level_text(
                text_size=14,
                text=f'Score: {score}s',  # Exibe o score como o tempo de sobrevivência
                text_color=COLOR_DARK_GREEN,
                text_pos=(10, 15)  # Posição do score na tela
            )
            
            pygame.display.flip()

            # Verifica colisões e saúde das entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    # Definições do texto
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="aharoni kalin", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
