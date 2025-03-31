import pygame
import sys
import datetime
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.const import COLOR_DARK_GREEN, COLOR_GREEN, COLOR_ORANGE, SCORE_POS
from code.const import MENU_OPTION
from code.DBProxy import DBProxy

class Score:
    
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu_fundo.png').convert_alpha()  # Buscar imagem no asset
        self.rect = self.surf.get_rect(center=(window.get_width() // 2, window.get_height() // 2))  # Centralizar a imagem
        self.start_time = pygame.time.get_ticks()  # Captura o tempo de início (em milissegundos)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Menu.wav')  # Buscar áudio no asset
        pygame.mixer_music.play(-1)  # Tocar em loop
        self.window.blit(source=self.surf, dest=self.rect)
        db_proxy = DBProxy('DBScore')  # Conectar com banco de dados
        name = ''  # Variável para armazenar o nome do jogador

        while True:
            self.score_text(30, 'Score', COLOR_DARK_GREEN, SCORE_POS['Title'])  # Tela do score e texto que aparece
            
            if game_mode == MENU_OPTION[0]:  # Nível fácil
                text = 'Coloque seu nome (4 caracteres):'

            elif game_mode == MENU_OPTION[1]:  # Nível difícil
                text = 'Coloque seu nome (4 caracteres):'

            self.score_text(20, text, COLOR_GREEN, SCORE_POS['EnterName'])
            
            for event in pygame.event.get():  # Verificando eventos
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    # Salvar o nome quando pressionar Enter e o nome tiver 4 caracteres
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        # Calcula o tempo de jogo como o score (em segundos)
                        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000  # Tempo em segundos
                        score = int(elapsed_time)  # Define o score como o tempo decorrido
                        score_dict = {'name': name, 'score': score, 'date': get_formatted_date()}
                        try:
                            db_proxy.save(score_dict)  # Salva o score no banco de dados
                            self.show()
                            return
                            print(f'Dados a salvar: {score_dict}')  # Para depuração
                        except Exception as e:
                            print(f"Erro ao salvar no banco de dados: {e}")
                    elif len(name) < 4:
                        name += event.unicode  # Adiciona o caractere ao nome
        
            # Renderizar o nome digitado
            self.score_text(20, name, COLOR_ORANGE, SCORE_POS['Name'])  # Exibe o nome atual digitado
            # Redesenha a tela após os eventos
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/Menu.wav')  # Buscar áudio no asset
        pygame.mixer_music.play(-1)  # Tocar em loop
        self.window.blit(source=self.surf, dest=self.rect)
        
        # Títulos das colunas com alinhamento
        self.score_text(30, 'TOP 10 SCORE', COLOR_GREEN, SCORE_POS['Title'])
        self.score_text(23, 'NAME           SCORE              DATE        ', COLOR_DARK_GREEN, (SCORE_POS['Label'][0], SCORE_POS['Label'][1]))

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        # Posição inicial para o primeiro score
        y_offset = SCORE_POS['Label'][1] + 40  # Ajuste do espaçamento entre os títulos e os scores

        for player_score in list_score:
            id_, name, score, date = player_score

            # Alinhar nome na coluna de nomes, pontuação na coluna de pontuação e data na coluna de data
            self.score_text(20, name, COLOR_DARK_GREEN, (SCORE_POS['NameColumn'][0], y_offset))  # Nome
            self.score_text(20, f'{score:05d}', COLOR_DARK_GREEN, (SCORE_POS['ScoreColumn'][0], y_offset))  # Pontuação
            self.score_text(20, date, COLOR_DARK_GREEN, (SCORE_POS['DateColumn'][0], y_offset))  # Data
            
            # Aumenta a distância para a próxima linha
            y_offset += 20  # Mantém o espaçamento de 40 pixels entre as linhas

        while True:
            for event in pygame.event.get():  # X para sair
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()



    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="calibri", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

        
def get_formatted_date():
    current_datetime = datetime.datetime.now()  # Corrigido para "datetime.datetime"
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"