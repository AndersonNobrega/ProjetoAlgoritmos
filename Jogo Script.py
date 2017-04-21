try:
    import pygame
    import random
    import csv
    import time
except ImportError:
    quit()

pygame.init()

#Listas para guarda as informações dos arquivos .csv
cidade_origem = []
cidade_destino1 = []
cidade_destino2 = []
cidade_destino3 = []
cidade_distancia1 = []
cidade_distancia2 = []
cidade_distancia3 = []
dica1 = []
dica2 = []
dica3 = []
descrição = []
nomes_femininos = []
nomes_masculinos = []
tesouros = []
lugares = ['Livraria','Aeroporto','Porto','Banco','Hotel','Embaixada','Mercado','Museu','Universidade']
flag_lugares = 0
flag_cidades = 0
lugar_1 = 0
lugar_2 = 0
lugar_3 = 0
cidade_atual = ''
cidade_d1 = ''
cidade_d2 = ''
cidade_d3 = ''

#Abre arquivo com cidades,distancias,dicas e as suas descrições
# "Cidade atual","Destino1","Distancia1","Destino2","Distancia2","Destino3","Distancia3","Dica1","Dica2","Dica3","Descrição"
with open('ARQUIVOS CSV/dicas.csv', 'r', encoding='ISO-8859-1') as dados_jogo:
    linhas_dado = csv.reader(dados_jogo)
    for linha in linhas_dado:
        cidade_origem.append(linha[0])
        cidade_destino1.append(linha[1])
        cidade_destino2.append(linha[3])
        cidade_destino3.append(linha[5])
        cidade_distancia1.append(linha[2])
        cidade_distancia2.append(linha[4])
        cidade_distancia3.append(linha[6])
        dica1.append(linha[7])
        dica2.append(linha[8])
        dica3.append(linha[9])
        descrição.append(linha[10])

#Abre arquivo dos nomes femininos
with open('ARQUIVOS CSV/nomesfemininos.csv', 'r', encoding='ISO-8859-1') as nomes1:
    nomef = csv.reader(nomes1)
    for linha in nomef:
        nomes_femininos.append(linha[0])

#Abre arquivo dos nomes masculinos
with open('ARQUIVOS CSV/nomesmasculinos.csv', 'r', encoding='ISO-8859-1') as nomes2:
    nomem = csv.reader(nomes2)
    for linha in nomem:
        nomes_masculinos.append(linha[0])

#Abre arquivo dos tesouros
with open('ARQUIVOS CSV/tesouros.csv', 'r', encoding='ISO-8859-1') as tesouro_lista:
    tesouro = csv.reader(tesouros)
    for linha in tesouro:
        tesouros.append(linha[0])

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
menu_conexões_img = pygame.image.load('assets/Menu_Conexoes.png')
menu_viajar_img = pygame.image.load('assets/Menu_Viajar.png')

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

def lugar():
    #Escolha dos lugares para a cidade atual
    global flag_lugares, lugar_1, lugar_2, lugar_3

    if flag_lugares == 0:
        while True:
            lugar_1 = random.randrange(len(lugares))
            lugar_2 = random.randrange(len(lugares))
            lugar_3 = random.randrange(len(lugares))
            if lugar_2 == lugar_1:
                lugar_2 = random.randrange(len(lugares))
            if lugar_3 == lugar_1 or lugar_3 == lugar_2:
                lugar_3 = random.randrange(len(lugares))
            else:
                flag_lugares = 1
                return lugar_1, lugar_2, lugar_3
    else:
        return lugar_1, lugar_2, lugar_3

def escolher_destinos():
    #Função para escolher destinos aleatorios

    global flag_cidades, cidade_atual, cidade_d1, cidade_d2, cidade_d3

    if flag_cidades == 0:
        cidade_o = random.randint(0,14)
        cidade_d1 = cidade_destino1[cidade_o]
        cidade_d2 = cidade_destino2[cidade_o]
        cidade_d3 = cidade_destino3[cidade_o]
        cidade_atual = cidade_origem[cidade_o]
        flag_cidades = 1
        return cidade_atual, cidade_d1, cidade_d2, cidade_d3
    else:
        return cidade_atual, cidade_d1, cidade_d2, cidade_d3

def escolher_destinos_menu():
    # Função para inserir os destinos aleatorios no menu
    cidade_atual, destino1, destino2, destino3 = escolher_destinos()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_jogo()

        resolução_jogo.blit(menu_viajar_img, (15, 435))
        botões("%s" %destino1, 50, 460, 300, 35, preto, cinza, )
        botões("%s" %destino2, 50, 495, 300, 35, preto, cinza, )
        botões("%s" %destino3, 50, 530, 300, 35, preto, cinza, )
        centralizar_texto(600, 497, 'Viajar')
        centralizar_texto(600, 532, 'Investigar')
        centralizar_texto(600, 567, 'Visitar Interpol')

        pygame.display.update()
        fps.tick(60)

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

def centralizar_texto(x, y, msg):
    #Função para centralizar texto
    superficie_texto, retangulo_texto = objetos_texto(msg, texto_pequeno)
    retangulo_texto.center = ((x, y))
    resolução_jogo.blit(superficie_texto, retangulo_texto)

def menu_conexões():
    #Mostrar os lugares que se pode ir
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_jogo()

        resolução_jogo.blit(menu_conexões_img, (25, 120))
        centralizar_texto(200, 150, '%s' %cidade_d1)
        centralizar_texto(200, 185, '%s' %cidade_d2)
        centralizar_texto(200, 220, '%s' %cidade_d3)
        centralizar_texto(600, 462, 'Conexões')
        centralizar_texto(600, 497, 'Viajar')
        centralizar_texto(600, 532, 'Investigar')
        centralizar_texto(600, 567, 'Visitar Interpol')

        pygame.display.update()
        fps.tick(60)

def menu_investigar():
    #Lugares para investigar na cidade

    indice_lugar1, indice_lugar2, indice_lugar3 = lugar()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_jogo()

        resolução_jogo.blit(menu_investigar_img, (15, 255))
        botões('%s' %(lugares[indice_lugar1]), 50, 460, 300, 35, preto, cinza, )
        botões('%s' %(lugares[indice_lugar2]), 50, 495, 300, 35, preto, cinza, )
        botões('%s' %(lugares[indice_lugar3]), 50, 530, 300, 35, preto, cinza, )
        centralizar_texto(600, 532, 'Investigar')
        centralizar_texto(600, 567, 'Visitar Interpol')

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
        botões('Ranking', 325, 300, 150, 50, preto, cinza, )
        botões('Creditos', 325, 350, 150, 50, preto, cinza, )
        botões('Sair', 325, 400, 150, 50, preto, cinza, sair_jogo)

        pygame.display.update()
        fps.tick(15)

def pausar(pause=False):
    #Menu de pausa

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_jogo()

        resolução_jogo.blit(pausar_img, (305, 190))
        botões('Continuar Jogo', 310, 197, 150, 50, preto, cinza, loop_jogo)
        botões('Salvar Jogo', 310, 247, 150, 50, preto, cinza, )
        botões('Sair do Jogo', 310, 297, 150, 50, preto, cinza, sair_jogo)

        pygame.display.update()
        fps.tick(15)

def interface_jogo():
    #Interface grafica do jogo

    resolução_jogo.blit(interface_jogo_img, (0, 0))
    botões('Conexões', 420, 445, 360, 35, preto, cinza, menu_conexões)
    botões('Viajar', 420, 480, 360, 35, preto, cinza, escolher_destinos_menu)
    botões('Investigar', 420, 515, 360, 35, preto, cinza, menu_investigar)
    botões('Visitar Interpol', 420, 550, 360, 35, preto, cinza, )

def loop_jogo():
    #Loop do jogo

    cidade_atual, destino1, destino2, destino3 = escolher_destinos()

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
        centralizar_texto(200, 40, '%s' % cidade_atual)
        dias_horas(dia, hora)
        interface_jogo()

        pygame.display.update()
        fps.tick(60)

menu_jogo()
loop_jogo()
sair_jogo()