import pygame
import random
import csv
import time

pygame.init()

resolução_largura = 800
resolução_altura = 600

preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (160, 160, 160)

texto_grande = pygame.font.Font('assets/arial.ttf', 115)
texto_médio = pygame.font.Font('assets/arial.ttf', 40)
texto_pequeno = pygame.font.Font('assets/arial.ttf', 20)

resolução_jogo = pygame.display.set_mode((resolução_altura, resolução_altura))
pygame.display.set_caption('Where in the world is carmen sandiego')
fps = pygame.time.Clock()

def sair_jogo():
    #Sair do modulo pygame e do jogo
    pygame.quit()
    quit()

def objetos_texto(texto, fonte):
    textSurface = fonte.render(texto, True, branco)
    return textSurface, textSurface.get_rect()

def botões(msg, x, y, largura, altura, cor_escura, cor_clara, ação=None):
    #Botões que vão ser usados no jogo
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + largura > mouse[0] > x and y + altura > mouse[1] > y:
        pygame.draw.rect(resolução_jogo, cor_clara, (x, y, largura, altura))
        if click[0] == 1 and ação != None:
            ação()
    else:
        pygame.draw.rect(resolução_jogo, cor_escura, (x, y, largura, altura))

    superficie_texto, retangulo_texto = objetos_texto(msg, texto_pequeno)
    retangulo_texto.center = ((x + (largura / 2)), (y + (altura / 2)))
    resolução_jogo.blit(superficie_texto, retangulo_texto)

def menu_jogo():
    #Menu principal do jogo
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

        resolução_jogo.fill(preto)
        #superficie_texto, retangulo_texto = objetos_texto('Where in the world is carmen sandiego', texto_médio)
        #retangulo_texto.center = ((resolução_largura / 2), (resolução_altura / 2))
        #resolução_jogo.blit(superficie_texto, retangulo_texto)

        botões('Novo Jogo', 250, 200, 150, 50, preto, cinza, loop_jogo)
        #botões('Carregar Jogo', 300, 250, 150, 50, preto, cinza, carregar_jogo)
        botões('Sair', 250, 300, 150, 50, preto, cinza, sair_jogo)

        pygame.display.update()
        fps.tick(15)

def loop_jogo():
    #Loop do jogo

    saiu_jogo = False

    while not saiu_jogo:

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sair_jogo()


        pygame.display.update()
        fps.tick(60)

menu_jogo()
loop_jogo()
sair_jogo()