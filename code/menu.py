#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu_fundo.png')
        self.rect = self.surf.get_rect(center=(window.get_width() // 2, window.get_height() // 2))  # Centraliza a imagem

    def run(self):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)  
            pygame.display.flip()
            
            #Checar eventos do pygame
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit() #Fechar a janela do jogo
                   quit() #Fechar o jogo


