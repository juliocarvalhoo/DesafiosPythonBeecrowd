import numpy as np

"""Xi,Yi  Posição inicial.   Xf,Yf Posição final"""

xi,yi,xf,yf = [int(x) for x in input().strip().split(" ")]


#CRIACAO DA MATRIZ
matriz8x8 = np.zeros((8,8), dtype=object)

for i in range(8):
    for j in range(8):
        matriz8x8[i][j] = (i+1,j+1)

#POSSIBILIDADE DE MOVIMETACAO NO TABULEIRO
horizontal  = [(xi,y) for y in range(1,9) ]
vertical = [(x,yi) for x in range(1,9)]
diag_primaria = list(np.diagonal(matriz8x8, offset = -(xi - yi)))
diag_secundaria = list(np.diagonal(np.fliplr(matriz8x8), offset = -(xi + yi -9)))

caminhos_dama = set(horizontal+vertical+diag_primaria+diag_secundaria)

if xi == xf and yi == yf:
    print(0) 

elif (xf,yf) in caminhos_dama:
    print(1)
else:
    print(2)