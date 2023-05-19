import pygame
import os

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
                break
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

print(f"A opcao escolhida foi {opcao_ativa}")

pygame.quit()