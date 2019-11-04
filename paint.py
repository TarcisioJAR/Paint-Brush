import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ferramentasDesenho import *

coordMouse = [0,0] #x, y
coordCanvas = [10, 800, 110, 600] #x1, x2, y1, y2
coordRedimensionar = [  [(coordCanvas[1]+coordCanvas[0])/2, coordCanvas[3] + 3], #sul  #+3 de offset
                        [coordCanvas[1] + 3, (coordCanvas[3]+coordCanvas[2])/2], #leste
                        [coordCanvas[1] + 3, coordCanvas[3] + 3]] #sudeste

def rgb(cor):
    return cor/255

cores = [   ( 0, 0, 0 ),                        #preto      
            ( rgb(127), rgb(127), rgb(127) ),   #cinza50   
            ( rgb(136), rgb(0), rgb(21) ),      #vermelhoEscuro
            ( rgb(237), rgb(28), rgb(36) ),     #vermelho
            ( rgb(255), rgb(127), rgb(39) ),    #laranja      
            ( rgb(255), rgb(242), rgb(0) ),     #amarelo      
            ( rgb(34), rgb(177), rgb(76) ),     #verde        
            ( rgb(0), rgb(162), rgb(232) ),     #turquesa     
            ( rgb(63), rgb(72), rgb(204) ),     #indigo       
            ( rgb(163), rgb(73), rgb(164) ),    #roxo         
            ( 1, 1, 1 ),                        #branco       
            ( rgb(195), rgb(195), rgb(195) ),   #cinza25      
            ( rgb(185), rgb(122), rgb(87) ),    #marrom       
            ( rgb(255), rgb(174), rgb(201) ),   #rosa         
            ( rgb(255), rgb(201), rgb(14) ),    #dourado      
            ( rgb(239), rgb(228), rgb(176) ),   #amareloClaro 
            ( rgb(181), rgb(230), rgb(29) ),    #lima         
            ( rgb(153), rgb(217), rgb(234) ),   #turquezaClaro
            ( rgb(112), rgb(146), rgb(190) ),   #cinzaAzulado
            ( rgb(200), rgb(191), rgb(231) )]   #lavanda     

coordCores = [  (590, 610, 15, 35), #preto      
                (615, 635, 15, 35), #cinza50   
                (640, 660, 15, 35), #vermelhoEscuro
                (665, 685, 15, 35), #vermelho
                (690, 710, 15, 35), #laranja      
                (715, 735, 15, 35), #amarelo      
                (740, 760, 15, 35), #verde        
                (765, 785, 15, 35), #turquesa     
                (790, 810, 15, 35), #indigo       
                (815, 835, 15, 35), #roxo         
                (590, 610, 40, 60), #branco       
                (615, 635, 40, 60), #cinza25      
                (640, 660, 40, 60), #marrom       
                (665, 685, 40, 60), #rosa         
                (690, 710, 40, 60), #dourado      
                (715, 735, 40, 60), #amareloClaro 
                (740, 760, 40, 60), #lima         
                (765, 785, 40, 60), #turquezaClaro
                (790, 810, 40, 60), #cinzaAzulado
                (815, 835, 40, 60)] #lavanda     

coordBotoes = [ (24, 46, 17, 43), #lapis
                (24, 46, 48, 71), #borracha
                (65, 88, 17, 43), #balde
                (65, 88, 48, 71), #pipeta
                (128, 152, 18, 42), #reta
                (158, 182, 18, 42), #curva
                (188, 212, 18, 42), #circulo
                (218, 242, 18, 42), #quadrado
                (248, 272, 18, 42)] #triangulo
                
ferramentas = [ "lapis", "borracha", "balde", "pipeta",
                "reta", "curva", "circulo", "quadrado", "triangulo"]
                
ferramenta = "lapis"
                
coordTamanhos = [   (408, 483, 17, 35), #pequeno
                    (408, 483, 36, 54), #medio
                    (408, 483, 55, 73)] #grande

tamanhos = [1, 3, 8] #pequeno, medio e grande

#Flag que indica se esta havendo redimensionamento
resize_clicado=0

#Flags que indicam esta havendo ou nao redimensionamento da area desenhavel
resize_baixo=0 
resize_sudeste=0
resize_direita=0

estadoMouse = -1
coordClica = (0, 0)
coordSolta = (0, 0)

estadoMouseAnterior = 1
clickInicial = 1

def drawMenu():
    global largura
    global altura
    global cor1
    global cor2
    
    #desenha retangulo de fundo
    glColor3f(rgb(245), rgb(246), rgb(247))
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f( 0, 100)
    glVertex2f(largura,  100)
    glVertex2f(largura,  0)
    glEnd()
    
    #escreve nome das secoes
    glColor3f(0, 0, 0)
    glRasterPos2f(26, 95)
    for letra in 'Ferramentas':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, c_int(ord(letra)))
    glRasterPos2f(230, 95)
    for letra in 'Formas':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, c_int(ord(letra)))
    glRasterPos2f(425, 95)
    for letra in 'Tamanho':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, c_int(ord(letra)))
    glRasterPos2f(655, 95)
    for letra in 'Cores':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, c_int(ord(letra)))
    #escreve detalhes das secoes
    glRasterPos2f(305, 50)
    for letra in 'Preenchimento':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, c_int(ord(letra)))
    glRasterPos2f(510, 65)
    for letra in 'Cor 1':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, c_int(ord(letra)))
    glRasterPos2f(550, 65)
    for letra in 'Cor 2':
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, c_int(ord(letra)))
        
    #desenha separadores
    glColor3f(rgb(217), rgb(218), rgb(219))
    glBegin(GL_LINES)
    glVertex2f(110, 5)
    glVertex2f(110, 95)
    glVertex2f(395, 5)
    glVertex2f(395, 95)
    glVertex2f(495, 5)
    glVertex2f(495, 95)
    glVertex2f(850, 5)
    glVertex2f(850, 95)
    glEnd()
    
    #desenha ferramentas
    glBegin(GL_QUADS)
    #lapis
    glColor3f(rgb(255), rgb(242), rgb(0))
    glVertex2f(27, 35)
    glVertex2f(30, 40)
    glVertex2f(42, 25)
    glVertex2f(39, 20)
    glColor3f(rgb(221), rgb(110), rgb(109))
    glVertex2f(38, 23)
    glVertex2f(42, 26)
    glVertex2f(45, 22)
    glVertex2f(42, 18)
    glColor3f(rgb(255), rgb(200), rgb(142))
    glVertex2f(25, 42)
    glVertex2f(30, 40)
    glVertex2f(30, 38)
    glVertex2f(27, 35)
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f(25, 42)
    glVertex2f(26, 42)
    glVertex2f(26, 41)
    glVertex2f(25, 41)
    
    #borracha
    glColor3f(rgb(250), rgb(150), rgb(147))
    glVertex2f(25, 70)
    glVertex2f(35, 70)
    glVertex2f(35, 50)
    glVertex2f(25, 60)
    glVertex2f(35, 70)
    glVertex2f(45, 60)
    glVertex2f(45, 50)
    glVertex2f(35, 50)
    
    #balde
    glColor3f(rgb(195), rgb(195), rgb(195))
    glVertex2f(78, 41)
    glVertex2f(87, 31)
    glVertex2f(75, 18)
    glVertex2f(66, 28)
    glColor3f(rgb(237), rgb(28), rgb(36))
    glVertex2f(66, 41)
    glVertex2f(69, 30)
    glVertex2f(71, 23)
    glVertex2f(65, 29)
    
    #pipeta
    glColor3f(rgb(213), rgb(227), rgb(240))
    glVertex2f(65, 69)
    glVertex2f(69, 70)
    glVertex2f(75, 65)
    glVertex2f(70, 60)
    
    glVertex2f(75, 65)
    glVertex2f(80, 60)
    glVertex2f(75, 56)
    glVertex2f(70, 60)
    
    glEnd()
    
    #detalhes das ferramentas
    glBegin(GL_LINES)
    glColor3f(rgb(199), rgb(127), rgb(124))
    glVertex(35,69)
    glVertex(35, 60)
    glVertex(35, 60)
    glVertex(26, 60)
    glVertex(35, 60)
    glVertex(44, 51)
    glColor3f(rgb(127), rgb(127), rgb(127))
    glVertex(76, 17)
    glVertex(76, 27)
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(rgb(39), rgb(116), rgb(180))
    glVertex2f(71, 59)
    glVertex2f(78, 63)
    glVertex2f(81, 60)
    glVertex2f(80, 59)
    glVertex2f(87, 53)
    glVertex2f(86, 50)
    glVertex2f(82, 50)
    glVertex2f(75, 57)
    glVertex2f(74, 56)
    glEnd()
    
    #desenha formas
    glBegin(GL_QUADS)
    glColor3f(rgb(250), rgb(251), rgb(252))
    glVertex2f(120, 10)
    glVertex2f(120, 80)
    glVertex2f(285, 80)
    glVertex2f(285, 10)
    glEnd()
    
    #reta
    glBegin(GL_LINES)
    glColor3f(rgb(26), rgb(106), rgb(171))
    glVertex2f(130, 20)
    glVertex2f(150, 40)
    glEnd()
    
    #curva
    glBegin(GL_LINE_STRIP)
    glVertex2f(160, 40)
    glVertex2f(163, 30)
    glVertex2f(165, 28)
    glVertex2f(167, 30)
    glVertex2f(170, 38)
    glVertex2f(172, 40)
    glVertex2f(175, 38)
    glVertex2f(178, 30)
    glVertex2f(180, 20)
    glEnd()
    
    #circulo
    glBegin(GL_LINE_STRIP)
    glVertex2f(190, 30)
    glVertex2f(193, 37)
    glVertex2f(200, 40)
    glVertex2f(207, 37)
    glVertex2f(210, 30)
    glVertex2f(207, 23)
    glVertex2f(200, 20)
    glVertex2f(193, 23)
    glVertex2f(190,30)
    glEnd()
    
    #quadrado
    glBegin(GL_LINE_STRIP)
    glVertex2f(221, 39)
    glVertex2f(239, 39)
    glVertex2f(239, 21)
    glVertex2f(221, 21)
    glVertex2f(221, 39)
    glEnd()
    
    #triangulo
    glBegin(GL_LINE_STRIP)
    glVertex2f(250, 39)
    glVertex2f(270, 39)
    glVertex2f(260, 20)
    glVertex2f(250, 39)
    glEnd()
    
    #quadrado preenchimento
    glColor3f(rgb(30), rgb(57), rgb(91))
    glBegin(GL_LINE_STRIP)
    glVertex2f(330, 20)
    glVertex2f(345, 20)
    glVertex2f(345, 35)
    glVertex2f(330, 35)
    glVertex2f(330, 20)
    glEnd()
    
    #linhas-tamanhos
    glBegin(GL_QUADS)
    glVertex2f(410, 25)
    glVertex2f(480, 25)
    glVertex2f(480, 26)
    glVertex2f(410, 26)
    
    glVertex2f(410, 44)
    glVertex2f(480, 44)
    glVertex2f(480, 47)
    glVertex2f(410, 47)
    
    glVertex2f(410, 60)
    glVertex2f(480, 60)
    glVertex2f(480, 68)
    glVertex2f(410, 68)
    glEnd()
    
    #desenha cores
    glBegin(GL_QUADS)
    glColor3f(cor1[0], cor1[1], cor1[2])
    glVertex2f(508, 20)
    glVertex2f(508, 50)
    glVertex2f(538, 50)
    glVertex2f(538, 20)
    
    glColor3f(cor2[0], cor2[1], cor2[2])
    glVertex2f(548, 20)
    glVertex2f(548, 50)
    glVertex2f(578, 50)
    glVertex2f(578, 20)
    
    for i in range(len(cores)):
        cor = cores[i]
        coord = coordCores[i]
        glColor3f(cor[0], cor[1], cor[2])
        glVertex2f(coord[0], coord[2])
        glVertex2f(coord[0], coord[3])
        glVertex2f(coord[1], coord[3])
        glVertex2f(coord[1], coord[2])
        
    glEnd()

def drawStatus():
    global largura
    global altura
    global coordMouse
    
    glColor3f(rgb(245), rgb(246), rgb(247))
    glBegin(GL_QUADS)
    glVertex2f(0, altura-25)
    glVertex2f( 0, altura)
    glVertex2f(largura,  altura)
    glVertex2f(largura,  altura-25)
    glEnd()
    
    x = coordMouse[0] - coordCanvas[0]
    y = coordMouse[1] - coordCanvas[2]
    if((x < 0) or (y < 0)
                    or (x > coordCanvas[1] - coordCanvas[0])
                    or (y > coordCanvas[3] - coordCanvas[2])):
        coord = ''
    else: coord = '{}, {}px'.format(str(x), str(y))
    glColor3f(0, 0, 0)
    glRasterPos2f(10, altura-10)
    for letra in coord:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, c_int(ord(letra)))

def drawRedimensionar():
    global coordRedimensionar
    
    glPointSize(5)
    glColor3f(0, 0, 0)
    glBegin(GL_POINTS)
    glVertex2f(coordRedimensionar[0][0], coordRedimensionar[0][1])
    glVertex2f(coordRedimensionar[1][0], coordRedimensionar[1][1])
    glVertex2f(coordRedimensionar[2][0], coordRedimensionar[2][1])
    glEnd()
    
def pipeta(coord):
    global cor1
    global cor2
    
    cor = matrizCores[coord[0]][coord[1]]
    
    if(botaoMouse == 0):
        if(cor != []): cor1 = cor
        else: cor1 = (1, 1, 1)
    elif(botaoMouse == 2):
        if(cor != []): cor2 = cor
        else: cor2 = (1, 1, 1)
    

def drawCanvas():
    global coordCanvas
    global coordClica
    global coordSolta
    global estadoMouseAnterior
    global clickInicial
    global cor1
    global cor2
    
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(coordCanvas[0], coordCanvas[2])
    glVertex2f(coordCanvas[0], coordCanvas[3])
    glVertex2f(coordCanvas[1],  coordCanvas[3])
    glVertex2f(coordCanvas[1],  coordCanvas[2])
    glEnd()
    
    drawRedimensionar()
    
    glPointSize(tamanho)
    
    if(pegaEstado() == 1) & (arrasteCurva() == False):
        bresenhamSemGravar(p1(), p4())
    
    if(estadoMouse == 0):
        if clickInicial:
            coordClica = coordMouse
            if not dentro(coordMouse, coordCanvas): return
            clickInicial = 0
        coordSolta = coordMouse
        novoDesenhoSemGravar(ferramenta, coordCanvas, coordClica, coordSolta, cor1, cor2, preenchimento, tamanho, botaoMouse)
        if(ferramenta == "pipeta"):
            pipeta(coordSolta)
        estadoMouseAnterior = 0
    if(estadoMouse == 1 and estadoMouseAnterior == 0):  
        coordSolta = coordMouse
        novoDesenho(ferramenta, coordCanvas, coordClica, coordSolta, cor1, cor2, preenchimento, tamanho, botaoMouse)
        estadoMouseAnterior = 1
        clickInicial = 1

def init():
    glClearColor(rgb(212), rgb(221), rgb(235), 0)
    glShadeModel(GL_FLAT)

def display():
    global ferramenta
    global tamanho

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    drawMenu()
    drawStatus()
    drawCanvas()
    
    #seleciona botao
    for i in range(len(ferramentas)):
        if(ferramentas[i] == ferramenta):
            coord = coordBotoes[i]
            glBegin(GL_LINE_STRIP)
            glColor3f(rgb(98), rgb(162), rgb(228))
            glVertex2f(coord[0]-1, coord[2])
            glVertex2f(coord[0]-1, coord[3]+1)
            glVertex2f(coord[1]+1, coord[3]+1)
            glVertex2f(coord[1]+1, coord[2])
            glVertex2f(coord[0]-1, coord[2])
            glEnd()
    
    #seleciona preenchimento
    if(preenchimento == True):
        glBegin(GL_LINE_STRIP)
        glColor3f(rgb(98), rgb(162), rgb(228))
        glVertex2f(331, 26)
        glVertex2f(335, 33)
        glVertex2f(343, 22)
        glEnd()
    
    #seleciona tamanho
    for i in range(len(tamanhos)):
        if(tamanhos[i] == tamanho):
            coord = coordTamanhos[i]
            glBegin(GL_LINE_STRIP)
            glColor3f(rgb(98), rgb(162), rgb(228))
            glVertex2f(coord[0]-1, coord[2])
            glVertex2f(coord[0]-1, coord[3]+1)
            glVertex2f(coord[1]+1, coord[3]+1)
            glVertex2f(coord[1]+1, coord[2])
            glVertex2f(coord[0]-1, coord[2])
            glEnd()
    
    for c in coordsPintadas:
        if(matrizTamanhos[c[0]][c[1]] != []): glPointSize(matrizTamanhos[c[0]][c[1]])
        glBegin(GL_POINTS)
        if(matrizCores[c[0]][c[1]] != []): glColor3f(matrizCores[c[0]][c[1]][0], matrizCores[c[0]][c[1]][1], matrizCores[c[0]][c[1]][2])
        if(dentro((c[0], c[1]), coordCanvas)): glVertex(c[0], c[1])
        else:
            coordsPintadas.remove(c)
            matrizCores[c[0]][c[1]] = []
            matrizTamanhos[c[0]][c[1]] = []
        glEnd()
        
    glutSwapBuffers()
  
def reshape(l, a):
    global largura
    global altura
    largura = l
    altura = a
    
    glViewport(0, 0, l, a)
    glLoadIdentity()
    gluOrtho2D(0, l, a, 0) 

#Funcao chamada toda vez que algum botao do mouse for clicado
def mouse(botao, estado, x, y):
    global coordMouse
    global cor1
    global cor2
    global ferramenta
    global preenchimento
    global tamanho
    
    global coordMouse
    global resize_baixo
    global resize_sudeste
    global resize_direita
    global resize_clicado
    global estadoMouse
    global botaoMouse
    
    coordMouse = [x, y]
    estadoMouse = estado
    botaoMouse = botao
    
    if botao == GLUT_LEFT_BUTTON:
        if resize_clicado:
            resize_clicado=0
            resize_baixo=0
            resize_direita=0
            resize_sudeste=0
            glutSetCursor(GLUT_CURSOR_LEFT_ARROW) 
            
        else:
            #redimensionar por baixo
            if(dentro(coordMouse, (coordRedimensionar[0][0]-8, coordRedimensionar[0][0]+8, coordRedimensionar[0][1]-8, coordRedimensionar[0][1]+8))):
                resize_baixo=1
                resize_clicado=1
                
            #redimensionar pela direita
            if(dentro(coordMouse, (coordRedimensionar[1][0]-8, coordRedimensionar[1][0]+8, coordRedimensionar[1][1]-8, coordRedimensionar[1][1]+8))):
                resize_direita=1
                resize_clicado=1
            
            #redimensionar pelo sudeste
            if(dentro(coordMouse, (coordRedimensionar[2][0]-8, coordRedimensionar[2][0]+8, coordRedimensionar[2][1]-8, coordRedimensionar[2][1]+8))):
                resize_sudeste=1
                resize_clicado=1
        
    #muda ferramenta
    for i in range(len(coordBotoes)):
        coord = coordBotoes[i]
        if(dentro(coordMouse, coord)):
            if(estado == 0):
                ferramenta = ferramentas[i]
    
    #muda preenchimento
    if(dentro(coordMouse, (330, 345, 20, 35))):
        if(estado == 0):
            if(preenchimento == False):
                preenchimento = True
            elif(preenchimento == True):
                preenchimento = False
    
    #muda tamanho
    for i in range(len(coordTamanhos)):
        coord = coordTamanhos[i]
        if(dentro(coordMouse, coord)):
            if(estado == 0):
                tamanho = tamanhos[i]
    
    #seleciona cores
    for i in range(len(cores)):
        cor = cores[i]
        coord = coordCores[i]
        if(dentro(coordMouse, coord)):
            if(botao == 0):
                cor1 = cor
            elif(botao == 2):
                cor2 = cor
    
    glutPostRedisplay()
    
def movimentoMouse(x, y):
    global coordMouse
    
    coordMouse = [x, y]
        
    glutPostRedisplay()


def arraste(x,y):
    global coordMouse
    coordMouse = [x, y]
    
    if resize_baixo:
        glutSetCursor(GLUT_CURSOR_UP_DOWN)
        coordCanvas[3] = y
        coordRedimensionar[0][1] = y + 3 #sul  #+3 de offset
        coordRedimensionar[2][1] = y + 3 #sudeste
        coordRedimensionar[1][1] = (coordCanvas[3]+coordCanvas[2])/2#leste
        
    if resize_direita:
        glutSetCursor(GLUT_CURSOR_LEFT_RIGHT)
        coordCanvas[1] = x
        coordRedimensionar[0][0] = (coordCanvas[1]+coordCanvas[0])/2 #sul
        coordRedimensionar[2][0] = x + 3 #sudeste
        coordRedimensionar[1][0] = x + 3 #leste
        
    if resize_sudeste:
        glutSetCursor(GLUT_CURSOR_TOP_LEFT_CORNER)
        coordCanvas[3] = y
        coordCanvas[1] = x
        coordRedimensionar[0][1] = y + 3 #sul
        coordRedimensionar[2][1] = y + 3 #sudeste
        coordRedimensionar[1][1] = (coordCanvas[3]+coordCanvas[2])/2#leste
        coordRedimensionar[0][0] = (coordCanvas[1]+coordCanvas[0])/2 #sul
        coordRedimensionar[2][0] = x + 3 #sudeste
        coordRedimensionar[1][0] = x + 3 #leste
        
    glutPostRedisplay()
    
 
#configuracao da janela
glutInit(sys.argv) 
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(1200, 800)
glutInitWindowPosition(350, 100)
glutCreateWindow('Paint')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMouseFunc(mouse)
glutPassiveMotionFunc(movimentoMouse);
glutMotionFunc(arraste);
glutMainLoop()
