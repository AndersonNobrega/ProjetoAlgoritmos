try:
    import pygame
    import random
    import csv
    import time
    import os
except ImportError:
    print("Erro no import")
    quit()

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

'''Listas e variaveis que vão ser usadas no jogo'''
COORDENADA_X_TELAS_FINAIS = 205
COORDENADA_Y_TELAS_FINAIS = 150
CIDADE_ORIGEM = []
CIDADE_DESTINO1 = []
CIDADE_DESTINO2 = []
CIDADE_DESTINO3 = []
CIDADE_DISTANCIA1 = []
CIDADE_DISTANCIA2 = []
CIDADE_DISTANCIA3 = []
DICA1 = []
DICA2 = []
DICA3 = []
DESCRICAO = []
NOMES_FEMININOS = []
NOMES_MASCULINOS = []
TESOUROS = []
LUGARES = []
HOBBY = []
CABELOS = []
DETALHE = []
CARRO = []
DICAS_HOBBY = []
DICAS_CABELO = []
DICAS_DETALHE = []
DICAS_CARRO = []
PATENTES = []
DIAS = []
DICAS_VAZIA = []
flag_lugares = False
flag_cidades = False
flag_hobby = False
flag_detalhes = False
flag_cabelo = False
flag_carro = False
flag_bandido = False
flag_dica = False
flag_cidades_proxima = False
lugar_1 = 0
lugar_2 = 0
lugar_3 = 0
indice_hobby = 0
indice_detalhes = 0
indice_carro = 0
indice_cabelo = 0
cont_cidades = 0
cidade_atual = ''
cidade_d1 = ''
cidade_d2 = ''
cidade_d3 = ''
tesouro_roubado = ''
dica1_lugares = ''
dica2_lugares = ''
dica3_lugares = ''
cidade_descricao = ''
sexo_mandado = ''
hobby_mandado = ''
detalhes_mandado = ''
cabelo_mandado = ''
carro_mandado = ''
nome_jogador = ''
sexo_bandido = ''
hobby_bandido = ''
cabelo_bandido = ''
detalhe_bandido = ''
carro_bandido = ''
cidade_da_vez = ''
nome_bandido = ''
distancia_lugar = 2
caracteristicas_necessarias = 0
mandado_certo = []
mandado_bandido = []

'''Abre arquivo com cidades,distancias,dicas e as suas descrições'''
'''"Cidade atual","Destino1","Distancia1","Destino2","Distancia2","Destino3","Distancia3","Dica1","Dica2","Dica3","Descrição"'''
with open('ARQUIVOS CSV/dicas.csv', 'r', encoding='ISO-8859-1') as dados_jogo:
    linhas_dado = csv.reader(dados_jogo)
    for linha in linhas_dado:
        try:
            CIDADE_ORIGEM.append(linha[0])
            CIDADE_DESTINO1.append(linha[1])
            CIDADE_DESTINO2.append(linha[3])
            CIDADE_DESTINO3.append(linha[5])
            CIDADE_DISTANCIA1.append(linha[2])
            CIDADE_DISTANCIA2.append(linha[4])
            CIDADE_DISTANCIA3.append(linha[6])
            DICA1.append(linha[7])
            DICA2.append(linha[8])
            DICA3.append(linha[9])
            DESCRICAO.append(linha[10])
        except IndexError:
            continue

'''Abre arquivo dos nomes femininos'''
with open('ARQUIVOS CSV/nomesfemininos.csv', 'r', encoding='ISO-8859-1') as nomes1:
    nomef = csv.reader(nomes1)
    for linha in nomef:
        try:
            NOMES_FEMININOS.append(linha[0])
        except IndexError:
            continue

'''Abre arquivo dos nomes masculinos'''
with open('ARQUIVOS CSV/nomesmasculinos.csv', 'r', encoding='ISO-8859-1') as nomes2:
    nomem = csv.reader(nomes2)
    for linha in nomem:
        try:
            NOMES_MASCULINOS.append(linha[0])
        except IndexError:
            continue

'''Abre arquivo dos tesouros'''
with open('ARQUIVOS CSV/tesouros.csv', 'r', encoding='ISO-8859-1') as tesouro_lista:
    tesouro = csv.reader(tesouro_lista)
    for linha in tesouro:
        try:
            TESOUROS.append(linha[0])
        except IndexError:
            continue

''' Abre arquivo das dicas dos hobbys,cabelos,detalhes e os carros'''
with open('ARQUIVOS CSV/pistacaracteristicas.csv', 'r', encoding='ISO-8859-1') as dicas_lista:
    linha_dicas = csv.reader(dicas_lista)
    for linha in linha_dicas:
        try:
            DICAS_HOBBY.append(linha[0])
            DICAS_CABELO.append(linha[1])
            DICAS_DETALHE.append(linha[2])
            DICAS_CARRO.append(linha[3])
            DICAS_VAZIA.append(linha[4])
        except IndexError:
            continue

'''Abre arquivo das caracteristicas dos bandidos'''
with open('ARQUIVOS CSV/caracteristicas.csv', 'r', encoding='ISO-8859-1') as lista_caracteristicas:
    caracteristicas = csv.reader(lista_caracteristicas)
    for linha in caracteristicas:
        try:
            HOBBY.append(linha[0])
            CABELOS.append(linha[1])
            DETALHE.append(linha[2])
            CARRO.append(linha[3])
        except IndexError:
            continue

'''Abre arquivo dos lugares da cidade em que se deve ir investigar'''
with open('ARQUIVOS CSV/lugares.csv', 'r', encoding='ISO-8859-1') as lugares:
    lugaress = csv.reader(lugares)
    for linha in lugaress:
        try:
            LUGARES.append(linha[0])
        except IndexError:
            continue

'''Abre arquivo com a lista das patentes e dias da semana'''
with open('ARQUIVOS CSV/patentesedias.csv', 'r', encoding='ISO-8859-1') as patentes_e_dias:
    patentes_e_diass = csv.reader(patentes_e_dias)
    for linha in patentes_e_diass:
        try:
            PATENTES.append(linha[0])
            DIAS.append(linha[1])
        except IndexError:
            continue

''' Cores em RGB para ser usadas no jogo'''
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (160, 160, 160)

dificuldade = 0
tentativas = 5
caracteristicas_certas = 0
bandidos_capturados = 0
dia_indice = random.randint(0, 6)
hora = random.randint(0, 23)
dia_limite = dia_indice - 1

'''Definindo fonte e as imagens a ser usadas'''
TEXTO_GRANDE = pygame.font.Font('assets/big_noodle_titling.ttf', 115)
TEXTO_MEDIO = pygame.font.Font('assets/big_noodle_titling.ttf', 30)
TEXTO_PEQUENO = pygame.font.Font('assets/big_noodle_titling.ttf', 20)
MENU_JOGO_IMG = pygame.image.load('assets/Menu_do_Jogo.png')
INTERFACE_JOGO_IMG = pygame.image.load('assets/Jogo_Interface_Principal.png')
PAUSAR_IMG = pygame.image.load('assets/Pausar.png')
MENU_INVESTIGAR_IMG = pygame.image.load('assets/Menu_Investigar.png')
MENU_VIAJAR_IMG = pygame.image.load('assets/Menu_Viajar.png')
ICONE_JOGO_IMG = pygame.image.load('assets/Jogo_Icone.png')
MENU_NOME_JOGADOR_IMG = pygame.image.load('assets/Menu_Nome.png')
MENU_DETALHES_CARRO_CABELO_IMG = pygame.image.load('assets/Menu_detalhes_carro_cabelo.png')
MENU_HOBBY_IMG = pygame.image.load('assets/Menu_Hobby.png')
MENU_SEXO_IMG = pygame.image.load('assets/Menu_sexo.png')
RANKING_IMG = pygame.image.load('assets/Ranking.png')
INST_IMG1 = pygame.image.load('assets/Inst_pg1.png')
INST_IMG2 = pygame.image.load('assets/Inst_pg2.png')
CREDITOS_IMG = pygame.image.load('assets/Creditos.png')
CLICK_SOM = pygame.mixer.Sound('assets/Select Sound.ogg')

''' Definindo resolução e framerate do jogo'''
RESOLUCAO_LARGURA = 800
RESOLUCAO_ALTURA = 600
RESOLUCAO_JOGO = pygame.display.set_mode((RESOLUCAO_LARGURA, RESOLUCAO_ALTURA))
pygame.display.set_caption('Where in the world is Carmen Sandiego?')
pygame.display.set_icon(ICONE_JOGO_IMG)
FPS = pygame.time.Clock()

def reseta_variaveis():
    '''Função que reserta as varias flags, tais variaveis servem para quando nós queremos que uma coisa aconteça só uma vez'''
    global flag_bandido, flag_detalhes, flag_cidades, flag_cidades_proxima, flag_lugares, flag_dica, \
        flag_carro, flag_hobby, flag_cabelo, cont_cidades, caracteristicas_certas, \
        hobby_bandido, detalhe_bandido, carro_bandido, cabelo_bandido, sexo_bandido, \
        dia_indice, hora, dia_limite, mandado_certo

    flag_lugares = False
    flag_cidades = False
    if dificuldade < 6:
        flag_bandido = False
    flag_cabelo = False
    flag_carro = False
    flag_cidades_proxima = False
    flag_detalhes = False
    flag_hobby = False
    flag_dica = False
    cont_cidades = 0
    caracteristicas_certas = 0
    hobby_bandido = ''
    detalhe_bandido = ''
    carro_bandido = ''
    cabelo_bandido = ''
    sexo_bandido = ''
    dia_indice = random.randint(0, 6)
    hora = random.randint(0, 23)
    dia_limite = dia_indice - 1
    mandado_certo = []

def dificuldade_jogo():
    '''Função de dificuldade do jogo'''
    global distancia_lugar, caracteristicas_necessarias, nome_bandido, sexo_mandado

    if dificuldade == 0:
        distancia_lugar = 2
        caracteristicas_necessarias = 3
    elif dificuldade == 1:
        distancia_lugar = 3
        caracteristicas_necessarias = 3
    elif dificuldade == 2:
        distancia_lugar = 4
        caracteristicas_necessarias = 4
    elif dificuldade == 3:
        distancia_lugar = 4
        caracteristicas_necessarias = 4
    elif dificuldade == 4:
        distancia_lugar = 5
        caracteristicas_necessarias = 4
    elif dificuldade == 5:
        distancia_lugar = 4
        caracteristicas_necessarias = 5
    else:
        distancia_lugar = 5
        caracteristicas_necessarias = 5
        nome_bandido = "Carmen Sandiego"
        sexo_mandado = 'Feminino'

def ver_ranking():
    '''Ler e mostrar o ranking para o jogador'''
    data = csv.reader(open('ARQUIVOS CSV/ranking.csv', encoding='ISO-8859-1'))
    RESOLUCAO_JOGO.blit(RANKING_IMG, (0, 0))
    centralizar_texto(420, 550, 'Pressione esc ou direito do mouse para voltar para o menu')
    X = 150
    y = 75
    while True:
        pygame_eventos(menu_jogo)
        for nome, patente, bandidos in data:
            centralizar_texto(X, y, nome)
            centralizar_texto((X + 230), y, patente)
            centralizar_texto((X + 470), y, bandidos)
            y += 50
        pygame.display.update()
        FPS.tick(60)

def salvar_jogo():
    '''Salvar informações do jogo em um arquivo csv'''
    time.sleep(1)
    with open('ARQUIVOS CSV/save.csv', 'w', encoding='ISO-8859-1') as arquivo_salvar:
        info = csv.writer(arquivo_salvar)
        info.writerow([nome_jogador, bandidos_capturados, dificuldade, tentativas])

def ranking_guardar():
    '''Guardar as informações ao final do jogo para o ranking'''
    arquivo_csv = open('ARQUIVOS CSV/ranking.csv', 'a', encoding='ISO-8859-1')
    if os.stat("ARQUIVOS CSV/ranking.csv").st_size == 0:
        arquivo_csv.write(nome_jogador + "," + PATENTES[dificuldade] + "," + str(bandidos_capturados))
    else:
        arquivo_csv.write("\n" + nome_jogador + "," + PATENTES[dificuldade] + "," + str(bandidos_capturados))
    arquivo_csv.close()

def centralizar_texto(x, y, msg):
    '''Função para centralizar texto'''

    superficie_texto, retangulo_texto = objetos_texto(msg, TEXTO_PEQUENO)
    retangulo_texto.center = ((x, y))
    RESOLUCAO_JOGO.blit(superficie_texto, retangulo_texto)

def objetos_texto(texto, fonte):
    '''Função para pegar o retângulo do texto'''
    textSurface = fonte.render(texto, True, BRANCO)
    return textSurface, textSurface.get_rect()

def botoes(msg, x, y, largura, altura, cor_escura, cor_clara, ação=None):
    ''' Botões que vão ser usados no jogo'''

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + largura > mouse[0] > x and y + altura > mouse[1] > y:
        pygame.draw.rect(RESOLUCAO_JOGO, cor_clara, (x, y, largura, altura))
        if click[0] == 1 and ação != None:
            pygame.mixer.Sound.play(CLICK_SOM)
            ação()
    else:
        pygame.draw.rect(RESOLUCAO_JOGO, cor_escura, (x, y, largura, altura))

    superficie_texto, retangulo_texto = objetos_texto(msg, TEXTO_PEQUENO)
    retangulo_texto.center = ((x + (largura / 2)), (y + (altura / 2)))
    RESOLUCAO_JOGO.blit(superficie_texto, retangulo_texto)

def botoes_mandado(msg, x, y, largura, altura, cor_escura, cor_clara, str, variavel):
    '''  Botões que vão ser usados no menu do mandado'''

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + largura > mouse[0] > x and y + altura > mouse[1] > y:
        pygame.draw.rect(RESOLUCAO_JOGO, cor_clara, (x, y, largura, altura))
        if click[0] == 1:
            pygame.mixer.Sound.play(CLICK_SOM)
            variavel = str
            return variavel

    else:
        pygame.draw.rect(RESOLUCAO_JOGO, cor_escura, (x, y, largura, altura))

    superficie_texto, retangulo_texto = objetos_texto(msg, TEXTO_PEQUENO)
    retangulo_texto.center = ((x + (largura / 2)), (y + (altura / 2)))
    RESOLUCAO_JOGO.blit(superficie_texto, retangulo_texto)

def descricao():
    '''Função para imprimir na tela a descrição da cidade'''
    decidir_cidade_inicial()
    imprimir_texto(RESOLUCAO_JOGO, cidade_descricao, (415, 70), TEXTO_PEQUENO, BRANCO)

def bandidos():
    '''Função para imprimir o nome do bandido a ser procurado'''
    global flag_bandido, nome_bandido, sexo_mandado

    if flag_bandido == False:
        indice = random.randint(0, 1)
        indice2 = random.randint(0, 14)
        if indice == 0:
            nome_bandido = NOMES_MASCULINOS[indice2]
            sexo_mandado = 'Masculino'
        else:
            nome_bandido = NOMES_FEMININOS[indice2]
            sexo_mandado = 'Feminino'
        flag_bandido = True

def lugar():
    '''Escolha dos lugares para a cidade atual'''
    global flag_lugares, lugar_1, lugar_2, lugar_3

    if flag_lugares == False:
        while True:
            lugar_1 = random.randrange(len(LUGARES))
            lugar_2 = random.randrange(len(LUGARES))
            lugar_3 = random.randrange(len(LUGARES))
            if lugar_2 == lugar_1:
                lugar_2 = random.randrange(len(LUGARES))
            if lugar_3 == lugar_1 or lugar_3 == lugar_2:
                lugar_3 = random.randrange(len(LUGARES))
            else:
                flag_lugares = True
                return lugar_1, lugar_2, lugar_3
    else:
        return lugar_1, lugar_2, lugar_3

def decidir_cidade_inicial():
    '''Função para decidir cidade incial'''

    global flag_cidades, cidade_descricao, cidade_atual, cidade_d1, cidade_d2, cidade_d3, cidade_da_vez, tesouro_roubado

    if flag_cidades == False:
        proximas_cidades = []
        cidade_o = random.randint(0, 14)
        cidade_descricao = DESCRICAO[cidade_o]
        cidade_d1 = CIDADE_DESTINO1[cidade_o]
        cidade_d2 = CIDADE_DESTINO2[cidade_o]
        cidade_d3 = CIDADE_DESTINO3[cidade_o]
        cidade_atual = CIDADE_ORIGEM[cidade_o]
        proximas_cidades.append(cidade_d1)
        proximas_cidades.append(cidade_d2)
        proximas_cidades.append(cidade_d3)
        indice_cidade = random.randrange(len(proximas_cidades))
        cidade_da_vez = proximas_cidades[indice_cidade]
        tesouro_roubado = TESOUROS[cidade_o]
        flag_cidades = True

def caracteristicas_bandido():
    '''FUnção que define as caracteristicas aleatorias do bandido a ser procurado'''
    global hobby_mandado, detalhes_mandado, cabelo_mandado, carro_mandado, flag_hobby, flag_detalhes, \
        flag_cabelo, flag_carro, carro_bandido, cabelo_bandido, detalhe_bandido, \
        hobby_bandido, sexo_bandido, indice_cabelo, indice_detalhes, indice_carro, indice_hobby, mandado_bandido

    if flag_hobby == False:
        indice_hobby = random.randint(0, 4)
        hobby_mandado = HOBBY[indice_hobby]
    if flag_detalhes == False:
        indice_detalhes = random.randint(0, 3)
        detalhes_mandado = DETALHE[indice_detalhes]
    if flag_cabelo == False:
        indice_cabelo = random.randint(0, 3)
        cabelo_mandado = CABELOS[indice_cabelo]
    if flag_carro == False:
        indice_carro = random.randint(0, 3)
        carro_mandado = CARRO[indice_carro]

    mandado_bandido = [hobby_mandado, detalhes_mandado, cabelo_mandado, carro_mandado, sexo_mandado]
    flag_hobby = True
    flag_detalhes = True
    flag_cabelo = True
    flag_carro = True

def dicas_caracteristicas():
    '''Função para escolher aleatoriamente as dicas das caracteristicas do bandido que está sendo investigado'''
    global flag_dica, dica1_lugares, dica2_lugares, dica3_lugares

    if flag_dica == False:
        dica_destino = dicas_destinos(cidade_da_vez)
        caracteristicas_bandido()

        dicas = []
        dicas.append(DICAS_DETALHE[indice_detalhes])
        dicas.append(DICAS_CABELO[indice_cabelo])
        dicas.append(DICAS_HOBBY[indice_hobby])
        dicas.append(DICAS_CARRO[indice_carro])
        dicas.append(dica_destino)
        dicas.append(DICAS_VAZIA[random.randint(0, 3)])

        while True:
            dica1_lugares = dicas[random.randint(0, 5)]
            dica2_lugares = dicas[random.randint(0, 5)]
            dica3_lugares = dicas[random.randint(0, 5)]
            if dica2_lugares == dica1_lugares:
                dica2_lugares = dicas[random.randint(0, 5)]
            if dica1_lugares != dica_destino and dica2_lugares != dica_destino:
                dica3_lugares = dica_destino
            if dica3_lugares == dica1_lugares or dica3_lugares == dica2_lugares:
                dica3_lugares = dicas[random.randint(0, 5)]
            else:
                flag_dica = True
                break

def mudar_cidades(cidade_viajar, lista_distancia):
    '''Função que define a opção de viajar para outra cidade'''
    global flag_dica, flag_lugares, cidade_descricao, cidade_atual, \
        cidade_d1, cidade_d2, cidade_d3, cidade_da_vez, dica1_lugares, dica2_lugares, dica3_lugares, hora, cont_cidades

    cidade_atual = cidade_viajar
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()
        RESOLUCAO_JOGO.blit(MENU_NOME_JOGADOR_IMG, (100, 280))
        centralizar_texto(200, 325, 'Viajando...')
        cont_cidades += 1

        pygame.display.update()
        FPS.tick(60)
        time.sleep(2)
        break

    for i in range(len(CIDADE_ORIGEM)):
        if cidade_atual == CIDADE_ORIGEM[i]:
            cidade_d1 = CIDADE_DESTINO1[i]
            cidade_d2 = CIDADE_DESTINO2[i]
            cidade_d3 = CIDADE_DESTINO3[i]
            cidade_descricao = DESCRICAO[i]
            hora += int(lista_distancia[i])
            break
    if cidade_atual == cidade_da_vez:
        proximas_cidades = [cidade_d1, cidade_d2, cidade_d3]
        indice_cidade = random.randrange(len(proximas_cidades))
        cidade_da_vez = proximas_cidades[indice_cidade]
        flag_dica = False
    else:
        dica1_lugares = 'Essa pessoa não foi vista por aqui'
        dica2_lugares = 'Essa pessoa não foi vista por aqui'
        dica3_lugares = 'Essa pessoa não foi vista por aqui'

    flag_lugares = False
    loop_jogo()

def cidade1_viajar():
    '''Função que pega a variavel da conexão da cidade atual para ser utilizada na função mudar_cidades'''

    mudar_cidades(cidade_d1, CIDADE_DISTANCIA1)

def cidade2_viajar():
    '''Função que pega a variavel da conexão da cidade atual para ser utilizada na função mudar_cidades'''

    mudar_cidades(cidade_d2, CIDADE_DISTANCIA2)

def cidade3_viajar():
    '''Função que pega a variavel da conexão da cidade atual para ser utilizada na função mudar_cidades'''

    mudar_cidades(cidade_d3, CIDADE_DISTANCIA3)

def dicas_destinos(cidade_destino):
    '''Função para receber a dica do proximo destino'''
    dica_cidade = []

    for i in range(len(CIDADE_ORIGEM)):
        if cidade_destino == CIDADE_ORIGEM[i]:
            dica_cidade.append(DICA1[i])
            dica_cidade.append(DICA2[i])
            if DICA3[i] != '':
                dica_cidade.append(DICA3[i])
            break

    while True:
        try:
            dica_indice = random.randint(0, 2)
            dica_da_vez = dica_cidade[dica_indice]
            break
        except IndexError:
            continue

    return dica_da_vez

def dicas_lugar(dica):
    '''Função para mostrar a dica do lugar que está sendo investigado'''
    global hora

    FUNDO_PRETO1 = pygame.image.load('assets/fundo_preto.png')
    time.sleep(0.1)
    hora += distancia_lugar
    RESOLUCAO_JOGO.blit(INTERFACE_JOGO_IMG, (0, 0))
    RESOLUCAO_JOGO.blit(FUNDO_PRETO1, (415, 100))
    imprimir_texto(RESOLUCAO_JOGO, dica, (415, 100), TEXTO_PEQUENO, BRANCO)

def investigando_tela():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()
        RESOLUCAO_JOGO.blit(MENU_NOME_JOGADOR_IMG, (100, 280))
        centralizar_texto(200, 325, 'Investigando...')

        pygame.display.update()
        FPS.tick(60)
        time.sleep(1)
        break

def dica_lugar1():
    '''Função para indicar qual dica estará no lugar da cidade que o bandido passou'''
    investigando_tela()
    if verificar_ganhou():
        time.sleep(1)
        tela_final_ganhou()
    elif verificar_perdeu() == False:
        time.sleep(1)
        tela_final_perdeu()
    else:
        dicas_caracteristicas()
        dicas_lugar(dica1_lugares)

def dica_lugar2():
    '''Função para indicar qual dica estará no lugar da cidade que o bandido passou'''
    investigando_tela()
    if verificar_ganhou():
        time.sleep(1)
        tela_final_ganhou()
    elif verificar_perdeu() == False:
        time.sleep(1)
        tela_final_perdeu()
    else:
        dicas_caracteristicas()
        dicas_lugar(dica2_lugares)

def dica_lugar3():
    '''Função para indicar qual dica estará no lugar da cidade que o bandido passou'''
    investigando_tela()
    if verificar_ganhou():
        time.sleep(1)
        tela_final_ganhou()
    elif verificar_perdeu() == False:
        time.sleep(1)
        tela_final_perdeu()
    else:
        dicas_caracteristicas()
        dicas_lugar(dica3_lugares)

def sexo_menu():
    '''Menu para preencher o sexo do bandido no mandado'''
    global sexo_bandido
    LARGURA = 160
    ALTURA = 50
    COORDENADA_X = 195
    COORDENADA_Y = 200

    while True:
        pygame_eventos(mandado, sexo_bandido)

        sexo_bandido = botoes_mandado('Masculino', COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, 'Masculino', sexo_bandido)
        if sexo_bandido == 'Masculino':
            break
        sexo_bandido = botoes_mandado('Feminino', COORDENADA_X, (COORDENADA_Y+50), LARGURA, ALTURA, PRETO, CINZA, 'Feminino', sexo_bandido)
        if sexo_bandido == 'Feminino':
            break

        RESOLUCAO_JOGO.blit(MENU_SEXO_IMG, (190, 193))

    cidade_img = pygame.image.load('assets/%s.png' % cidade_atual)
    RESOLUCAO_JOGO.blit(cidade_img, (10, 119))
    return sexo_bandido

def hobby_menu():
    '''Menu para preencher o hobby do bandido no mandado'''
    global hobby_bandido
    LARGURA = 160
    ALTURA = 50
    COORDENADA_X = 195
    COORDENADA_Y = 200

    while True:
        pygame_eventos(mandado, hobby_bandido)

        hobby_bandido = botoes_mandado('%s' % HOBBY[0], COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, '%s' % HOBBY[0], hobby_bandido)
        if hobby_bandido == HOBBY[0]:
            break
        hobby_bandido = botoes_mandado('%s' % HOBBY[1], COORDENADA_X, (COORDENADA_Y+50), LARGURA, ALTURA, PRETO, CINZA, '%s' % HOBBY[1], hobby_bandido)
        if hobby_bandido == HOBBY[1]:
            break
        hobby_bandido = botoes_mandado('%s' % HOBBY[2], COORDENADA_X, (COORDENADA_Y+100), LARGURA, ALTURA, PRETO, CINZA, '%s' % HOBBY[2], hobby_bandido)
        if hobby_bandido == HOBBY[2]:
            break
        hobby_bandido = botoes_mandado('%s' % HOBBY[3], COORDENADA_X, (COORDENADA_Y+150), LARGURA, ALTURA, PRETO, CINZA, '%s' % HOBBY[3], hobby_bandido)
        if hobby_bandido == HOBBY[3]:
            break
        hobby_bandido = botoes_mandado('%s' % HOBBY[4], COORDENADA_X, (COORDENADA_Y+200), LARGURA, ALTURA, PRETO, CINZA, '%s' % HOBBY[4], hobby_bandido)
        if hobby_bandido == HOBBY[4]:
            break

        RESOLUCAO_JOGO.blit(MENU_HOBBY_IMG, (190, 190))

    cidade_img = pygame.image.load('assets/%s.png' % cidade_atual)
    RESOLUCAO_JOGO.blit(cidade_img, (10, 119))
    return hobby_bandido

def detalhe_menu():
    ''' Menu para preencher o detalhe do bandido no mandado'''
    global detalhe_bandido
    LARGURA = 160
    ALTURA = 50
    COORDENADA_X = 195
    COORDENADA_Y = 200

    while True:
        pygame_eventos(mandado, detalhe_bandido)

        detalhe_bandido = botoes_mandado('%s' % DETALHE[0], COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, '%s' % DETALHE[0],
                                         detalhe_bandido)
        if detalhe_bandido == DETALHE[0]:
            break
        detalhe_bandido = botoes_mandado('%s' % DETALHE[1], COORDENADA_X, (COORDENADA_Y+50), LARGURA, ALTURA, PRETO, CINZA, '%s' % DETALHE[1],
                                         detalhe_bandido)
        if detalhe_bandido == DETALHE[1]:
            break
        detalhe_bandido = botoes_mandado('%s' % DETALHE[2], COORDENADA_X, (COORDENADA_Y+100), LARGURA, ALTURA, PRETO, CINZA, '%s' % DETALHE[2],
                                         detalhe_bandido)
        if detalhe_bandido == DETALHE[2]:
            break
        detalhe_bandido = botoes_mandado('%s' % DETALHE[3], COORDENADA_X, (COORDENADA_Y+150), LARGURA, ALTURA, PRETO, CINZA, '%s' % DETALHE[3],
                                         detalhe_bandido)
        if detalhe_bandido == DETALHE[3]:
            break

        RESOLUCAO_JOGO.blit(MENU_DETALHES_CARRO_CABELO_IMG, (190, 190))

    cidade_img = pygame.image.load('assets/%s.png' % cidade_atual)
    RESOLUCAO_JOGO.blit(cidade_img, (10, 119))
    return detalhe_bandido

def cabelo_menu():
    '''Menu para preencher a cor do cabelo do bandido no mandado'''
    global cabelo_bandido
    LARGURA = 160
    ALTURA = 50
    COORDENADA_X = 195
    COORDENADA_Y = 200

    while True:
        pygame_eventos(mandado, cabelo_bandido)

        cabelo_bandido = botoes_mandado('%s' % CABELOS[0], COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, '%s' % CABELOS[0],
                                        cabelo_bandido)
        if cabelo_bandido == CABELOS[0]:
            break
        cabelo_bandido = botoes_mandado('%s' % CABELOS[1], COORDENADA_X, (COORDENADA_Y+50), LARGURA, ALTURA, PRETO, CINZA, '%s' % CABELOS[1],
                                        cabelo_bandido)
        if cabelo_bandido == CABELOS[1]:
            break
        cabelo_bandido = botoes_mandado('%s' % CABELOS[2], COORDENADA_X, (COORDENADA_Y+100), LARGURA, ALTURA, PRETO, CINZA, '%s' % CABELOS[2],
                                        cabelo_bandido)
        if cabelo_bandido == CABELOS[2]:
            break
        cabelo_bandido = botoes_mandado('%s' % CABELOS[3], COORDENADA_X, (COORDENADA_Y+150), LARGURA, ALTURA, PRETO, CINZA, '%s' % CABELOS[3],
                                        cabelo_bandido)
        if cabelo_bandido == CABELOS[3]:
            break

        RESOLUCAO_JOGO.blit(MENU_DETALHES_CARRO_CABELO_IMG, (190, 190))

    cidade_img = pygame.image.load('assets/%s.png' % cidade_atual)
    RESOLUCAO_JOGO.blit(cidade_img, (10, 119))
    return cabelo_bandido

def carro_menu():
    '''Menu para preencher o modelo do bandido no mandado'''
    global carro_bandido
    LARGURA = 160
    ALTURA = 50
    COORDENADA_X = 195
    COORDENADA_Y = 200

    while True:
        pygame_eventos(mandado, carro_bandido)

        carro_bandido = botoes_mandado('%s' % CARRO[0], COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, '%s' % CARRO[0], carro_bandido)
        if carro_bandido == CARRO[0]:
            break
        carro_bandido = botoes_mandado('%s' % CARRO[1], COORDENADA_X, (COORDENADA_Y+50), LARGURA, ALTURA, PRETO, CINZA, '%s' % CARRO[1], carro_bandido)
        if carro_bandido == CARRO[1]:
            break
        carro_bandido = botoes_mandado('%s' % CARRO[2], COORDENADA_X, (COORDENADA_Y+100), LARGURA, ALTURA, PRETO, CINZA, '%s' % CARRO[2], carro_bandido)
        if carro_bandido == CARRO[2]:
            break
        carro_bandido = botoes_mandado('%s' % CARRO[3], COORDENADA_X, (COORDENADA_Y+150), LARGURA, ALTURA, PRETO, CINZA, '%s' % CARRO[3], carro_bandido)
        if carro_bandido == CARRO[3]:
            break

        RESOLUCAO_JOGO.blit(MENU_DETALHES_CARRO_CABELO_IMG, (190, 190))

    cidade_img = pygame.image.load('assets/%s.png' % cidade_atual)
    RESOLUCAO_JOGO.blit(cidade_img, (10, 119))
    return carro_bandido

def mandado():
    '''Menu para criação do mandado de prisão e as escolha das caracteristicas para o bandido'''
    global carro_bandido, cabelo_bandido, detalhe_bandido, hobby_bandido, sexo_bandido
    LARGURA = 355
    ALTURA = 60
    COORDENADA_X = 420
    COORDENADA_Y = 25

    while True:
        pygame_eventos(loop_jogo)

        if carro_bandido == None:
            carro_bandido = ''
        if cabelo_bandido == None:
            cabelo_bandido = ''
        if detalhe_bandido == None:
            detalhe_bandido = ''
        if hobby_bandido == None:
            hobby_bandido = ''
        if sexo_bandido == None:
            sexo_bandido = ''

        botoes('Sexo: %s' % sexo_bandido, COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, sexo_menu)
        botoes('Detalhes: %s' % detalhe_bandido, COORDENADA_X, (COORDENADA_Y+60), LARGURA, ALTURA, PRETO, CINZA, detalhe_menu)
        botoes('Hobby: %s' % hobby_bandido, COORDENADA_X, (COORDENADA_Y+120), LARGURA, ALTURA, PRETO, CINZA, hobby_menu)
        botoes('Cabelo: %s' % cabelo_bandido, COORDENADA_X, (COORDENADA_Y+180), LARGURA, ALTURA, PRETO, CINZA, cabelo_menu)
        botoes('Veículo: %s' % carro_bandido, COORDENADA_X, (COORDENADA_Y+240), LARGURA, ALTURA, PRETO, CINZA, carro_menu)
        botoes('Enviar Mandado', COORDENADA_X, (COORDENADA_Y+325), LARGURA, ALTURA, PRETO, CINZA, verificar_mandado)

        centralizar_texto(600, 567, 'Mandado')

def verificar_mandado():
    '''Função para verificar se o mandando está certo'''
    global mandado_certo, caracteristicas_certas, hora

    time.sleep(0.1)
    mandado_jogador = [hobby_bandido, detalhe_bandido, carro_bandido, cabelo_bandido, sexo_bandido]
    hora += 3

    for i in range(len(mandado_jogador)):
        if mandado_jogador[i] in mandado_bandido and mandado_jogador[i] not in mandado_certo:
            caracteristicas_certas += 1
            mandado_certo.append(mandado_jogador[i])

def dias_horas():
    '''Tempo utilizado no jogo'''
    global hora, dia_indice

    while True:
        try:
            dia = DIAS[dia_indice]
            break
        except IndexError:
            dia_indice = 0
    if hora > 23:
        if hora % 2 == 0:
            hora = 0
        else:
            hora = 1
        dia_indice += 1

    if hora >= 0 and hora < 12:
        centralizar_texto(200, 90, ('%s, %s a.m. ' % (dia, str(hora))))
    else:
        centralizar_texto(200, 90, ('%s, %s p.m. ' % (dia, str(hora))))

def recebe_nome_jogador():
    ''' Função que recebe e retorna o nome do jogador'''

    global nome_jogador
    teclas_não_adc = ['backspace', 'tab', 'space', 'escape', 'down', 'up', 'right', 'left', 'enter']

    while True:
        RESOLUCAO_JOGO.fill(PRETO)
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
                    intro()
                else:
                    letra = pygame.key.name(event.key)
                    if letra.isalpha() and letra not in teclas_não_adc:
                        nome_jogador += letra

        RESOLUCAO_JOGO.fill(PRETO)
        RESOLUCAO_JOGO.blit(INTERFACE_JOGO_IMG, (0, 0))
        RESOLUCAO_JOGO.blit(MENU_NOME_JOGADOR_IMG, (100, 380))
        centralizar_texto(200, 400, 'Nome do jogador:')
        centralizar_texto(200, 450, nome_jogador)
        pygame.display.update()
        FPS.tick(60)

def intro():
    '''Função que mostra o que deve ser feito, introdução'''
    COORDENADA_X = 600
    COORDENADA_Y = 50
    reseta_variaveis()
    decidir_cidade_inicial()
    dificuldade_jogo()
    caracteristicas_bandido()

    while True:
        pygame_eventos(loop_jogo)
        RESOLUCAO_JOGO.fill(PRETO)
        RESOLUCAO_JOGO.blit(INTERFACE_JOGO_IMG, (0, 0))
        centralizar_texto(COORDENADA_X, COORDENADA_Y, 'Dificuldade atual: %s' % (PATENTES[dificuldade]))
        imprimir_texto(RESOLUCAO_JOGO, ('O ladrão robou %s' % (tesouro_roubado)),
                       ((COORDENADA_X-175), (COORDENADA_Y+25)), TEXTO_PEQUENO, BRANCO)
        centralizar_texto(COORDENADA_X, (COORDENADA_Y+100), 'Sua missão é captura-lo')
        centralizar_texto(COORDENADA_X, (COORDENADA_Y+150), 'Cidade onde aconteceu o roubo: %s' % (cidade_atual))
        centralizar_texto(COORDENADA_X, (COORDENADA_Y+450), 'Pressione esc ou direito do mouse para continuar')

def imprimir_texto(surface, texto, pos, fonte, cor):
    '''Função que quebra textos no jogo'''
    palavras = [palavra.split(' ') for palavra in
                texto.splitlines()]  # 2D array onde cada linha é uma lista de palavras.
    espaco = fonte.size(' ')[0]  # A largura de um espaco.
    max_largura, max_altura = surface.get_size()
    x, y = pos
    for linha in palavras:
        for palavra in linha:
            palavra_superficie = fonte.render(palavra, 0, cor)
            palavra_largura, palavra_altura = palavra_superficie.get_size()
            if x + palavra_largura >= max_largura:
                x = pos[0]  # Reseta o x.
                y += palavra_altura  # Começa na nova linha.
            surface.blit(palavra_superficie, (x, y))
            x += palavra_largura + espaco

def menu_investigar():
    ''' Lugares para investigar na cidade'''
    LARGURA = 300
    ALTURA = 35
    COORDENADA_X = 50
    COORDENADA_Y = 460

    indice_lugar1, indice_lugar2, indice_lugar3 = lugar()

    while True:
        pygame_eventos(loop_jogo)
        RESOLUCAO_JOGO.blit(MENU_INVESTIGAR_IMG, (15, 255))
        lugar1_img = pygame.image.load('assets/%s.png' % LUGARES[indice_lugar1])
        lugar2_img = pygame.image.load('assets/%s.png' % LUGARES[indice_lugar2])
        lugar3_img = pygame.image.load('assets/%s.png' % LUGARES[indice_lugar3])
        botoes('%s' % (LUGARES[indice_lugar1]), COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, dica_lugar1)
        botoes('%s' % (LUGARES[indice_lugar2]), COORDENADA_X, (COORDENADA_Y+35), LARGURA, ALTURA, PRETO, CINZA, dica_lugar2)
        botoes('%s' % (LUGARES[indice_lugar3]), COORDENADA_X, (COORDENADA_Y+70), LARGURA, ALTURA, PRETO, CINZA, dica_lugar3)
        RESOLUCAO_JOGO.blit(lugar1_img, ((COORDENADA_X-20), (COORDENADA_Y-150)))
        RESOLUCAO_JOGO.blit(lugar2_img, ((COORDENADA_X+100), (COORDENADA_Y-150)))
        RESOLUCAO_JOGO.blit(lugar3_img, ((COORDENADA_X+220), (COORDENADA_Y-150)))

        centralizar_texto(600, 532, 'Investigar')
        centralizar_texto(600, 567, 'Mandado')

def pygame_eventos(ação, variavel=' '):
    '''Função que pega todos os eventos do jogo'''
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair_jogo()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if variavel != ' ':
                    cidade_img = pygame.image.load('assets/%s.png' % cidade_atual)
                    RESOLUCAO_JOGO.blit(cidade_img, (10, 119))
                    ação()
                else:
                    ação()
        if variavel != ' ':
            if click[2] == 1:
                cidade_img = pygame.image.load('assets/%s.png' % cidade_atual)
                RESOLUCAO_JOGO.blit(cidade_img, (10, 119))
                ação()
        else:
            if click[2] == 1:
                ação()

    pygame.display.update()
    FPS.tick(60)

def escolher_destinos_menu():
    ''' Função para inserir os destinos aleatorios no menu'''
    LARGURA = 300
    ALTURA = 35
    COORDENADA_X = 50
    COORDENADA_Y = 460

    while True:
        pygame_eventos(loop_jogo)
        RESOLUCAO_JOGO.blit(MENU_VIAJAR_IMG, (15, 435))
        botoes('%s' % cidade_d1, COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, cidade1_viajar)
        botoes('%s' % cidade_d2, COORDENADA_X, (COORDENADA_Y+35), LARGURA, ALTURA, PRETO, CINZA, cidade2_viajar)
        if cidade_d3 != '':
            botoes('%s' % cidade_d3, COORDENADA_X, (COORDENADA_Y+70), LARGURA, ALTURA, PRETO, CINZA, cidade3_viajar)
        centralizar_texto(600, 497, 'Viajar')
        centralizar_texto(600, 532, 'Investigar')
        centralizar_texto(600, 567, 'Mandado')

def tela_fim_jogo_ganhou():
    '''Tela se o jogador completar o jogo'''
    global bandidos_capturados

    bandidos_capturados += 1
    ranking_guardar()
    while True:
        pygame_eventos(creditos)
        cadeia_img = pygame.image.load('assets/Cadeia_capturado.png')
        RESOLUCAO_JOGO.fill(PRETO)
        RESOLUCAO_JOGO.blit(INTERFACE_JOGO_IMG, (0, 0))
        RESOLUCAO_JOGO.blit(cadeia_img, (450, 75))

        centralizar_texto(COORDENADA_X_TELAS_FINAIS, COORDENADA_Y_TELAS_FINAIS, 'Parabéns %s' % nome_jogador)
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+50), 'Você conseguiu capturar %s' % nome_bandido)
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+70), 'no tempo dado')
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+100), 'A polícia de %s agradece' % cidade_atual)
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+120), 'pela ajuda')
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+250), 'Você conseguiu capturar Carmen Sandiego!!!')
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+280), 'Obrigado por jogar.')
        centralizar_texto((COORDENADA_X_TELAS_FINAIS+395), (COORDENADA_Y_TELAS_FINAIS+350), 'Pressione esc ou direito do mouse para continuar')

def tela_fim_jogo_perdeu():
    '''Tela de gameover'''
    ranking_guardar()
    while True:
        pygame_eventos(creditos)
        cadeia_img = pygame.image.load('assets/Cadeia_vazio.png')
        RESOLUCAO_JOGO.fill(PRETO)
        RESOLUCAO_JOGO.blit(INTERFACE_JOGO_IMG, (0, 0))
        RESOLUCAO_JOGO.blit(cadeia_img, (450, 75))

        centralizar_texto(COORDENADA_X_TELAS_FINAIS, COORDENADA_Y_TELAS_FINAIS, 'Está foi a ultima vez que você falhou')
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+50), '%s, parece que esta vida não foi feita para você' % (nome_jogador))
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+350), 'Fim de jogo.')
        centralizar_texto((COORDENADA_X_TELAS_FINAIS+395), (COORDENADA_Y_TELAS_FINAIS+350), 'Pressione esc ou direito do mouse para continuar')

def verificar_ganhou():
    '''Função que verefica se o jogador ganhou'''
    global dificuldade, bandidos_capturados
    dificuldade_jogo()

    if caracteristicas_certas >= caracteristicas_necessarias and cont_cidades > 2:
        if dificuldade == 6:
            tela_fim_jogo_ganhou()
        else:
            dificuldade += 1
            bandidos_capturados += 1
            return True

def verificar_perdeu():
    '''Função que verefica se o jogador perdeu'''
    global tentativas

    if DIAS[dia_indice] == DIAS[dia_limite] or cont_cidades > 6:
        if tentativas == 0:
            tela_fim_jogo_perdeu()
        else:
            tentativas -= 1
            return False

def tela_final_ganhou():
    '''Função que mostra quando o jogador capturou o bandido, ou foi promovido, ou ganhou o jogo '''

    while True:
        pygame_eventos(intro)
        cadeia_img = pygame.image.load('assets/Cadeia_capturado.png')
        RESOLUCAO_JOGO.fill(PRETO)
        RESOLUCAO_JOGO.blit(INTERFACE_JOGO_IMG, (0, 0))
        RESOLUCAO_JOGO.blit(cadeia_img, (450, 75))

        centralizar_texto(COORDENADA_X_TELAS_FINAIS, COORDENADA_Y_TELAS_FINAIS, 'Parabéns %s' % nome_jogador)
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+50), 'Você conseguiu capturar %s' % nome_bandido)
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+70), 'no tempo dado')
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+100), 'A polícia de %s agradece' % cidade_atual)
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+120), 'pela ajuda')
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+250), 'Você foi promovido a %s' % PATENTES[dificuldade])
        centralizar_texto((COORDENADA_X_TELAS_FINAIS+395), (COORDENADA_Y_TELAS_FINAIS+350), 'Pressione esc ou direito do mouse para continuar')

def tela_final_perdeu():
    '''Função que mostra na tela quando o jogador não termina o mandado, ou perdeu a vez, ou perdeu uma vida'''

    while True:
        pygame_eventos(intro)
        cadeia_img = pygame.image.load('assets/Cadeia_vazio.png')
        RESOLUCAO_JOGO.fill(PRETO)
        RESOLUCAO_JOGO.blit(INTERFACE_JOGO_IMG, (0, 0))
        RESOLUCAO_JOGO.blit(cadeia_img, (450, 75))

        centralizar_texto(COORDENADA_X_TELAS_FINAIS, COORDENADA_Y_TELAS_FINAIS, 'O ladrão foi preso mas você não tinha o mandado')
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+50), 'Melhor sorte da proxima vez %s' % (nome_jogador))
        centralizar_texto(COORDENADA_X_TELAS_FINAIS, (COORDENADA_Y_TELAS_FINAIS+350), 'Você perdeu uma vida')
        centralizar_texto((COORDENADA_X_TELAS_FINAIS+395), (COORDENADA_Y_TELAS_FINAIS+350), 'Pressione esc ou direito do mouse para continuar')

def pagina_um_instrucoes():
    '''Pagina um do menu instruções'''
    LARGURA = 150
    ALTURA = 50
    COORDENADA_X = 15
    COORDENADA_Y = 520

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            RESOLUCAO_JOGO.fill(PRETO)
            RESOLUCAO_JOGO.blit(INST_IMG1, (0, 0))

            botoes("Menu Principal", COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, menu_jogo)
            botoes("Página Dois", (COORDENADA_X+615), COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, pagina_dois_instrucoes)

        pygame.display.update()
        FPS.tick(60)

def pagina_dois_instrucoes():
    '''Pagina dois do menu instruções'''
    LARGURA = 150
    ALTURA = 50
    COORDENADA_X = 15
    COORDENADA_Y = 520

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            RESOLUCAO_JOGO.fill(PRETO)
            RESOLUCAO_JOGO.blit(INST_IMG2, (0, 0))

            botoes("Página um", COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, pagina_um_instrucoes)
            botoes("Menu Principal", (COORDENADA_X+615), COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, menu_jogo)

        pygame.display.update()
        FPS.tick(60)

def carregar_jogo():
    '''Carregar o jogo a partir do save feito,se existir'''
    global nome_jogador, bandidos_capturados, dificuldade, tentativas

    with open('ARQUIVOS CSV/save.csv', 'r', encoding='ISO-8859-1') as arquivo_carregar:
        info = csv.reader(arquivo_carregar)
        for linha in info:
            try:
                nome_jogador = linha[0]
                bandidos_capturados = int(linha[1])
                dificuldade = int(linha[2])
                tentativas = int(linha[3])
            except IndexError:
                continue

    intro()
def carregar_musica():
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.load('assets/Menu Tema.mp3')
    pygame.mixer.music.play(-1)

def menu_jogo():
    ''' Menu principal do jogo'''
    intro = True
    LARGURA = 150
    ALTURA = 50
    COORDENADA_X = 325
    COORDENADA_Y = 200
    carregar_musica()

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

        RESOLUCAO_JOGO.blit(MENU_JOGO_IMG, (0, 0))
        botoes('Novo Jogo', COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, recebe_nome_jogador)
        botoes('Carregar Jogo', COORDENADA_X, (COORDENADA_Y+50), LARGURA, ALTURA, PRETO, CINZA, carregar_jogo)
        botoes('Ranking', COORDENADA_X, (COORDENADA_Y+100), LARGURA, ALTURA, PRETO, CINZA, ver_ranking)
        botoes('Instruções', COORDENADA_X, (COORDENADA_Y+150), LARGURA, ALTURA, PRETO, CINZA, pagina_um_instrucoes)
        botoes('Sair', COORDENADA_X, (COORDENADA_Y+200), LARGURA, ALTURA, PRETO, CINZA, sair_jogo)

        pygame.display.update()
        FPS.tick(60)

def interface_jogo():
    '''Interface grafica do jogo'''
    LARGURA = 360
    ALTURA = 35
    COORDENADA_X = 420
    COORDENADA_Y = 480
    bandidos()

    RESOLUCAO_JOGO.blit(INTERFACE_JOGO_IMG, (0, 0))
    cidade_img = pygame.image.load('assets/%s.png' % cidade_atual)
    RESOLUCAO_JOGO.blit(cidade_img, (10, 119))
    centralizar_texto(200, 40, '%s' % cidade_atual)
    centralizar_texto(600, 40, 'Bandido a ser procurado:%s' % nome_bandido)
    centralizar_texto(600, 462, 'Tentativas restantes: %s' % tentativas)
    botoes('Viajar', COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, escolher_destinos_menu)
    botoes('Investigar', COORDENADA_X, (COORDENADA_Y+35), LARGURA, ALTURA, PRETO, CINZA, menu_investigar)
    botoes('Mandado', COORDENADA_X, (COORDENADA_Y+70), LARGURA, ALTURA, PRETO, CINZA, mandado)

def pausar(pause=False):
    ''' Menu de pausa'''
    LARGURA = 150
    ALTURA = 50
    COORDENADA_X = 310
    COORDENADA_Y = 197

    while pause:
        pygame_eventos(loop_jogo)

        RESOLUCAO_JOGO.blit(PAUSAR_IMG, (305, 190))
        botoes('Continuar Jogo', COORDENADA_X, COORDENADA_Y, LARGURA, ALTURA, PRETO, CINZA, loop_jogo)
        botoes('Salvar Jogo', COORDENADA_X, (COORDENADA_Y+50), LARGURA, ALTURA, PRETO, CINZA, salvar_jogo)
        botoes('Sair do Jogo', COORDENADA_X, (COORDENADA_Y+100), LARGURA, ALTURA, PRETO, CINZA, sair_jogo)

def sair_jogo():
    ''' Sair do modulo pygame e do jogo'''
    pygame.quit()
    quit()

def creditos():
    '''Tela de creditos do jogo'''
    pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.load('assets/Creditos Tema.mp3')
    pygame.mixer.music.play(-1)

    while True:
        pygame_eventos(sair_jogo)

        RESOLUCAO_JOGO.blit(CREDITOS_IMG, (0, 0))
        pygame.display.update()
        FPS.tick(60)

def loop_jogo():
    '''Loop do jogo'''

    pygame.mixer.music.stop()
    saiu_jogo = False
    while not saiu_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair_jogo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa = True
                    pausar(pausa)

        RESOLUCAO_JOGO.fill(PRETO)
        dias_horas()
        interface_jogo()
        descricao()
        pygame.display.update()
        FPS.tick(60)

menu_jogo()
loop_jogo()
sair_jogo()