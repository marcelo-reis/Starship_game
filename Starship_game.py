# '''
# Criado por: Marcelo Reis
# Data: 2018.07.25
# Ultima Atualização 2018.07.26
# '''

import pygame
from pygame.locals import *
from sys import exit
# Para poder usar o método randint
from random import randint


# Algumas imagens podem possuir direitos autorais e estão aqui apenas para teste
imagem_fundo  = '/Python36-32/Starship_game-master/background02.jpg'
sprite_rocha1 = '/Python36-32/Starship_game-master/sprite_rock01_35px.png'
sprite_rocha2 = '/Python36-32/Starship_game-master/sprite_rock02_50px.png'
sprite_rocha3 = '/Python36-32/Starship_game-master/sprite_rock03_130px.png'
sprite_nave   = '/Python36-32/Starship_game-master/sprite_spaceship01.png'

# Largura e Altura da tela
largura = 640
altura  = 480
tamanho_tela = (largura, altura)

pygame.init()
tela = pygame.display.set_mode(tamanho_tela, 0, 32)

fundo  = pygame.image.load(imagem_fundo).convert()
rocha1 = pygame.image.load(sprite_rocha1).convert_alpha()
rocha2 = pygame.image.load(sprite_rocha2).convert_alpha()
rocha3 = pygame.image.load(sprite_rocha3).convert_alpha()
nave   = pygame.image.load(sprite_nave).convert_alpha()

# cria um objeto Clock(0
relogio = pygame.time.Clock()

# define a posição inical e a velocidade das rochas e da nave
speed_rocha1 = 300
pos_rocha1_x = -35
pos_rocha1_y = randint(0, altura)

speed_rocha2 = 60
pos_rocha2_x = -50
pos_rocha2_y = randint(0, altura)

speed_rocha3 = 200
pos_rocha3_x = -130
pos_rocha3_y = randint(0, altura)

speed_nave = 15
pos_nave_x = -nave.get_width()
pos_nave_y = randint(81, altura - nave.get_height())

while True:
        # fechar o jogo ao clicar no X da janela
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                exit()
        
        # posiciona as imagens na tela
        tela.blit(fundo , (0,0)                       )
        tela.blit(rocha1, (pos_rocha1_x, pos_rocha1_y))
        tela.blit(rocha2, (pos_rocha2_x, pos_rocha2_y))
        tela.blit(nave  , (pos_nave_x, pos_nave_y)    )
        tela.blit(rocha3, (pos_rocha3_x, pos_rocha3_y))

        tempo = relogio.tick()
        # transforma o tempo do tick() em segundos
        tempo_segundos = tempo / 1000.
        
        # Movimento da rocha1
        mover_rocha1 = tempo_segundos * speed_rocha1
        pos_rocha1_x -= mover_rocha1
        #if pos_rocha1_x < -35:
        if pos_rocha1_x < -rocha1.get_width():
            pos_rocha1_x = largura + rocha1.get_width()
            pos_rocha1_y = randint(0,altura)
        
        # Movimento da rocha2
        mover_rocha2 = tempo_segundos * speed_rocha2
        pos_rocha2_x -= mover_rocha2
        if pos_rocha2_x < -rocha2.get_width():
            pos_rocha2_x = largura + rocha2.get_width()
            pos_rocha2_y = randint(0,altura)
        
        # Movimento da rocha3
        mover_rocha3 = tempo_segundos * speed_rocha3
        pos_rocha3_x -= mover_rocha3
        if pos_rocha3_x < -rocha3.get_width():
            pos_rocha3_x = largura + rocha3.get_width()
            pos_rocha3_y = randint(0,altura)

        # Movimento da nave
        mover_nave = tempo_segundos * speed_nave
        pos_nave_x += mover_nave
        if pos_nave_x > largura + nave.get_width():
            pos_nave_x = -nave.get_width()
            pos_nave_y = randint(nave.get_height(),altura - nave.get_height())

        # aualiza o display    
        pygame.display.flip()
