import pygame
import os
import sys

pygame.init()

caminho_imagens = os.path.join(os.getcwd(), "imagens")

LARGURA_TELA = 500
ALTURA_TELA = 600

def carregar_imagem(caminho, largura, altura):
    imagem = pygame.transform.scale(pygame.image.load(caminho).convert_alpha(), (largura, altura))
    return imagem





def executar_jogo():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Menu Principal")

    exibir_menu_principal(tela)
    exibir_menu_naves(tela)

    print("Jogo rodaria aqui")

    pygame.quit()

executar_jogo()