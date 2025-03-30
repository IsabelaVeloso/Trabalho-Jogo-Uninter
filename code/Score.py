import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.const import COLOR_DARK_GREEN, COLOR_GREEN, COLOR_ORANGE, SCORE_POS
from code.const import MENU_OPTION
class Score:
    
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu_fundo.png').convert_alpha() # Buscar imagem no asset
        self.rect = self.surf.get_rect(center=(window.get_width() // 2, window.get_height() // 2))  # Centralizar a imagem
        pass
    
    def save(self, menu_return: str):
        pygame.mixer_music.load('./asset/Menu.wav') # Buscar áudio no asset
        pygame.mixer_music.play(-1) # Tocar em loop
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.score_text(48, 'x', COLOR_DARK_GREEN, SCORE_POS['Title'])
            pygame.display.flip()
            pass
    
    def show(self):
        pygame.mixer_music.load('./asset/Menu.wav') # Buscar áudio no asset
        pygame.mixer_music.play(-1) # Tocar em loop
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass
        
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="aharoni kalin", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
