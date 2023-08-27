
def leitura(n):
    gastos=[]
    diferença=[]
    for i in range(n):
        gastos.append(float(input())) #gastos -> lista com valores pagos de cada viajante
    soma=sum(gastos)
    ind=soma/n
    for j in gastos:
        diferença.append(j-ind)
    return(diferença) #diferença -> lista com a diferença de valor de cada viajante

def splitwise(n):
    diferença=leitura(n)
    dinheiro=0
    for i in diferença:
        if i<0:
            dinheiro+=abs(i)
    print('${:.2f}'.format(dinheiro))

while True:
    n=int(input('viajantes: '))
    if n==0:
        break
    splitwise(n)

