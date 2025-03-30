import pygame
import sys
import random  # Para gerar tempos e posições aleatórias

from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY
from code.const import COLOR_DARK_GREEN, COLOR_GREEN, COLOR_ORANGE
from code.entitymediator import EntityMediator
from code.player import Player
from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.timeout = 20000  # 20 segundos
        self.name = name
        self.game_mode = game_mode  
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Fundopt'))
        self.enemy_count = 0  # Contador de inimigos
        
        if game_mode == MENU_OPTION[0]:  # opção do menu que aparece o player 1 [0]
            self.entity_list.append(EntityFactory.get_entity('Player1'))
        elif game_mode in [MENU_OPTION[1]]:  # opção do menu que aparece o player 2 [1]
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        # Variável para o tempo de aparição do próximo inimigo
        self.enemy_spawn_time = random.randint(2000, 5000)  # Aleatório entre 2 e 5 segundos
        self.last_enemy_spawn_time = pygame.time.get_ticks()  # Tempo do último spawn

    def run(self):
        pygame.mixer_music.load('./asset/Level.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        
        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela a cada frame

            # Captura todos os eventos da rodada
            events = pygame.event.get()  

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)  # Desenha entidades
                
                if isinstance(ent, Player):
                    ent.move(events)  # Passa os eventos para capturar teclas
                else:
                    ent.move()  # Outras entidades podem não precisar de eventos

            # Verifica colisões entre o jogador e os inimigos
            player = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)
            if player:
                for ent in self.entity_list:
                    if isinstance(ent, Entity) and ent != player:
                        if player.rect.colliderect(ent.rect):  # Se há colisão com um inimigo
                            self.game_over()  # Chama a função de game over

            current_time = pygame.time.get_ticks()
            
            # Verifica se o tempo de spawn do inimigo foi atingido
            if current_time - self.last_enemy_spawn_time >= self.enemy_spawn_time:
                if self.enemy_count < 3:  # Permite até 3 inimigos na tela
                    # Determina qual inimigo aparecerá dependendo do game_mode
                    if self.game_mode == MENU_OPTION[0]:
                        enemy = EntityFactory.get_entity('Enemy')  # Inimigo 1
                    elif self.game_mode == MENU_OPTION[1]:
                        enemy = EntityFactory.get_entity('Enemy2')  # Inimigo 2
                    
                    # Define a posição padronizada para o inimigo na altura Y=230
                    enemy_position = random.randint(0, WIN_WIDTH), 230  # Posição Y fixada em 230
                    
                    enemy.rect.topleft = enemy_position  # Coloca o inimigo na posição aleatória
                    
                    # Adiciona o inimigo na lista e atualiza o contador
                    self.entity_list.append(enemy)
                    self.enemy_count += 1

                    # Atualiza o tempo do último inimigo adicionado e escolhe um novo intervalo de spawn
                    self.last_enemy_spawn_time = current_time
                    self.enemy_spawn_time = random.randint(2000, 5000)  # Tempo aleatório entre 2 e 5 segundos

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Renderiza o texto na tela
            self.level_text(
                text_size=14, 
                text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',
                text_color=COLOR_DARK_GREEN, 
                text_pos=(10, 5))
            
            pygame.display.flip()

            # Verifica colisões e saúde das entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    # Função que é chamada quando o jogador perde
    def game_over(self):
        # Aqui você pode colocar um código para finalizar o jogo ou exibir uma mensagem de Game Over
        font = pygame.font.SysFont("arial", 48)
        text = font.render("GAME OVER", True, COLOR_ORANGE)
        text_rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.window.blit(text, text_rect)
        pygame.display.flip()
        
        pygame.time.wait(2000)  # Espera 2 segundos para mostrar a mensagem

        pygame.quit()
        sys.exit()

    # Definições do texto
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="aharoni kalin", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
