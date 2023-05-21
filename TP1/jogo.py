import os
import sys

import time
import pygame

pygame.init()

# Configurações e atalhos
LARGURA, ALTURA = (500, 600)
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Projeto TP1")
clock = pygame.time.Clock()
fonte = pygame.font.Font(f"{os.getcwd()}/fontes/Pixeltype.ttf", 50)
caminho_imagens = f"{os.getcwd()}/imagens"

from funcoes import carregar_imagem
from asteroide import *
from commando import Commando
from hunter import Hunter
from carrier import Carrier


class Jogo:
    def __init__(self):
        self.player = Commando()
        self.tela_de_fundo = carregar_imagem(f"{caminho_imagens}/espaco.png", 500, 600)
        self.asteroides = Asteroides(4)
        self.tempo_atual = time.time()

    def exibir_menu_principal(self):
        botao_jogar = carregar_imagem(
            os.path.join(caminho_imagens, "botao_jogar.png"), 375, 75
        )
        botao_jogar_hover = carregar_imagem(
            os.path.join(caminho_imagens, "botao_jogar_hover.png"), 375, 75
        )
        botao_sair = carregar_imagem(
            os.path.join(caminho_imagens, "botao_sair.png"), 375, 75
        )
        botao_sair_hover = carregar_imagem(
            os.path.join(caminho_imagens, "botao_sair_hover.png"), 375, 75
        )

        opcoes = {botao_jogar : (botao_jogar_hover, 200), botao_sair : (botao_sair_hover, 350)}
        opcao_ativa = botao_jogar
        rodando = True

        while rodando:
            tela.blit(self.tela_de_fundo, (0, 0))
            tela.blit(botao_jogar, (x_imagem(botao_jogar), 200))
            tela.blit(botao_sair, (x_imagem(botao_sair), 350))

            tela.blit(opcoes[opcao_ativa][0], (x_imagem(opcoes[opcao_ativa][0]), opcoes[opcao_ativa][1]))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and opcao_ativa == botao_sair:
                        opcao_ativa = botao_jogar
                    elif event.key == pygame.K_DOWN and opcao_ativa == botao_jogar:
                        opcao_ativa = botao_sair
                    elif event.key == pygame.K_RETURN:
                        rodando = False
                        if opcao_ativa == botao_sair:
                            pygame.quit()
                            sys.exit()
                        break
            pygame.display.update()

    def exibir_menu_naves(self):
        naves = []
        alpha_value = 128

        for i in range(1, 4):
            nome_arquivo = f"Ship_{i}.png"
            nave = carregar_imagem(os.path.join(caminho_imagens, nome_arquivo), 100, 100)
            nave.set_alpha(alpha_value)
            naves.append(nave)
        nave_selecionada = 0

        rodando = True
        while rodando:
            tela.blit(self.tela_de_fundo, (0, 0))
            retangulo = pygame.Rect(80, 40, 350, 500)
            pygame.draw.rect(tela, "Black", retangulo)

            titulo = fonte.render("Escolha sua nave", True, (255, 255, 255))
            tela.blit(titulo, (120, 60))

            atributos = [
                {"ataque": "6", "vida": "10", "velocidade": "5"},
                {"ataque": "4", "vida": "25", "velocidade": "3"},
                {"ataque": "5", "vida": "15", "velocidade": "4"}
            ]

            j = 0
            for i in range(100, 550, 150):
                tela.blit(naves[j], (x_imagem(naves[j]) - 100, i))

                textos = [
                    fonte.render(f"Ataque: {atributos[j]['ataque']}", True, (255, 255, 255)),
                    fonte.render(f"Vida: {atributos[j]['vida']}", True, (255, 255, 255)),
                    fonte.render(f"Velocidade: {atributos[j]['velocidade']}", True, (255, 255, 255))
                ]

                for k in range(3):
                    tela.blit(textos[k], (x_imagem(naves[j]) + naves[j].get_width() - 90, 120 + 150 * j + 30 * k))

                j += 1
            naves[nave_selecionada].set_alpha(255)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if nave_selecionada > 0:
                            naves[nave_selecionada].set_alpha(128)
                            nave_selecionada -= 1
                    elif event.key == pygame.K_DOWN:
                        if nave_selecionada < len(naves) - 1:
                            naves[nave_selecionada].set_alpha(128)
                            nave_selecionada += 1
                    elif event.key == pygame.K_RETURN:
                        if nave_selecionada == 0:
                            self.player = Hunter()
                        elif nave_selecionada == 1:
                            self.player = Carrier()
                        elif nave_selecionada == 2:
                            self.player = Commando()
                        rodando = False
            pygame.display.update()

    def exibir_menu_interno(self):
        rodando = True
        tela_de_fundo_desfocada = carregar_imagem(os.path.join(caminho_imagens, "espaco_desfocado.png"), 500, 600)
        botao_retomar = carregar_imagem(os.path.join(caminho_imagens, "botao_retomar.png"), 375, 75)
        botao_retomar_hover = carregar_imagem(os.path.join(caminho_imagens, "botao_retomar_hover.png"), 375, 75)
        botao_sair_para_menu = carregar_imagem(os.path.join(caminho_imagens, "botao_sair_para_menu.png"), 375, 75)
        botao_sair_para_menu_hover = carregar_imagem(os.path.join(caminho_imagens, "botao_sair_para_menu_hover.png"), 375, 75)

        opcoes = {botao_retomar : (botao_retomar_hover, 200), botao_sair_para_menu : (botao_sair_para_menu_hover, 350)}
        opcao_ativa = botao_retomar
        while(rodando):
            tela.blit(tela_de_fundo_desfocada, (0, 0))
            tela.blit(botao_retomar, (x_imagem(botao_retomar), 200))
            tela.blit(botao_sair_para_menu, (x_imagem(botao_sair_para_menu), 350))

            tela.blit(opcoes[opcao_ativa][0], (x_imagem(opcoes[opcao_ativa][0]), opcoes[opcao_ativa][1]))
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        rodando = False
                        break
                    elif event.key == pygame.K_UP and opcao_ativa == botao_sair_para_menu:
                        opcao_ativa = botao_retomar
                    elif event.key == pygame.K_DOWN and opcao_ativa == botao_retomar:
                        opcao_ativa = botao_sair_para_menu
                    elif event.key == pygame.K_RETURN:
                        if opcao_ativa == botao_retomar:
                            return 0
                        return 1

            pygame.display.update()

    def apertou_sair_para_menu(self):
        return self.exibir_menu_interno()

    def gameplay(self):
        while True:

            if time.time() - self.tempo_atual > 15:
                self.asteroides.aumentar_dificuldade(1)
                self.tempo_atual = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.apertou_sair_para_menu():
                        return False

                self.player.atacar(event)

            tela.blit(self.tela_de_fundo, (0, 0))

            self.asteroides.gerar_asteroides()
            self.asteroides.desenhar_asteroides(tela, ALTURA)
            self.asteroides.checar_colisao(self.player)

            self.player.controles()
            self.player.desenhar_objeto(tela)
            self.player.checar_colisao(self.asteroides)

            if self.player.vida <= 0:
                break

            pygame.display.update()
            clock.tick(60)
        return True

    def final_de_jogo(self):
        rodando = True

        while rodando:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        rodando = False
                        break

            tela.fill("White")

            texto = fonte.render(f"Final de Jogo", True, "Black")
            tela.blit(texto, (150, 200))

            texto = fonte.render(f"Pontos: {self.player.pontos}", True, "Black")
            tela.blit(texto, (160, 300))

            font1 = pygame.font.Font(f"{os.getcwd()}/fontes/Pixeltype.ttf", 35)
            texto = font1.render(
                f"Pressione 'Enter' para tentar novamente", True, "Black"
            )
            tela.blit(texto, (40, 500))

            pygame.display.update()
            clock.tick(60)
