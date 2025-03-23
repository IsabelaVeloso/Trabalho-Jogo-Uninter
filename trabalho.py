import pygame

print('Inicio')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Fim')

print('Inicio do loop do fechamento')
while True:
    #Checar eventos do pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Fechar a janela do jogo
            quit() #Fechar o jogo