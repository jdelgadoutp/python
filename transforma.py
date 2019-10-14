import math

def trans(t,p):
    xp = t[0] + p[0]
    yp = t[1] + p[1]
    pp = [xp,yp]
    return pp

def transcartesiano(c,p):
    xp = c[0] + p[0]
    yp = c[1] - p[1]
    pp = [xp,yp]
    return pp

def transpantalla(c,p):
    xp = p[0] - c[0]
    yp = c[1] - p[1]
    pp = [xp,yp]
    return pp

def transcentro(c,p):
    xp = c[0] - p[0]
    yp = c[1] - p[1]
    pp = [xp,yp]
    return pp

    xp = c[0] + p[0]
    yp = c[1] - p[1]
    pp = [xp,yp]
    return pp

def transpantalla(c,p):
def transoriginal(c,p):
    xp = c[0] + p[0]
    yp = c[1] + p[1]
    pp = [xp,yp]
    return pp

def rotar(r,p):
    coseno = math.cos(math.radians(r))
    seno = math.sin(math.radians(r)) 
    xp = p[0]*coseno - p[1]*seno
    yp = p[0]*seno + p[1]*coseno
    pp = [xp,yp]
    return pp

def rotar2(r,p):
    coseno = math.cos(math.radians(r))
    seno = math.sin(math.radians(r)) 
    xp = p[0]*coseno + p[1]*seno
    yp = p[1]*coseno - p[0]*seno
    pp = [xp,yp]
    return pp

def escalar(p,e):
    xp = p[0]*e[0]
    yp = p[1]*e[1]
    pp = [xp,yp]
    return pp

def polar(cartersiana):
    r = math.sqrt(math.pow(cartersiana[0],2) + math.pow(cartersiana[1],2))
    a = math.degrees(math.asin(cartersiana[1]/r))
    pp = [a,r]
    return pp

def cartersiana(polar):
    x = polar[1] * math.cos(math.radians(polar[0]))
    y = polar[1] * math.sin(math.radians(polar[0]))
    pp = [x,y]
    return pp