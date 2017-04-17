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

resolução_jogo = pygame.display.set_mode((resolução_altura, resolução_altura))
pygame.display.set_caption('Where in the world is carmen sandiego')
relogio = pygame.time.Clock()

def sair_jogo():
    pygame.quit()
    quit()

def button(msg, x, y, w, h, ic, ac, ação=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(resolução_jogo, ac, (x, y, w, h))
        if click[0] == 1 and ação != None:
            ação()
    else:
        pygame.draw.rect(resolução_jogo, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    resolução_jogo.blit(textSurf, textRect)
