try:
    import pygame
    import random
    import csv
    import time
except ImportError:
    quit()

pygame.init()

#Listas e variaveis que vão ser usadas no jogo
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
lugares = ['Livraria', 'Aeroporto', 'Porto', 'Banco', 'Hotel', 'Embaixada', 'Mercado', 'Museu', 'Universidade']
flag_lugares = 0
flag_cidades = 0
flag_hobby = 0
flag_detalhes = 0
flag_cabelo = 0
flag_carro = 0
lugar_1 = 0
lugar_2 = 0
lugar_3 = 0
cidade_atual = ''
cidade_d1 = ''
cidade_d2 = ''
cidade_d3 = ''
cidade_descrição = ''
hobby = ['Tênis', 'Música', 'Futebol', 'Escalar Montanhas', 'Nadar']
cabelos = ['Careca', 'Loiro', 'Ruivo', 'Preto']
detalhe = ['Aliança', 'Tatuagem', 'Cicatriz', 'Joia']
carro  = ['Conversivel', 'Limosine', 'Carro de corrida', 'Motocicleta']
dicas_hobby = []
dicas_cabelos = []
dicas_detalhe = []
dicas_carro = []
sexo_mandato = ''
hobby_mandato = ''
detalhes_mandato = ''
cabelo_mandato = ''
carro_mandato = ''
nome_jogador = ''
sexo_bandido = ''
hobby_bandido = ''
cabelo_bandido = ''
detalhe_bandido = ''
carro_bandido = ''

# Abre arquivo com cidades,distancias,dicas e as suas descrições
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

# Abre arquivo dos nomes masculinos
with open('ARQUIVOS CSV/nomesmasculinos.csv', 'r', encoding='ISO-8859-1') as nomes2:
    nomem = csv.reader(nomes2)
    for linha in nomem:
        nomes_masculinos.append(linha[0])

# Abre arquivo dos tesouros
with open('ARQUIVOS CSV/tesouros.csv', 'r', encoding='ISO-8859-1') as tesouro_lista:
    tesouro = csv.reader(tesouros)
    for linha in tesouro:
        tesouros.append(linha[0])

# Abre arquivo das dicas dos hobbys,cabelos,detalhes e os carros
with open('ARQUIVOS CSV/pistahobbys.csv', 'r', encoding='ISO-8859-1') as dicas_lista:
    linha_dicas = csv.reader(dicas_lista)
    for linha in linha_dicas:
        try:
            dicas_hobby.append(linha[0])
            dicas_cabelos.append(linha[1])
            dicas_detalhe.append(linha[2])
            dicas_carro.append(linha[3])
        except IndexError:
            continue

resolução_largura = 800
resolução_altura = 600

# Cores em RGB para ser usadas no jogo
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (160, 160, 160)

dificuldade = 1
tentativas = 5
bandidos_capturados = 0
dia = random.randint(0, 6)
hora = random.randint(0, 23)

# Definindo fonte e as imagens a ser usadas
texto_grande = pygame.font.Font('assets/big_noodle_titling.ttf', 115)
texto_médio = pygame.font.Font('assets/big_noodle_titling.ttf', 30)
texto_pequeno = pygame.font.Font('assets/big_noodle_titling.ttf', 20)
menu_jogo_img = pygame.image.load('assets/Menu_do_Jogo.png')
interface_jogo_img = pygame.image.load('assets/Jogo_Interface_Principal.png')
pausar_img = pygame.image.load('assets/Pausar.png')
menu_investigar_img = pygame.image.load('assets/Menu_Investigar.png')
menu_conexões_img = pygame.image.load('assets/Menu_Conexoes.png')
menu_viajar_img = pygame.image.load('assets/Menu_Viajar.png')
icone_jogo_img = pygame.image.load('assets/Jogo_Icone.png')
plano_de_fundo = pygame.image.load('assets/carmensandiego760760.png')
menu_nome_jogador_img = pygame.image.load('assets/Menu_Nome.png')
menu_detalhes_carro_cabelo_img = pygame.image.load('assets/Menu_detalhes_carro_cabelo.png')
menu_hobby_img = pygame.image.load('assets/Menu_Hobby.png')
menu_sexo_img = pygame.image.load('assets/Menu_sexo.png')
fundo_preto = pygame.image.load('assets/Esconder_mandato.png')

# Definindo resolução e framerate do jogo
resolução_jogo = pygame.display.set_mode((resolução_largura, resolução_altura))
pygame.display.set_caption('Where in the world is carmen sandiego')
pygame.display.set_icon(icone_jogo_img)
fps = pygame.time.Clock()

def sair_jogo():
    # Sair do modulo pygame e do jogo
    pygame.quit()
    quit()

def objetos_texto(texto, fonte):
    textSurface = fonte.render(texto, True, branco)
    return textSurface, textSurface.get_rect()

def botões(msg, x, y, largura, altura, cor_escura, cor_clara, ação=None):
    # Botões que vão ser usados no jogo

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

def botões_mandato(msg, x, y, largura, altura, cor_escura, cor_clara, str, variavel):
    # Botões que vão ser usados no jogo

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + largura > mouse[0] > x and y + altura > mouse[1] > y:
        pygame.draw.rect(resolução_jogo, cor_clara, (x, y, largura, altura))
        if click[0] == 1:
            variavel = str
            return variavel

    else:
        pygame.draw.rect(resolução_jogo, cor_escura, (x, y, largura, altura))

    superficie_texto, retangulo_texto = objetos_texto(msg, texto_pequeno)
    retangulo_texto.center = ((x + (largura / 2)), (y + (altura / 2)))
    resolução_jogo.blit(superficie_texto, retangulo_texto)

def lugar():
    # Escolha dos lugares para a cidade atual
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
    # Função para escolher destinos aleatorios

    global flag_cidades,cidade_descrição, cidade_atual, cidade_d1, cidade_d2, cidade_d3

    if flag_cidades == 0:
        cidade_o = random.randint(0,14)
        cidade_descrição = descrição[cidade_o]
        cidade_d1 = cidade_destino1[cidade_o]
        cidade_d2 = cidade_destino2[cidade_o]
        cidade_d3 = cidade_destino3[cidade_o]
        cidade_atual = cidade_origem[cidade_o]
        flag_cidades = 1
        return cidade_descrição, cidade_atual, cidade_d1, cidade_d2, cidade_d3
    else:
        return cidade_descrição, cidade_atual, cidade_d1, cidade_d2, cidade_d3

def recebe_nome_jogador():
    # Função que recebe e retorna o nome do jogador

    global nome_jogador
    teclas_não_adc = ['backspace', 'tab', 'space', 'escape', 'down', 'up', 'right', 'left', 'enter']

    while True:
        resolução_jogo.fill(preto)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    nome_jogador += ' '
                if event.key == pygame.K_BACKSPACE:
                    try:
                        nome_jogador = nome_jogador.rstrip(nome_jogador[-1])
                    except IndexError:
                        continue
                if event.key == pygame.K_RETURN:
                    loop_jogo()
                else:
                    letra = pygame.key.name(event.key)
                    if letra.isalpha() and letra not in teclas_não_adc:
                        nome_jogador += letra

        resolução_jogo.fill(preto)
        resolução_jogo.blit(interface_jogo_img, (0, 0))
        resolução_jogo.blit(menu_nome_jogador_img, (100, 380))
        centralizar_texto(200, 400, 'Nome do jogador:')
        centralizar_texto(200, 450, nome_jogador)
        pygame.display.update()
        fps.tick(15)

def escolher_destinos_menu():
    # Função para inserir os destinos aleatorios no menu
    cidade_descrição, cidade_atual, destino1, destino2, destino3 = escolher_destinos()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_jogo()

        resolução_jogo.blit(menu_viajar_img, (15, 435))
        botões('%s' %destino1, 50, 460, 300, 35, preto, cinza, )
        botões('%s' %destino2, 50, 495, 300, 35, preto, cinza, )
        botões('%s' %destino3, 50, 530, 300, 35, preto, cinza, )
        centralizar_texto(600, 497, 'Viajar')
        centralizar_texto(600, 532, 'Investigar')
        centralizar_texto(600, 567, 'Visitar Interpol')

        pygame.display.update()
        fps.tick(60)

def sexo_menu():
    global sexo_bandido

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sexo_bandido = ''
                    resolução_jogo.blit(fundo_preto, (190, 190))
                    mandato()

        sexo_bandido = botões_mandato('Masculino', 200, 200, 150, 50, preto, cinza, 'Masculino', sexo_bandido)
        if sexo_bandido == 'Masculino':
            break
        sexo_bandido = botões_mandato('Feminino', 200, 250, 150, 50, preto, cinza, 'Feminino', sexo_bandido)
        if sexo_bandido == 'Feminino':
            break

        resolução_jogo.blit(menu_sexo_img, (190, 190))
        pygame.display.update()
        fps.tick(60)

    resolução_jogo.blit(fundo_preto, (190, 190))
    return sexo_bandido

def hobby_menu():
    global hobby_bandido

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    hobby_bandido = ''
                    resolução_jogo.blit(fundo_preto, (190, 190))
                    mandato()

        hobby_bandido = botões_mandato('%s' %hobby[0], 200, 200, 150, 50, preto, cinza, '%s' %hobby[0], hobby_bandido)
        if hobby_bandido == hobby[0]:
            break
        hobby_bandido = botões_mandato('%s' %hobby[1], 200, 250, 150, 50, preto, cinza,'%s' %hobby[1], hobby_bandido)
        if hobby_bandido == hobby[1]:
            break
        hobby_bandido = botões_mandato('%s' %hobby[2], 200, 300, 150, 50, preto, cinza, '%s' %hobby[2], hobby_bandido)
        if hobby_bandido == hobby[2]:
            break
        hobby_bandido = botões_mandato('%s' %hobby[3], 200, 350, 150, 50, preto, cinza,'%s' %hobby[3], hobby_bandido)
        if hobby_bandido == hobby[3]:
            break
        hobby_bandido = botões_mandato('%s' %hobby[4], 200, 400, 150, 50, preto, cinza,'%s' %hobby[4], hobby_bandido)
        if hobby_bandido == hobby[4]:
            break

        resolução_jogo.blit(menu_hobby_img, (190, 190))
        pygame.display.update()
        fps.tick(60)

    resolução_jogo.blit(fundo_preto, (190, 190))
    return hobby_bandido

def detalhe_menu():
    global detalhe_bandido

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    detalhe_bandido = ''
                    resolução_jogo.blit(fundo_preto, (190, 190))
                    mandato()

        detalhe_bandido = botões_mandato('%s' %detalhe[0], 200, 200, 150, 50, preto, cinza, '%s' %detalhe[0], detalhe_bandido)
        if detalhe_bandido == detalhe[0]:
            break
        detalhe_bandido = botões_mandato('%s' %detalhe[1], 200, 250, 150, 50, preto, cinza, '%s' %detalhe[1], detalhe_bandido)
        if detalhe_bandido == detalhe[1]:
            break
        detalhe_bandido = botões_mandato('%s' %detalhe[2], 200, 300, 150, 50, preto, cinza, '%s' %detalhe[2], detalhe_bandido)
        if detalhe_bandido == detalhe[2]:
            break
        detalhe_bandido = botões_mandato('%s' %detalhe[3], 200, 350, 150, 50, preto, cinza, '%s' %detalhe[3], detalhe_bandido)
        if detalhe_bandido == detalhe[3]:
            break

        resolução_jogo.blit(menu_detalhes_carro_cabelo_img, (190, 190))
        pygame.display.update()
        fps.tick(60)

    resolução_jogo.blit(fundo_preto, (190, 190))
    return detalhe_bandido

def cabelo_menu():
    global cabelo_bandido

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cabelo_bandido = ''
                    resolução_jogo.blit(fundo_preto, (190, 190))
                    mandato()

        cabelo_bandido = botões_mandato('%s' %cabelos[0], 200, 200, 150, 50, preto, cinza, '%s' % cabelos[0], cabelo_bandido)
        if cabelo_bandido == cabelos[0]:
            break
        cabelo_bandido = botões_mandato('%s' % cabelos[1], 200, 250, 150, 50, preto, cinza, '%s' % cabelos[1], cabelo_bandido)
        if cabelo_bandido == cabelos[1]:
            break
        cabelo_bandido = botões_mandato('%s' % cabelos[2], 200, 300, 150, 50, preto, cinza, '%s' % cabelos[2], cabelo_bandido)
        if cabelo_bandido == cabelos[2]:
            break
        cabelo_bandido = botões_mandato('%s' % cabelos[3], 200, 350, 150, 50, preto, cinza, '%s' % cabelos[3], cabelo_bandido)
        if cabelo_bandido == cabelos[3]:
            break

        resolução_jogo.blit(menu_detalhes_carro_cabelo_img, (190, 190))
        pygame.display.update()
        fps.tick(60)

    resolução_jogo.blit(fundo_preto, (190, 190))
    return cabelo_bandido

def carro_menu():
    global carro_bandido

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    resolução_jogo.blit(fundo_preto, (190, 190))
                    carro_bandido = ''
                    mandato()

        carro_bandido = botões_mandato('%s' %carro[0], 200, 200, 150, 50, preto, cinza, '%s' %carro[0], carro_bandido)
        if carro_bandido == carro[0]:
            break
        carro_bandido = botões_mandato('%s' %carro[1], 200, 250, 150, 50, preto, cinza, '%s' %carro[1], carro_bandido)
        if carro_bandido == carro[1]:
            break
        carro_bandido = botões_mandato('%s' %carro[2], 200, 300, 150, 50, preto, cinza, '%s' %carro[2], carro_bandido)
        if carro_bandido == carro[2]:
            break
        carro_bandido = botões_mandato('%s' %carro[3], 200, 350, 150, 50, preto, cinza, '%s' %carro[3], carro_bandido)
        if carro_bandido == carro[3]:
            break

        resolução_jogo.blit(menu_detalhes_carro_cabelo_img, (190, 190))
        pygame.display.update()
        fps.tick(60)
    resolução_jogo.blit(fundo_preto, (190, 190))
    return carro_bandido

def mandato():
    # Menu para criação do mandato de prisão e as escolha das caracteristicas para o bandido

    global hobby_mandato, detalhes_mandato, cabelo_mandato,carro_mandato, flag_hobby, flag_detalhes,\
        flag_cabelo, flag_carro

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop_jogo()

        if flag_hobby == 0:
            hobby_mandato = hobby[(random.randrange(len(hobby)))]
        if flag_detalhes == 0:
            detalhes_mandato = detalhe[(random.randrange(len(detalhe)))]
        if flag_cabelo == 0:
            cabelo_mandato = cabelos[(random.randrange(len(cabelos)))]
        if flag_carro == 0:
            carro_mandato = carro[(random.randrange(len(carro)))]

        botões('Sexo: %s' %sexo_bandido, 420, 25, 355, 75, preto, cinza, sexo_menu)
        botões('Detalhes: %s' %detalhe_bandido, 420, 100, 355, 75, preto, cinza, detalhe_menu)
        botões('Hobby: %s' %hobby_bandido, 420, 175, 355, 75, preto, cinza, hobby_menu)
        botões('Cabelo: %s'%cabelo_bandido, 420, 250, 355, 75, preto, cinza,cabelo_menu)
        botões('Carro: %s'%carro_bandido, 420, 325, 355, 75, preto, cinza, carro_menu)

        centralizar_texto(600, 567, 'Visitar Interpol')

        flag_hobby = 1
        flag_detalhes = 1
        flag_cabelo = 1
        flag_carro = 1

        pygame.display.update()
        fps.tick(60)

def dias_horas(dia, hora):
    # Tempo utilizado no jogo

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
        centralizar_texto(200, 90, ('%s, %s a.m. ' % (dia, str(hora))))
    else:
        centralizar_texto(200, 90, ('%s, %s p.m. ' % (dia, str(hora))))

def centralizar_texto(x, y, msg):
    # Função para centralizar texto

    superficie_texto, retangulo_texto = objetos_texto(msg, texto_pequeno)
    retangulo_texto.center = ((x, y))
    resolução_jogo.blit(superficie_texto, retangulo_texto)

def menu_conexões():
    # Mostrar os lugares que se pode ir

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
    # Lugares para investigar na cidade

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
    # Menu principal do jogo
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

        resolução_jogo.fill(preto)
        resolução_jogo.blit(plano_de_fundo, (0, 0))

        resolução_jogo.blit(menu_jogo_img, (0, 0))
        botões('Novo Jogo', 325, 200, 150, 50, preto, cinza, recebe_nome_jogador)
        botões('Carregar Jogo', 325, 250, 150, 50, preto, cinza, )
        botões('Ranking', 325, 300, 150, 50, preto, cinza, )
        botões('Creditos', 325, 350, 150, 50, preto, cinza, )
        botões('Sair', 325, 400, 150, 50, preto, cinza, sair_jogo)

        pygame.display.update()
        fps.tick(15)

def pausar(pause=False):
    # Menu de pausa

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
    # Interface grafica do jogo

    resolução_jogo.blit(interface_jogo_img, (0, 0))
    botões('Conexões', 420, 445, 360, 35, preto, cinza, menu_conexões)
    botões('Viajar', 420, 480, 360, 35, preto, cinza, escolher_destinos_menu)
    botões('Investigar', 420, 515, 360, 35, preto, cinza, menu_investigar)
    botões('Visitar Interpol', 420, 550, 360, 35, preto, cinza, mandato)

def loop_jogo():
    # Loop do jogo

    cidade_descrição, cidade_atual, destino1, destino2, destino3 = escolher_destinos()

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
       # centralizar_texto(600, 50, '%s' %cidade_descrição)
        dias_horas(dia, hora)
        interface_jogo()

        pygame.display.update()
        fps.tick(60)

menu_jogo()
loop_jogo()
sair_jogo()