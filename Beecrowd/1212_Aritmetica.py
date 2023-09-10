# BeeCrowd - 1212 -Aritmética Primária

while True:
    n1, n2 = (i for i in input().split())
    if n1 == '0' and n2 == '0':
        break
    
    if len(n1) <= len(n2):
        menor = n1
        maior = n2
    else:
        menor = n2
        maior = n1
        
    resto = 0
    carry = 0

    for i in range (len(menor)):
        saldo = int(n1[-1-i]) + int(n2[-1-i]) + resto
        if saldo > 9:
            carry += 1
            resto = 1
        else:
            resto = 0

    for i in maior[-1-len(menor): -len(maior) - 1: -1]:
        saldo = int(i) + resto
        if saldo > 9:
            carry += 1
            resto = 1
        else:
            break
                
    if carry == 0:
        print('No carry operation.')
    elif carry == 1:
        print('{} carry operation.'.format(carry))
    else:
        print('{} carry operations.'.format(carry))
