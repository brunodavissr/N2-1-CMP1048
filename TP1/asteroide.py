import os

import pygame
import random

from funcoes import *

caminho_imagens = f"{os.getcwd()}/imagens"


def determinar_imagem(numero):
    imagens = [
        f"{caminho_imagens}/asteroide1.png",
        f"{caminho_imagens}/asteroide2.png",
        f"{caminho_imagens}/asteroide3.png",
        f"{caminho_imagens}/asteroide4.png",
    ]
    return imagens[numero]


def determinar_atributos(numero):
    # vida, dano, velocidade do asteroide
    numeros = [(3, 5, 3, 60, 10), (6, 10, 2, 120, 15), (9, 20, 1, 200, 20)]
    atributos = list(numeros)
    if numero <= 50:
        return atributos[0]
    else:
        if numero <= 70:
            return atributos[1]
        else:
            return atributos[2]


class Asteroides:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.asteroides = []

    def aumentar_dificuldade(self, incr):
        self.tamanho += incr

    def gerar_asteroides(self):
        aleatorio = random.randint(4, 9) * 10
        if len(self.asteroides) < self.tamanho:
            asteroide = Asteroide(random.randint(aleatorio, 500 - aleatorio), aleatorio)
            self.asteroides.append(asteroide)

    def checar_colisao(self, player):
        for asteroide in self.asteroides:
            for projetil in player.projeteis:
                if asteroide.retangulo.colliderect(projetil):
                    asteroide.vida -= player.dano
                    player.projeteis.remove(projetil)
                    if asteroide.vida <= 0:
                        self.asteroides.remove(asteroide)
                        player.pontos += asteroide.pontos

    def desenhar_asteroides(self, tela, ALTURA):
        for asteroide in self.asteroides:
            asteroide.retangulo.y += asteroide.velocidade
            if asteroide.retangulo.y > ALTURA + asteroide.limite:
                self.asteroides.remove(asteroide)
            else:
                asteroide.desenhar(tela)


class Asteroide:
    def __init__(self, x, tamanho):
        self.x = x
        self.tamanho = tamanho
        (
            self.vida,
            self.dano,
            self.velocidade,
            self.limite,
            self.pontos,
        ) = determinar_atributos(self.tamanho)
        self.y = 0 - self.limite
        self.imagem = carregar_imagem(
            determinar_imagem(random.randint(0, 3)), self.tamanho, self.tamanho
        )
        self.retangulo = self.imagem.get_rect(midbottom=(self.x, self.y))

    def desenhar(self, tela):
        tela.blit(self.imagem, self.retangulo)
