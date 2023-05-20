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

def x_imagem(imagem):
    return (LARGURA_TELA - imagem.get_width()) // 2

def y_imagem(imagem):
    return (ALTURA_TELA - imagem.get_height()) // 2

def exibir_menu_principal(tela):
    tela_de_fundo = carregar_imagem(os.path.join(caminho_imagens, "espaco.png"), LARGURA_TELA, ALTURA_TELA)
    botao_jogar = carregar_imagem(os.path.join(caminho_imagens, "botao_jogar.png"), 375, 75)
    botao_jogar_hover = carregar_imagem(os.path.join(caminho_imagens, "botao_jogar_hover.png"), 375, 75)
    botao_sair = carregar_imagem(os.path.join(caminho_imagens, "botao_sair.png"), 375, 75)
    botao_sair_hover = carregar_imagem(os.path.join(caminho_imagens, "botao_sair_hover.png"), 375, 75)

    opcao_ativa = "Jogar"
    rodando = True

    while rodando:
        tela.blit(tela_de_fundo, (0, 0))
        tela.blit(botao_jogar, (x_imagem(botao_jogar), 200))
        tela.blit(botao_sair, (x_imagem(botao_sair), 350))

        if opcao_ativa == "Jogar":
            tela.blit(botao_jogar_hover, (x_imagem(botao_jogar_hover), 200))
        else:
            tela.blit(botao_sair_hover, (x_imagem(botao_sair_hover), 350))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and opcao_ativa == "Sair":
                    opcao_ativa = "Jogar"
                elif event.key == pygame.K_DOWN and opcao_ativa == "Jogar":
                    opcao_ativa = "Sair"
                elif event.key == pygame.K_RETURN:
                    rodando = False
                    if opcao_ativa == "Sair":
                        sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

def exibir_menu_naves(tela):
    tela_de_fundo = carregar_imagem(os.path.join(caminho_imagens, "espaco.png"), LARGURA_TELA, ALTURA_TELA)
    nave1 = carregar_imagem(os.path.join(caminho_imagens, "Ship_1.png"), 100, 100)
    nave2 = carregar_imagem(os.path.join(caminho_imagens, "Ship_2.png"), 100, 100)
    nave3 = carregar_imagem(os.path.join(caminho_imagens, "Ship_3.png"), 100, 100)

    nave1.set_alpha(128)
    nave2.set_alpha(128)
    nave3.set_alpha(128)

    fonte = pygame.font.SysFont("arial", 20)

    opcoes_nave = [nave1, nave2, nave3]
    nave_selecionada = 0

    rodando = True

    while rodando:
        tela.blit(tela_de_fundo, (0, 0))
        tela.blit(nave1, (x_imagem(nave1), 100))
        tela.blit(nave2, (x_imagem(nave2), 250))
        tela.blit(nave3, (x_imagem(nave3), 400))
        opcoes_nave[nave_selecionada].set_alpha(255)

        # Texto de atributos
        texto_ataque = fonte.render("Ataque: 10", True, (255, 255, 255))
        texto_defesa = fonte.render("Defesa: 5", True, (255, 255, 255))

        tela.blit(texto_ataque, (x_imagem(nave1) + nave1.get_width() + 10, 120))
        tela.blit(texto_defesa, (x_imagem(nave1) + nave1.get_width() + 10, 140))

        tela.blit(texto_ataque, (x_imagem(nave2) + nave2.get_width() + 10, 270))
        tela.blit(texto_defesa, (x_imagem(nave2) + nave2.get_width() + 10, 290))

        tela.blit(texto_ataque, (x_imagem(nave3) + nave3.get_width() + 10, 420))
        tela.blit(texto_defesa, (x_imagem(nave3) + nave3.get_width() + 10, 440))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if nave_selecionada > 0:
                        opcoes_nave[nave_selecionada].set_alpha(128)
                        nave_selecionada -= 1
                elif event.key == pygame.K_DOWN:
                    if nave_selecionada < len(opcoes_nave) - 1:
                        opcoes_nave[nave_selecionada].set_alpha(128)
                        nave_selecionada += 1
                elif event.key == pygame.K_RETURN:
                    rodando = False
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

def executar_jogo():
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Menu Principal")

    exibir_menu_principal(tela)
    exibir_menu_naves(tela)

    print("Jogo rodaria aqui")

    pygame.quit()

executar_jogo()
