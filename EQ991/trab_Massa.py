import numpy as np
import math
import trabalho_func as trab

#Constantes Calculadas (SI):
v_agua = (100000/18.02)*(1000/3600) #kg/s
v_ar = (10000/28.97)*(1000/3600)    #kg/s
T_ar = 400+273.15   #K
T_agua = 20+273.15  #K
Cp_agua = 75.39  #j/(mol.K)
Cp_ar = 29.09    #j/(mol.K)
tc= 416.3 #K
pc= 67   #bar
po=1.033 #bar
ef=0.5

#Parametros p/ Balanço de massa:
def P_sat(t):
    x=1-(t+273.15)/tc
    p=pc*math.exp((1/(1-x))*(-6.86672*x+1.52273*x**1.5-1.92919*x**3-2.61459*x**6))
    return p
def y_inf (t):
    y_20= 1.265+0.64+0.073
    y=10**((20+273.15)/(t+273.15)*y_20)
    return y
def K (t):
    K=P_sat(t)*y_inf(t)/po
    return K

#Balanço Massa:
def massa(estag):
    temp= trab.energia(estag)[:,6]
    matriz=np.zeros((estag+2,8))
    matriz[0]=[0,1,0,0,0,0,0,0]                   #Estágio '0'
    matriz[estag+1,6]=0.001*ef*K(temp[estag+1])   #Condição Contorno
        
    for i in range(1,estag+1):
        matriz[i,0]= v_ar+v_agua*(1-ef)/(ef*K(temp[i]))                             #A_i
        matriz[i,1]= -(v_ar+v_agua*(1-ef)/(ef*K(temp[i+1])+v_agua/ef*K(temp[i])))   #B_i
        matriz[i,2]= v_agua/(ef*K(temp[i+1]))                                       #C_i
        matriz[i,3]=  0                                                             #D_i   
        matriz[i,4]=matriz[i,2]/(matriz[i,1]-matriz[i,0]*matriz[i-1,4])                              #P_i
        matriz[i,5]=(matriz[i,3]-matriz[i,0]*matriz[i-1,5])/(matriz[i,1]-matriz[i,0]*matriz[i-1,4])  #Q_i

    for j in range(estag,0,-1):   #Interativo (y)
        matriz[j,6]= matriz[j,3]-matriz[j,4]*matriz[j+1,6]       
    for j in range(estag,0,-1):   #Interativo (x)
        matriz[j,7]= (matriz[j,6]-(1-ef)*matriz[j-1,6])/(ef*K(temp[j]))        

    return matriz
   