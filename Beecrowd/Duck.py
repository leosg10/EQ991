# BeeCrowd - Desafio 1163 'Angry Ducks'
import math
#fres
while True:
    try:
        h=float(input())
        d1,d2=(int(i) for i in input().split())
        tries=int(input())

        g = 9.80665
        pi = 3.14159

        def med(v,ang,h):
            vy=v*math.sin(ang*pi/180)
            vx=v*math.cos(ang*pi/180)
            tempo = vy/g+math.sqrt((2*(h+vy**2/(2*g)))/g)
            s_x=vx*tempo
            return(s_x)

        def saida(d1,d2,v,ang,h):
                x=med(v,ang,h)
                if x <d1 or x>d2:
                    print('{:.5f} -> NUCK'.format(x))
                else:
                    print('{:.5f} -> DUCK'.format(x))

        for i in range(tries):
            ang,v = (float(j) for j in input().split())
            saida(d1,d2,v,ang,h)
    except EOFError:
        break



