# BeeCrowd - 1212 -Aritmética Primária
from math import sqrt

C = int(input())

for _ in range(C):
    
    N = int(input())
    
    x_0, y_0 = (int(i) for i in input().split())

    for indice in range(N):
        x, y = (int(i) for i in input().split())
        dist = sqrt(abs(x_0 - x)**2 + abs(y_0 - y)**2)
        if indice == 0:
            menor = dist
            escolha = indice + 1
        elif dist < menor:
            menor = dist
            escolha = indice + 1
                 
    print('{}'.format(escolha))