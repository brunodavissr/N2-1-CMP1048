import pygame


def x_imagem(imagem):
    return (500 - imagem.get_width()) // 2


def y_imagem(imagem):
    return (600 - imagem.get_height()) // 2


def carregar_imagem(caminho, largura, altura):
    imagem = pygame.transform.scale(
        pygame.image.load(caminho).convert(), (largura, altura)
    )
    imagem.set_colorkey("Black")
    return imagem
