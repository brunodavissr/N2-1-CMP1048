import os

import pygame

from player import Player
from funcoes import *

caminho_imagens = f"{os.getcwd()}/imagens"


class Commando(Player):
    def __init__(
        self,
        x=215,
        y=300,
        velocidade=4,
        imagem=carregar_imagem(f"{caminho_imagens}/Ship_3.png", 60, 60),
        vida=15,
        imagem_projetil=carregar_imagem(f"{caminho_imagens}/lazer_vermelho.png", 6, 12),
        dano=3,
    ):
        super().__init__(x, y, velocidade, imagem, vida, imagem_projetil, dano)
