try:
    import pygame
    import random
    import csv
    import time
except ImportError:
    quit()

pygame.init()

resolução_largura = 800
resolução_altura = 600

#Cores em RGB para ser usadas no jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (160, 160, 160)

dificuldade = 1
tentativas = 5
bandidos_capturados = 0
dia = random.randint(0, 6)
hora = random.randint(0, 23)

#Definindo fonte e as imagens a ser usadas
texto_grande = pygame.font.Font('assets/arial.ttf', 115)
texto_médio = pygame.font.Font('assets/arial.ttf', 30)
texto_pequeno = pygame.font.Font('assets/arial.ttf', 20)
menu_jogo_img = pygame.image.load('assets/Menu_do_Jogo.png')
interface_jogo_img = pygame.image.load('assets/Jogo_Interface_Principal.png')
pausar_img = pygame.image.load('assets/Pausar.png')
menu_investigar_img = pygame.image.load('assets/Menu_Investigar.png')

#Definindo resolução e framerate do jogo
resolução_jogo = pygame.display.set_mode((resolução_largura, resolução_altura))
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

def dias_horas(dia, hora):
    #Tempo utilizado no jogo

    dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
    while True:
        try:
            dia = dias[dia]
            break
        except IndexError:
            dia = 0
    if hora > 23:
        hora = 0
        dia += 1

    if hora >= 0 and hora < 12:
        superficie_texto, retangulo_texto = objetos_texto(("%s, %s a.m. " %(dia, str(hora))), texto_pequeno)
        resolução_jogo.blit(superficie_texto,  (135, 70))
    else:
        superficie_texto, retangulo_texto = objetos_texto(("%s, %s p.m. " % (dia, str(hora))), texto_pequeno)
        resolução_jogo.blit(superficie_texto, (135, 70))

def menu_investigar():
    #Lugares para investigar na cidade

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_jogo()

        resolução_jogo.blit(menu_investigar_img, (15, 255))
        botões('Lugar 1', 50, 460, 300, 35, preto, cinza, )
        botões('Lugar 2', 50, 495, 300, 35, preto, cinza, )
        botões('Lugar 3', 50, 530, 300, 35, preto, cinza, )
        superficie_texto1, retangulo_texto1 = objetos_texto('Investigar', texto_pequeno)
        retangulo_texto1.center = ((600, 532))
        resolução_jogo.blit(superficie_texto1, retangulo_texto1)
        superficie_texto2, retangulo_texto2 = objetos_texto('Visitar Interpol', texto_pequeno)
        retangulo_texto2.center = ((600, 567))
        resolução_jogo.blit(superficie_texto2, retangulo_texto2)


        pygame.display.update()
        fps.tick(60)

def menu_jogo():
    #Menu principal do jogo
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

        resolução_jogo.fill(preto)

        resolução_jogo.blit(menu_jogo_img, (0, 0))
        botões('Novo Jogo', 325, 200, 150, 50, preto, cinza, loop_jogo)
        botões('Carregar Jogo', 325, 250, 150, 50, preto, cinza, )
        botões('Sair', 325, 300, 150, 50, preto, cinza, sair_jogo)

        pygame.display.update()
        fps.tick(15)

def pausar(pause=False):
    #Menu de pausa

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

        resolução_jogo.blit(pausar_img, (305, 190))
        botões('Continuar Jogo', 310, 197, 150, 50, preto, cinza, loop_jogo)
        botões('Salvar Jogo', 310, 247, 150, 50, preto, cinza, )
        botões('Sair do Jogo', 310, 297, 150, 50, preto, cinza, sair_jogo)

        pygame.display.update()
        fps.tick(15)

def interface_jogo():
    #Interface grafica do jogo

    resolução_jogo.blit(interface_jogo_img, (0, 0))
    botões('Conexões', 420, 445, 360, 35, preto, cinza, )
    botões('Viajar', 420, 480, 360, 35, preto, cinza, )
    botões('Investigar', 420, 515, 360, 35, preto, cinza, menu_investigar)
    botões('Visitar Interpol', 420, 550, 360, 35, preto, cinza, )

def loop_jogo():
    #Loop do jogo

    saiu_jogo = False

    while not saiu_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa = True
                    pausar(pausa)

        resolução_jogo.fill(preto)
        dias_horas(dia, hora)
        interface_jogo()

        pygame.display.update()
        fps.tick(60)

menu_jogo()
loop_jogo()
sair_jogo()