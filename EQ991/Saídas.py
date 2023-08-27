import trab_energia as energia
import trab_Massa as massa
10
#Entrada -> Número de estágios // 
estag=int(input('Digite número de pratos: '))        

#Saída -> Temperatura em cada estágio //
print('\n',' ****** TEMPERATUA EM CADA ESTÁGIO ****** ')
matriz1=energia.energia(estag)
for k in range(1,estag+1):
    print('  A temperatura no prato {} é {:.6f} °C'.format(k,matriz1[k,6]))

#Saída -> Fração CH3CL cada estágio por fase
print('\n   ****** CONCENTRAÇÃO CH3CL CADA PRATO ******')
matriz2=massa.massa(estag)
for k in range(1,estag+1): 
    print('  A concentração do organoclorado no prato {} é {:.8f} na água e {:.8f} no ar.'.format(k,matriz2[k,6],matriz2[k,6]))