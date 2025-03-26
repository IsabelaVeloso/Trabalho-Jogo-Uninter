import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.const import COLOR_DARK_GREEN, COLOR_GREEN, COLOR_ORANGE
from code.const import MENU_OPTION

class Menu:  # Aplicar imagem
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu_fundo.png') # Buscar imagem no asset
        self.rect = self.surf.get_rect(center=(window.get_width() // 2, window.get_height() // 2))  # Centralizar a imagem

    def run(self): # Aplicar áudio
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.wav') # Buscar áudio no asset
        pygame.mixer_music.play(-1) # Tocar em loop
       
       # Tela do menu
        while True:
            self.window.blit(self.surf, self.rect) 
            self.menu_text(text_size=80, text="WAR OF THE", text_color=(COLOR_DARK_GREEN), text_center_pos=(WIN_WIDTH / 2, 70))
            self.menu_text(text_size=80, text="OGRES", text_color=(COLOR_DARK_GREEN), text_center_pos=(WIN_WIDTH / 2, 120))
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=28, text=MENU_OPTION[i], text_color=(COLOR_ORANGE), text_center_pos=(WIN_WIDTH / 2, 200 + 28 * i))
                else:
                    self.menu_text(text_size=28, text=MENU_OPTION[i], text_color=(COLOR_GREEN), text_center_pos=(WIN_WIDTH / 2, 200 + 28 * i))
            pygame.display.flip()
                
        # Checar eventos do pygame  
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit() # Fechar a janela do jogo
                   quit() # Fechar o jogo
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # Seta descendo
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                            
                    if event.key == pygame.K_UP: # Seta subindo
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1              
   
                    if event.key == pygame.K_RETURN: # Enter
                        return MENU_OPTION[menu_option]
                                        

                   
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="aharoni kalin", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

