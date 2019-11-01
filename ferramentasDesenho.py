from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

cCanvas = []

tamanho = 1

coresCanvas = []

def dentro(coord1, coord2): #coord2 = (x1, x2, y1, y2)
    if(coord1[0] > coord2[0]) & (coord1[0] < coord2[1]) & (coord1[1] > coord2[2]) & (coord1[1] < coord2[3]):
        return True
    else:
        return False

def novoDesenho(ferramenta, canvas, coord1, coord2, cor1, cor2, preenchimento, tam):
    global cCanvas
    global tamanho
    
    cCanvas = canvas
    tamanho = tam
    
    glPointSize(tamanho)
    
    if(ferramenta == "reta"):
        bresenham(coord1, coord2, cor1)
    elif(ferramenta == "quadrado"):
        quadrado(coord1, coord2, cor1, cor2, preenchimento)
    elif(ferramenta == "triangulo"):
        triangulo(coord1, coord2, cor1, cor2, preenchimento)
    elif(ferramenta == "circulo"):
        circulo(coord1, coord2, cor1, cor2, preenchimento)

def novoDesenhoSemGravar(ferramenta, canvas, coord1, coord2, cor1, cor2, preenchimento, tam):
    global cCanvas
    global tamanho
    
    cCanvas = canvas
    tamanho = tam
    
    glPointSize(tamanho)
    
    if(ferramenta == "reta"):
        bresenhamSemGravar(coord1, coord2, cor1)
    elif(ferramenta == "quadrado"):
        quadradoSemGravar(coord1, coord2, cor1, cor2, preenchimento)
    elif(ferramenta == "triangulo"):
        trianguloSemGravar(coord1, coord2, cor1, cor2, preenchimento)
    elif(ferramenta == "circulo"):
        circuloSemGravar(coord1, coord2, cor1, cor2, preenchimento)
        
def bresenhamSemGravar(cInicial, cFinal, cor):
    
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
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


def bresenham(cInicial, cFinal, cor):
    
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    glBegin(GL_POINTS)
    glColor3f(cor[0], cor[1], cor[2])
    if(dentro((x1, y1), cCanvas)):
        coresCanvas.append((x1, y1, cor, tamanho))
    
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
                    if (x, y, cor, tamanho) in coresCanvas:
                        coresCanvas.remove((x, y, cor, tamanho))
                    coresCanvas.append((x, y, cor, tamanho))
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y -= 1
                x += 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    if (x, y, cor, tamanho) in coresCanvas:
                        coresCanvas.remove((x, y, cor, tamanho))
                    coresCanvas.append((x, y, cor, tamanho))
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
                    if (x, y, cor, tamanho) in coresCanvas:
                        coresCanvas.remove((x, y, cor, tamanho))
                    coresCanvas.append((x, y, cor, tamanho))
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y -= 1
                x -= 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    if (x, y, cor, tamanho) in coresCanvas:
                        coresCanvas.remove((x, y, cor, tamanho))
                    coresCanvas.append((x, y, cor, tamanho))
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
                    if (x, y, cor, tamanho) in coresCanvas:
                        coresCanvas.remove((x, y, cor, tamanho))
                    coresCanvas.append((x, y, cor, tamanho))
                if pantX < 0:
                    pantX = pantX + dy2 
                else:
                    pantX = pantX + dydx2
                    y += 1
                x -= 1
        else:
            for i in range(dy):
                if(dentro((x, y), cCanvas)):
                    if (x, y, cor, tamanho) in coresCanvas:
                        coresCanvas.remove((x, y, cor, tamanho))
                    coresCanvas.append((x, y, cor, tamanho))
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
                    if (x, y, cor, tamanho) in coresCanvas:
                        coresCanvas.remove((x, y, cor, tamanho))
                    coresCanvas.append((x, y, cor, tamanho))
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
                    if (x, y, cor, tamanho) in coresCanvas:
                        coresCanvas.remove((x, y, cor, tamanho))
                    coresCanvas.append((x, y, cor, tamanho))
                if pantY < 0:
                    pantY = pantY + dx2 
                else:
                    pantY = pantY - dydx2
                    x += 1
                y += 1
    
    glEnd()

def quadrado(cInicial, cFinal, cor1, cor2, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    bresenham((x1, y1), (x1, y2), cor1)
    bresenham((x1, y2), (x2, y2), cor1)
    bresenham((x2, y2), (x2, y1), cor1)
    bresenham((x2, y1), (x1, y1), cor1)

def quadradoSemGravar(cInicial, cFinal, cor1, cor2, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    bresenhamSemGravar((x1, y1), (x1, y2), cor1)
    bresenhamSemGravar((x1, y2), (x2, y2), cor1)
    bresenhamSemGravar((x2, y2), (x2, y1), cor1)
    bresenhamSemGravar((x2, y1), (x1, y1), cor1)
    
def triangulo(cInicial, cFinal, cor1, cor2, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    bresenham((int((x2 + x1)/2), y1), (x1, y2), cor1)
    bresenham((int((x2 + x1)/2), y1), (x2, y2), cor1)
    bresenham((x1, y2), (x2, y2), cor1)

def trianguloSemGravar(cInicial, cFinal, cor1, cor2, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = cFinal[0]
    y2 = cFinal[1]
    
    bresenhamSemGravar((int((x2 + x1)/2), y1), (x1, y2), cor1)
    bresenhamSemGravar((int((x2 + x1)/2), y1), (x2, y2), cor1)
    bresenhamSemGravar((x1, y2), (x2, y2), cor1)

def circulo(cInicial, cFinal, cor1, cor2, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = 0
    y2 = cFinal[1]
    
    d = 1 - y2
    
    glColor3f(cor1[0], cor1[1], cor1[2])
    glBegin(GL_POINTS)
    if(dentro((x2+x1, y2+y1), cCanvas)):
        coresCanvas.append((x2+x1, y2+y1, cor1, tamanho))
    if(dentro((x1-y2, x2+y1), cCanvas)):
        coresCanvas.append((x1-y2, x2+y1, cor1, tamanho))
    if(dentro((x1-y2, y1-x2), cCanvas)):
        coresCanvas.append((x1-y2, y1-x2, cor1, tamanho))
    if(dentro((x1-x2, y1-y2), cCanvas)):
        coresCanvas.append((x1-x2, y1-y2, cor1, tamanho))
    if(dentro((x1-x2, y1+y2), cCanvas)):
        coresCanvas.append((x1-x2, y1+y2, cor1, tamanho))
    if(dentro((x2+x1, y1-y2), cCanvas)):
        coresCanvas.append((x2+x1, y1-y2, cor1, tamanho))
    if(dentro((y2+x1, y1-x2), cCanvas)):
        coresCanvas.append((y2+x1, y1-x2, cor1, tamanho))
    if(dentro((y2+x1, x2+y1), cCanvas)):
        coresCanvas.append((y2+x1, x2+y1, cor1, tamanho))
    
    while(y2 > x2):
        if(d < 0):
            d += (2 * x2) + 3
        else:
            d += 2 * (x2 - y2) + 5
            y2 -= 1
        x2 += 1
        if(dentro((x2+x1, y2+y1), cCanvas)):
            coresCanvas.append((x2+x1, y2+y1, cor1, tamanho))
        if(dentro((x1-y2, x2+y1), cCanvas)):
            coresCanvas.append((x1-y2, x2+y1, cor1, tamanho))
        if(dentro((x1-y2, y1-x2), cCanvas)):
            coresCanvas.append((x1-y2, y1-x2, cor1, tamanho))
        if(dentro((x1-x2, y1-y2), cCanvas)):
            coresCanvas.append((x1-x2, y1-y2, cor1, tamanho))
        if(dentro((x1-x2, y1+y2), cCanvas)):
            coresCanvas.append((x1-x2, y1+y2, cor1, tamanho))
        if(dentro((x2+x1, y1-y2), cCanvas)):
            coresCanvas.append((x2+x1, y1-y2, cor1, tamanho))
        if(dentro((y2+x1, y1-x2), cCanvas)):
            coresCanvas.append((y2+x1, y1-x2, cor1, tamanho))
        if(dentro((y2+x1, x2+y1), cCanvas)):
            coresCanvas.append((y2+x1, x2+y1, cor1, tamanho))
    
    glEnd()

def circuloSemGravar(cInicial, cFinal, cor1, cor2, preenchimento):
    x1 = cInicial[0]
    y1 = cInicial[1]
    x2 = 0
    y2 = cFinal[1]
    
    d = 1 - y2
    
    glColor3f(cor1[0], cor1[1], cor1[2])
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
