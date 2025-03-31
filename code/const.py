# c
COLOR_DARK_GREEN = (24,62,12)
COLOR_GREEN = (40, 105, 20)
COLOR_ORANGE = (240, 87, 56)

#e
import pygame
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Fundopt0': 0,
                 'Fundopt1': 1,
                 'Fundopt2': 2,
                 'Fundopt3': 2,
                 'Player1': 3,
                 'Player2': 7,
                 'Enemy': 4,
                 'Enemy2': 8}

ENTITY_HEALTH = {'Fundopt0': 999,
                 'Fundopt1': 999,
                 'Fundopt2': 999,
                 'Fundopt3': 999,
                 'Player1': 5,
                 'Player2': 5,
                 'Enemy': 50,
                 'Enemy2': 50}

ENTITY_DAMAGE = {'Fundopt0': 0,
                 'Fundopt1': 0,
                 'Fundopt2': 0,
                 'Fundopt3': 0,
                 'Player1': 1,
                 'Player2': 1,
                 'Enemy': 1,
                 'Enemy2': 1}


# m
MENU_OPTION = ('INICIAR NOVO JOGO - MODO FÁCIL',
               'INICIAR NOVO JOGO - MODO DÍFICIL',
               'SCORE',
               'SAIR DO JOGO')

# w
WIN_WIDTH = 576
WIN_HEIGHT = 324

# s 
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             'NameColumn': (WIN_WIDTH / 4, 90),  
             'ScoreColumn': (WIN_WIDTH / 2, 90),
             'DateColumn': (3 * WIN_WIDTH / 4, 90)}
