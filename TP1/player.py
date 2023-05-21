import os
import pygame


class Player:
    def __init__(self, x, y, velocidade, imagem, vida, imagem_projetil, dano):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.imagem = imagem
        self.vida = vida
        self.retangulo = self.imagem.get_rect(topleft=(self.x, self.y))
        self.projeteis = []
        self.velocidade_projetil = self.velocidade + 4
        self.imagem_projetil = imagem_projetil
        self.dano = dano
        self.fonte = pygame.font.Font(f"{os.getcwd()}/fontes/Pixeltype.ttf", 50)
        self.pontos = 0

    def desenhar_objeto(self, tela):
        # Desenhar projeteis na tela
        for projetil in self.projeteis:
            projetil.y -= self.velocidade_projetil
            if projetil.y < 0:
                self.projeteis.remove(projetil)
            else:
                tela.blit(self.imagem_projetil, projetil)

        # Desenhar player na tela
        tela.blit(self.imagem, self.retangulo)

        # Desenhar pontos de vida na tela
        texto = self.fonte.render(f"Vida : {self.vida}", False, "White")
        tela.blit(texto, (490 - texto.get_width(), 590 - texto.get_height()))

        # Desenhar pontuação na tela
        texto = self.fonte.render(f"Pontos: {self.pontos}", False, "White")
        tela.blit(texto, (490 - texto.get_width(), 0 + texto.get_height()))

    def controles(self):
        # Lidar com as teclas de movimentação
        tecla_pressionada = pygame.key.get_pressed()
        if (
            tecla_pressionada[pygame.K_LEFT]
        ) and self.retangulo.x - self.velocidade > 0:
            self.retangulo.x -= self.velocidade
        if (
            tecla_pressionada[pygame.K_RIGHT]
        ) and self.retangulo.x + self.velocidade < 500 - self.imagem.get_width():
            self.retangulo.x += self.velocidade
        if (tecla_pressionada[pygame.K_UP]) and self.retangulo.y > 0:
            self.retangulo.y -= self.velocidade
        if (
            tecla_pressionada[pygame.K_DOWN]
        ) and self.retangulo.y < 600 - self.imagem.get_height():
            self.retangulo.y += self.velocidade

    def atacar(self, event):
        # Disparar projeteis quando o player aperta espaço
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and len(self.projeteis) < 3:
                projetil = pygame.Rect(
                    self.retangulo.x + self.imagem.get_width() // 2 - 2,
                    self.retangulo.y + 10,
                    self.imagem_projetil.get_width(),
                    self.imagem_projetil.get_height(),
                )
                self.projeteis.append(projetil)

    def checar_colisao(self, Asteroides):
        # Checar se o player colidiu com algum asteroide
        for asteroide in Asteroides.asteroides:
            if asteroide.retangulo.colliderect(self.retangulo):
                Asteroides.asteroides.remove(asteroide)
                self.vida -= asteroide.dano
