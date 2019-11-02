from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

cor1 = (0, 0, 0)
cor2 = (1, 1, 1)

cCanvas = []

tamanho = 1
botaoMouse = -1

coordsPintadas = []
matrizCores = []
matrizTamanhos = []



#Coordenada do ultimo ponto que foi pintado (Utilizado na ferramenta lapis)
ultimaCoord = -1

corTrocada = []

#instancia matrizes
for i in range(2000): #max 2000 colunas
    linhaC = []
    linhaT = []
    for j in range(1000): #max 1000 linhas
        linhaC.append([])
        linhaT.append([])
    matrizCores.append(linhaC)
    matrizTamanhos.append(linhaT)

def dentro(coord1, coord2): #coord2 = (x1, x2, y1, y2)
    if(coord1[0] > coord2[0]) & (coord1[0] < coord2[1]) & (coord1[1] > coord2[2]) & (coord1[1] < coord2[3]):
        return True
    else:
        return False

def novoDesenho(ferramenta, canvas, coord1, coord2, c1, c2, preenchimento, tam, botao):
    global cCanvas
    global tamanho
    global cor1
    global cor2
    global botaoMouse
    global ultimaCoord
    
    cor1 = c1
    cor2 = c2
    cCanvas = canvas
    tamanho = tam
    botaoMouse = botao
    
    glPointSize(tamanho)
    
    if(ferramenta == "reta"):
        bresenham(coord1, coord2)
    elif(ferramenta == "quadrado"):
        quadrado(coord1, coord2, preenchimento)
    elif(ferramenta == "triangulo"):
        triangulo(coord1, coord2, preenchimento)
    elif(ferramenta == "circulo"):
        circulo(coord1, coord2, preenchimento)
    elif(ferramenta == "lapis"):
        ultimaCoord = -1
    elif(ferramenta == "borracha"):
        borracha(coord1)
    

def novoDesenhoSemGravar(ferramenta, canvas, coord1, coord2, c1, c2, preenchimento, tam, botao):
    global cCanvas
    global tamanho
    global cor1
    global cor2
    global botaoMouse
    global ultimaCoord
    cor1 = c1
    cor2 = c2
    cCanvas = canvas
    tamanho = tam
    botaoMouse = botao
    
    glPointSize(tamanho)
    
    if(ferramenta == "reta"):
        bresenhamSemGravar(coord1, coord2)
    elif(ferramenta == "quadrado"):
        quadradoSemGravar(coord1, coord2, preenchimento)
    elif(ferramenta == "triangulo"):
        trianguloSemGravar(coord1, coord2, preenchimento)
    elif(ferramenta == "circulo"):
        circuloSemGravar(coord1, coord2, preenchimento)
    elif(ferramenta == "lapis"):
        if ultimaCoord == -1: ultimaCoord = coord1
        bresenham(ultimaCoord, coord2)
        ultimaCoord = coord2
    elif(ferramenta == "balde"):
        pintar(coord1)
    elif(ferramenta == "borracha"):
        borracha(coord2)
        
def bresenhamSemGravar(cInicial, cFinal):
    
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    if(botaoMouse == 0):
        cor = cor1
    else: cor = cor2
    
    glBegin(GL_POINTS)
    glColor3f(cor[0], cor[1], cor[2])
    if(dentro((x1, y1), cCanvas)):
        glVertex2f(x1, y1)
    
    if((x1 <= x2) & (y1 >= y2)): #1o quadrante
        dx    = x2 - x1
        dy    = y1 - y2
        dy2   = 2 * dy
        dx2   = 2 * dx
        dydx2 = dy2 - 2 * dx
        pantX  = dy2 - dx
        pantY  = dx2 - dy
        x = x1
        y = y1
        
        if(dydx2 < 0):
            for i in range(dx):
                if(dentro((x, y), cCanvas)):
                    glVertex2f(x, y)
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y -= 1
                x += 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    glVertex2f(x, y)
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x += 1
                y -= 1
    
    elif((x1 > x2) & (y1 > y2)): #2o quadrante
        dx    = x1 - x2
        dy    = y1 - y2
        dy2   = 2 * dy
        dx2   = 2 * dx
        dydx2 = dy2 - 2 * dx
        pantX  = dy2 - dx
        pantY  = dx2 - dy
        x = x1
        y = y1
        
        if(dydx2 < 0):
            for i in range(dx):
                if(dentro((x, y), cCanvas)):
                    glVertex2f(x, y)
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y -= 1
                x -= 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    glVertex2f(x, y)
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x -= 1
                y -= 1
    
    elif((x1 >= x2) & (y1 <= y2)): #3o quadrante
        dx    = x1 - x2
        dy    = y2 - y1
        dy2   = 2 * dy
        dx2   = 2 * dx
        dydx2 = dy2 - 2 * dx
        pantX  = dy2 - dx
        pantY  = dx2 - dy
        x = x1
        y = y1
        
        if(dydx2 < 0):
            for i in range(dx):
                if(dentro((x, y), cCanvas)):
                    glVertex2f(x, y)
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y += 1
                x -= 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    glVertex2f(x, y)
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x -= 1
                y += 1
    
    elif((x1 < x2) & (y1 < y2)): #4o quadrante
        dx    = x2 - x1
        dy    = y2 - y1
        dy2   = 2 * dy
        dx2   = 2 * dx
        dydx2 = dy2 - 2 * dx
        pantX  = dy2 - dx
        pantY  = dx2 - dy
        x = x1
        y = y1
        
        if(dydx2 < 0):
            for i in range(dx):
                if(dentro((x, y), cCanvas)):
                    glVertex2f(x, y)
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y += 1
                x += 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    glVertex2f(x, y)
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x += 1
                y += 1
    
    glEnd()


def bresenham(cInicial, cFinal):
    global matrizCores
    global matrizTamanhos
    
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    if(botaoMouse == 0):
        cor = cor1
    else: cor = cor2
    
    glBegin(GL_POINTS)
    glColor3f(cor[0], cor[1], cor[2])
    if(dentro((x1, y1), cCanvas)):
        if (x1, y1) in coordsPintadas:
            coordsPintadas.remove((x1, y1))
        coordsPintadas.append((x1, y1))
        matrizCores[x1][y1] = cor
        matrizTamanhos[x1][y1] = tamanho
    
    if((x1 <= x2) & (y1 >= y2)): #1o quadrante
        dx    = x2 - x1
        dy    = y1 - y2
        dy2   = 2 * dy
        dx2   = 2 * dx
        dydx2 = dy2 - 2 * dx
        pantX  = dy2 - dx
        pantY  = dx2 - dy
        x = x1
        y = y1
        
        if(dydx2 < 0):
            for i in range(dx):
                if(dentro((x, y), cCanvas)):
                    if (x, y) in coordsPintadas:
                        coordsPintadas.remove((x, y))
                    coordsPintadas.append((x, y))
                    matrizCores[x][y] = cor
                    matrizTamanhos[x][y] = tamanho
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y -= 1
                x += 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    if (x, y) in coordsPintadas:
                        coordsPintadas.remove((x, y))
                    coordsPintadas.append((x, y))
                    matrizCores[x][y] = cor
                    matrizTamanhos[x][y] = tamanho
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x += 1
                y -= 1
    
    elif((x1 > x2) & (y1 > y2)): #2o quadrante
        dx    = x1 - x2
        dy    = y1 - y2
        dy2   = 2 * dy
        dx2   = 2 * dx
        dydx2 = dy2 - 2 * dx
        pantX  = dy2 - dx
        pantY  = dx2 - dy
        x = x1
        y = y1
        
        if(dydx2 < 0):
            for i in range(dx):
                if(dentro((x, y), cCanvas)):
                    if (x, y) in coordsPintadas:
                        coordsPintadas.remove((x, y))
                    coordsPintadas.append((x, y))
                    matrizCores[x][y] = cor
                    matrizTamanhos[x][y] = tamanho
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y -= 1
                x -= 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    if (x, y) in coordsPintadas:
                        coordsPintadas.remove((x, y))
                    coordsPintadas.append((x, y))
                    matrizCores[x][y] = cor
                    matrizTamanhos[x][y] = tamanho
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x -= 1
                y -= 1
    
    elif((x1 >= x2) & (y1 <= y2)): #3o quadrante
        dx    = x1 - x2
        dy    = y2 - y1
        dy2   = 2 * dy
        dx2   = 2 * dx
        dydx2 = dy2 - 2 * dx
        pantX  = dy2 - dx
        pantY  = dx2 - dy
        x = x1
        y = y1
        
        if(dydx2 < 0):
            for i in range(dx):
                if(dentro((x, y), cCanvas)):
                    if (x, y) in coordsPintadas:
                        coordsPintadas.remove((x, y))
                    coordsPintadas.append((x, y))
                    matrizCores[x][y] = cor
                    matrizTamanhos[x][y] = tamanho
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y += 1
                x -= 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    if (x, y) in coordsPintadas:
                        coordsPintadas.remove((x, y))
                    coordsPintadas.append((x, y))
                    matrizCores[x][y] = cor
                    matrizTamanhos[x][y] = tamanho
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x -= 1
                y += 1
    
    elif((x1 < x2) & (y1 < y2)): #4o quadrante
        dx    = x2 - x1
        dy    = y2 - y1
        dy2   = 2 * dy
        dx2   = 2 * dx
        dydx2 = dy2 - 2 * dx
        pantX  = dy2 - dx
        pantY  = dx2 - dy
        x = x1
        y = y1
        
        if(dydx2 < 0):
            for i in range(dx):
                if(dentro((x, y), cCanvas)):
                    if (x, y) in coordsPintadas:
                        coordsPintadas.remove((x, y))
                    coordsPintadas.append((x, y))
                    matrizCores[x][y] = cor
                    matrizTamanhos[x][y] = tamanho
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y += 1
                x += 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    if (x, y) in coordsPintadas:
                        coordsPintadas.remove((x, y))
                    coordsPintadas.append((x, y))
                    matrizCores[x][y] = cor
                    matrizTamanhos[x][y] = tamanho
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x += 1
                y += 1
    
    glEnd()

def quadrado(cInicial, cFinal, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    bresenham((x1, y1), (x1, y2))
    bresenham((x1, y2), (x2, y2))
    bresenham((x2, y2), (x2, y1))
    bresenham((x2, y1), (x1, y1))

def quadradoSemGravar(cInicial, cFinal, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    bresenhamSemGravar((x1, y1), (x1, y2))
    bresenhamSemGravar((x1, y2), (x2, y2))
    bresenhamSemGravar((x2, y2), (x2, y1))
    bresenhamSemGravar((x2, y1), (x1, y1))
    
def triangulo(cInicial, cFinal, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    bresenham((int((x2 + x1)/2), y1), (x1, y2))
    bresenham((int((x2 + x1)/2), y1), (x2, y2))
    bresenham((x1, y2), (x2, y2))

def trianguloSemGravar(cInicial, cFinal, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    bresenhamSemGravar((int((x2 + x1)/2), y1), (x1, y2))
    bresenhamSemGravar((int((x2 + x1)/2), y1), (x2, y2))
    bresenhamSemGravar((x1, y2), (x2, y2))

def circulo(cInicial, cFinal, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = 0
    y2 = cFinal[1]
    
    d = 1 - y2
    
    if(botaoMouse == 0):
        cor = cor1
    else: cor = cor2
    
    glColor3f(cor[0], cor[1], cor[2])
    glBegin(GL_POINTS)
    if(dentro((x2+x1, y2+y1), cCanvas)):
        if (x2+x1, y2+y1) in coordsPintadas: coordsPintadas.remove((x2+x1, y2+y1))
        coordsPintadas.append((x2+x1, y2+y1))
        matrizCores[x2+x1][y2+y1] = cor
        matrizTamanhos[x2+x1][y2+y1] = tamanho
    if(dentro((x1-y2, x2+y1), cCanvas)):
        if (x1-y2, x2+y1) in coordsPintadas: coordsPintadas.remove((x1-y2, x2+y1))
        coordsPintadas.append((x1-y2, x2+y1))
        matrizCores[x1-y2][x2+y1] = cor
        matrizTamanhos[x1-y2][x2+y1] = tamanho
    if(dentro((x1-y2, y1-x2), cCanvas)):
        if (x1-y2, y1-x2) in coordsPintadas: coordsPintadas.remove((x1-y2, y1-x2))
        coordsPintadas.append((x1-y2, y1-x2))
        matrizCores[x1-y2][y1-x2] = cor
        matrizTamanhos[x1-y2][y1-x2] = tamanho
    if(dentro((x1-x2, y1-y2), cCanvas)):
        if (x1-x2, y1-y2) in coordsPintadas: coordsPintadas.remove((x1-x2, y1-y2))
        coordsPintadas.append((x1-x2, y1-y2))
        matrizCores[x1-x2][y1-y2] = cor
        matrizTamanhos[x1-x2][y1-y2] = tamanho
    if(dentro((x1-x2, y1+y2), cCanvas)):
        if (x1-x2, y1+y2) in coordsPintadas: coordsPintadas.remove((x1-x2, y1+y2))
        coordsPintadas.append((x1-x2, y1+y2))
        matrizCores[x1-x2][y1+y2] = cor
        matrizTamanhos[x1-x2][y1+y2] = tamanho
    if(dentro((x2+x1, y1-y2), cCanvas)):
        if (x2+x1, y1-y2) in coordsPintadas: coordsPintadas.remove((x2+x1, y1-y2))
        coordsPintadas.append((x2+x1, y1-y2))
        matrizCores[x2+x1][y1-y2] = cor
        matrizTamanhos[x2+x1][y1-y2] = tamanho
    if(dentro((y2+x1, y1-x2), cCanvas)):
        if (y2+x1, y1-x2) in coordsPintadas: coordsPintadas.remove((y2+x1, y1-x2))
        coordsPintadas.append((y2+x1, y1-x2))
        matrizCores[y2+x1][y1-x2] = cor
        matrizTamanhos[y2+x1][y1-x2] = tamanho
    if(dentro((y2+x1, x2+y1), cCanvas)):
        if (y2+x1, x2+y1) in coordsPintadas: coordsPintadas.remove((y2+x1, x2+y1))
        coordsPintadas.append((y2+x1, x2+y1))
        matrizCores[y2+x1][x2+y1] = cor
        matrizTamanhos[y2+x1][x2+y1] = tamanho
    
    while(y2 > x2):
        if(d < 0):
            d += (2 * x2) + 3
        else:
            d += 2 * (x2 - y2) + 5
            y2 -= 1
        x2 += 1
        if(dentro((x2+x1, y2+y1), cCanvas)):
            if (x2+x1, y2+y1) in coordsPintadas: coordsPintadas.remove((x2+x1, y2+y1))
            coordsPintadas.append((x2+x1, y2+y1))
            matrizCores[x2+x1][y2+y1] = cor
            matrizTamanhos[x2+x1][y2+y1] = tamanho
        if(dentro((x1-y2, x2+y1), cCanvas)):
            if (x1-y2, x2+y1) in coordsPintadas: coordsPintadas.remove((x1-y2, x2+y1))
            coordsPintadas.append((x1-y2, x2+y1))
            matrizCores[x1-y2][x2+y1] = cor
            matrizTamanhos[x1-y2][x2+y1] = tamanho
        if(dentro((x1-y2, y1-x2), cCanvas)):
            if (x1-y2, y1-x2) in coordsPintadas: coordsPintadas.remove((x1-y2, y1-x2))
            coordsPintadas.append((x1-y2, y1-x2))
            matrizCores[x1-y2][y1-x2] = cor
            matrizTamanhos[x1-y2][y1-x2] = tamanho
        if(dentro((x1-x2, y1-y2), cCanvas)):
            if (x1-x2, y1-y2) in coordsPintadas: coordsPintadas.remove((x1-x2, y1-y2))
            coordsPintadas.append((x1-x2, y1-y2))
            matrizCores[x1-x2][y1-y2] = cor
            matrizTamanhos[x1-x2][y1-y2] = tamanho
        if(dentro((x1-x2, y1+y2), cCanvas)):
            if (x1-x2, y1+y2) in coordsPintadas: coordsPintadas.remove((x1-x2, y1+y2))
            coordsPintadas.append((x1-x2, y1+y2))
            matrizCores[x1-x2][y1+y2] = cor
            matrizTamanhos[x1-x2][y1+y2] = tamanho
        if(dentro((x2+x1, y1-y2), cCanvas)):
            if (x2+x1, y1-y2) in coordsPintadas: coordsPintadas.remove((x2+x1, y1-y2))
            coordsPintadas.append((x2+x1, y1-y2))
            matrizCores[x2+x1][y1-y2] = cor
            matrizTamanhos[x2+x1][y1-y2] = tamanho
        if(dentro((y2+x1, y1-x2), cCanvas)):
            if (y2+x1, y1-x2) in coordsPintadas: coordsPintadas.remove((y2+x1, y1-x2))
            coordsPintadas.append((y2+x1, y1-x2))
            matrizCores[y2+x1][y1-x2] = cor
            matrizTamanhos[y2+x1][y1-x2] = tamanho
        if(dentro((y2+x1, x2+y1), cCanvas)):
            if (y2+x1, x2+y1) in coordsPintadas: coordsPintadas.remove((y2+x1, x2+y1))
            coordsPintadas.append((y2+x1, x2+y1))
            matrizCores[y2+x1][x2+y1] = cor
            matrizTamanhos[y2+x1][x2+y1] = tamanho
    
    glEnd()

def circuloSemGravar(cInicial, cFinal, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = 0
    y2 = cFinal[1]
    
    d = 1 - y2
    
    if(botaoMouse == 0):
        cor = cor1
    else: cor = cor2
    
    glColor3f(cor[0], cor[1], cor[2])
    glBegin(GL_POINTS)
    if(dentro((x2+x1, y2+y1), cCanvas)):
        glVertex2f(x2+x1, y2+y1)
    if(dentro((x1-y2, x2+y1), cCanvas)):
        glVertex2f(x1-y2, x2+y1)
    if(dentro((x1-y2, y1-x2), cCanvas)):
        glVertex2f(x1-y2, y1-x2)
    if(dentro((x1-x2, y1-y2), cCanvas)):
        glVertex2f(x1-x2, y1-y2)
    if(dentro((x1-x2, y1+y2), cCanvas)):
        glVertex2f(x1-x2, y1+y2)
    if(dentro((x2+x1, y1-y2), cCanvas)):
        glVertex2f(x2+x1, y1-y2)
    if(dentro((y2+x1, y1-x2), cCanvas)):
        glVertex2f(y2+x1, y1-x2)
    if(dentro((y2+x1, x2+y1), cCanvas)):
        glVertex2f(y2+x1, x2+y1)
    
    while(y2 > x2):
        if(d < 0):
            d += (2 * x2) + 3
        else:
            d += 2 * (x2 - y2) + 5
            y2 -= 1
        x2 += 1
        if(dentro((x2+x1, y2+y1), cCanvas)):
            glVertex2f(x2+x1, y2+y1)
        if(dentro((x1-y2, x2+y1), cCanvas)):
            glVertex2f(x1-y2, x2+y1)
        if(dentro((x1-y2, y1-x2), cCanvas)):
            glVertex2f(x1-y2, y1-x2)
        if(dentro((x1-x2, y1-y2), cCanvas)):
            glVertex2f(x1-x2, y1-y2)
        if(dentro((x1-x2, y1+y2), cCanvas)):
            glVertex2f(x1-x2, y1+y2)
        if(dentro((x2+x1, y1-y2), cCanvas)):
            glVertex2f(x2+x1, y1-y2)
        if(dentro((y2+x1, y1-x2), cCanvas)):
            glVertex2f(y2+x1, y1-x2)
        if(dentro((y2+x1, x2+y1), cCanvas)):
            glVertex2f(y2+x1, x2+y1)
    
    glEnd()


def pintar(coord):
    global cCanvas
    global total
    pilha = []
    visitados = [0,0,0,0]
    x = coord[0]
    y = coord[1]
    x1 = -1
    y1 = -1
    elementosIteracao = [0,0,0,0, x, y, x1, y1]
    pilha.append(elementosIteracao)
    
    if(botaoMouse == 0):
        cor = cor1
    else: cor = cor2
    
    while(pilha != []):
        elementosIteracao = pilha.pop()
        #print("Tirou")
        visitados[0] = elementosIteracao[0]
        visitados[1] = elementosIteracao[1]
        visitados[2] = elementosIteracao[2]
        visitados[3] = elementosIteracao[3]
        x = elementosIteracao[4]
        y = elementosIteracao[5]
        x1 = elementosIteracao[6]
        y1 = elementosIteracao[7]
        
        if(dentro((x, y+1), cCanvas) and visitados[0] == 0 and matrizCores[x][y+1] == corTrocada and (x,y+1) != (x1,y1)):
            #print("A")
            glBegin(GL_POINTS)
            glColor3f(cor[0],cor[1], cor[2])
            coordsPintadas.append((x, y+1))
            matrizCores[x][y+1] = cor
            matrizTamanhos[x][y+1] = 1
            glEnd()
            visitados[0] = 1
            pilha.append([visitados[0], visitados[1], visitados[2], visitados[3], x, y, x1, y1])
            pilha.append([0, 0, 0, 0, x, y+1, x, y])
            
        elif(dentro((x+1, y), cCanvas) and visitados[1] == 0 and matrizCores[x+1][y] == corTrocada and (x+1,y) != (x1,y1)):
            #print("B")
            glBegin(GL_POINTS)
            glColor3f(cor[0],cor[1], cor[2])
            coordsPintadas.append((x+1, y))
            matrizCores[x+1][y] = cor
            matrizTamanhos[x+1][y] = 1
            glEnd()
            visitados[1] = 1
            pilha.append([visitados[0], visitados[1], visitados[2], visitados[3], x, y, x1, y1])
            pilha.append([0, 0, 0, 0, x+1, y, x, y])
        elif(dentro((x, y-1), cCanvas) and visitados[2] == 0 and matrizCores[x][y-1] == corTrocada and (x,y-1) != (x1,y1)):
            glBegin(GL_POINTS)
            glColor3f(cor[0],cor[1], cor[2])
            coordsPintadas.append((x, y-1))
            matrizCores[x][y-1] = cor
            matrizTamanhos[x][y-1] = 1
            glEnd()
            visitados[2] = 1
            pilha.append([visitados[0], visitados[1], visitados[2], visitados[3], x, y, x1, y1])
            pilha.append([0, 0, 0, 0, x, y-1, x, y])
        elif(dentro((x-1, y), cCanvas) and visitados[3] == 0 and matrizCores[x-1][y] == corTrocada and (x-1,y) != (x1,y1)):
            #print("D")
            glBegin(GL_POINTS)
            glColor3f(cor[0],cor[1], cor[2])
            coordsPintadas.append((x-1, y))
            matrizCores[x-1][y] = cor
            matrizTamanhos[x-1][y] = 1
            glEnd()
            visitados[3] = 1
            pilha.append([visitados[0], visitados[1], visitados[2], visitados[3], x, y, x1, y1])
            pilha.append([0, 0, 0, 0, x-1, y, x, y])
            
    
def borracha(coord):
    global cor1
    
    x1 = coord[0] - tamanho*5
    x2 = coord[0] + tamanho*5
    y1 = coord[1] - tamanho*5
    y2 = coord[1] + tamanho*5
    
    cor1 = (0, 0, 0)
    quadradoSemGravar((x1, y1), (x2, y2), False)
    
    for x in range(x2 - x1):
        for y in range(y2 - y1):
            if (x + x1, y + y1) in coordsPintadas:
                if dentro((x+x1, y+y1), (x1, x2, y1, y2)):
                    coordsPintadas.remove((x+x1, y+y1))
                    matrizCores[x+x1][y+y1] = []
                    matrizTamanhos[x+x1][y+y1] = []