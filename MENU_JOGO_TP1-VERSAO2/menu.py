import pygame
import os
import sys

pygame.init()

caminho_imagens = f"{os.getcwd()}/imagens"

LARGURA_TELA = 500
ALTURA_TELA = 600

def carregar_imagem(caminho, largura, altura):
    imagem = pygame.transform.scale(
        pygame.image.load(caminho).convert(), (largura, altura)
    )
    imagem.set_colorkey((0, 0, 0))
    return imagem

def x_imagem(imagem):
    return (LARGURA_TELA - imagem.get_width()) // 2

def y_imagem(imagem):
    return (ALTURA_TELA - imagem.get_height()) // 2

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Menu Principal")
tela_de_fundo = carregar_imagem(f"{caminho_imagens}/espaco.png", 500, 600)

botao_jogar = carregar_imagem(f"{caminho_imagens}/botao_jogar.png",375,75)
botao_jogar_hover = carregar_imagem(f"{caminho_imagens}/botao_jogar_hover.png",375,75)
botao_sair = carregar_imagem(f"{caminho_imagens}/botao_sair.png",375,75)
botao_sair_hover = carregar_imagem(f"{caminho_imagens}/botao_sair_hover.png",375,75)

nave1 = carregar_imagem(f"{caminho_imagens}/Ship_1.png",100,100)
nave2 = carregar_imagem(f"{caminho_imagens}/Ship_2.png",100,100)
nave3 = carregar_imagem(f"{caminho_imagens}/Ship_3.png",100,100)

opcao_ativa = "Jogar"

run = True

while run:
    tela.blit(tela_de_fundo, (0, 0))
    tela.blit(botao_jogar, (x_imagem(botao_jogar),200))
    tela.blit(botao_sair, (x_imagem(botao_sair),350))

    if opcao_ativa == "Jogar":
        tela.blit(botao_jogar_hover, (x_imagem(botao_jogar_hover),200))
    else:
        tela.blit(botao_sair_hover, (x_imagem(botao_sair_hover),350))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and opcao_ativa == "Sair":
                opcao_ativa = "Jogar"
            elif event.key == pygame.K_DOWN and opcao_ativa == "Jogar":
                opcao_ativa = "Sair"
            elif event.key == pygame.K_RETURN:
                run = False
                if opcao_ativa == "Sair":
                    sys.exit()
                break
                
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

run = True

while run:
    tela.blit(tela_de_fundo, (0, 0))
    tela.blit(nave1, (x_imagem(nave1),100))
    tela.blit(nave2, (x_imagem(nave2),250))
    tela.blit(nave3, (x_imagem(nave3),400))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and opcao_ativa == "Sair":
                opcao_ativa = "Jogar"
            elif event.key == pygame.K_DOWN and opcao_ativa == "Jogar":
                opcao_ativa = "Sair"
            elif event.key == pygame.K_RETURN:
                run = False
                if opcao_ativa == "Sair":
                    sys.exit()
                break
                
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
pygame.quit()