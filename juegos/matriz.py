import numpy as np

file = 'matriz.csv'
matriz = np.loadtxt(file,delimiter=';').astype(int)

def mapa(pos_pacman,move):
    # valido si se mueve a la derecha
    vandera = [False,pos_pacman]
    x = pos_pacman[0]
    y = pos_pacman[1]
    print (pos_pacman)
    matriz[x][y] = 1

    if move == 0 and matriz[x][y+1] == 1:
        vandera[0] = True
        vandera[1] = (x,y+1)
        matriz[x][y+1] = 2

    if move == 1 and matriz[x][y-1] == 1:
        vandera[0] = True
        vandera[1] = (x,y-1)   
        matriz[x][y-1] = 2 

    if move == 2 and matriz[x+1][y] == 1:
        vandera[0] = True
        vandera[1] = (x+1,y)
        matriz[x+1][y] = 2 

    if move == 3 and matriz[x-1][y] == 1:
        vandera[0] = True
        vandera[1] = (x-1,y)   
        matriz[x-1][y] = 2     

    print (matriz[x])       

    return vandera



