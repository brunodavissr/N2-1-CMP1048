import os

import pygame

from player import Player
from funcoes import *

caminho_imagens = f"{os.getcwd()}/imagens"


class Hunter(Player):
    def __init__(
        self,
        x=215,
        y=300,
        velocidade=5,
        imagem=carregar_imagem(f"{caminho_imagens}/Ship_1.png", 60, 60),
        vida=10,
        imagem_projetil=carregar_imagem(f"{caminho_imagens}/lazer_azul.png", 6, 12),
        dano=4,
    ):
        super().__init__(x, y, velocidade, imagem, vida, imagem_projetil, dano)

    def atacar(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(self.projeteis) < 4:
                projetil = pygame.Rect(
                    self.retangulo.x + self.imagem.get_width() // 2 - 2,
                    self.retangulo.y + 10,
                    self.imagem_projetil.get_width(),
                    self.imagem_projetil.get_height(),
                )
                self.projeteis.append(projetil)
