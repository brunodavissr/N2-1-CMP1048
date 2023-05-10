import pygame
import sys

# inicializar o Pygame
pygame.init()

# definir as dimensões da tela
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# carregar a imagem de fundo do espaço
space_bg_image = pygame.image.load("space_bg.jpg").convert()

# carregar a imagem da nave espacial
spaceship_image = pygame.image.load("spaceship.png").convert()
spaceship_image.set_colorkey((0, 0, 0))  # definir a cor branca como transparente

# definir a posição inicial da nave espacial
spaceship_position = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]

# definir a velocidade da nave espacial
spaceship_speed = 0.25

# loop principal do jogo
while True:
    # lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # sair do loop se o usuário clicar no botão de fechar
            pygame.quit()
            sys.exit()
    
    # lidar com as teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_position[0] > 0:
        spaceship_position[0] -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_position[0] < SCREEN_WIDTH - spaceship_image.get_width():
        spaceship_position[0] += spaceship_speed
    if keys[pygame.K_UP] and spaceship_position[1] > 0:
        spaceship_position[1] -= spaceship_speed
    if keys[pygame.K_DOWN] and spaceship_position[1] < SCREEN_HEIGHT - spaceship_image.get_height():
        spaceship_position[1] += spaceship_speed

    # desenhar o fundo do espaço
    screen.blit(space_bg_image, (0, 0))

    # desenhar a imagem da nave espacial
    screen.blit(spaceship_image, spaceship_position)

    # atualizar a tela
    pygame.display.update()