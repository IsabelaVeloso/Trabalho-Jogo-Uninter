import pygame

class Score:
    
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu_fundo.png').convert_alpha() # Buscar imagem no asset
        self.rect = self.surf.get_rect(center=(window.get_width() // 2, window.get_height() // 2))  # Centralizar a imagem
        pass
    
    def save(self, menu_return: str):
        pass
    
    def show(self):
        pygame.mixer_music.load('./asset/Menu.wav') # Buscar áudio no asset
        pygame.mixer_music.play(-1) # Tocar em loop
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass