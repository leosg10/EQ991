import numpy as np
import math


#Constantes Calculadas (SI)
v_agua = (100000/18.02)*(1000/3600) #kg/s
v_ar = (10000/28.97)*(1000/3600)    #kg/s
T_ar = 400+273.15   #K
T_agua = 20+273.15  #K
Cp_agua = 75.39 #j/(mol.K)
Cp_ar = 29.09   #j/(mol.K)

#Função Balanço Energia
def energia(estag):
    matriz=np.zeros((estag+2,7))
    matriz[0]=[0,1,0,400,0,400,400]    #Estágio '0'
    matriz[estag+1,6]=20               #Condição contorno
    
    for i in range(1,estag+1):
        matriz[i,0]= v_ar*Cp_ar                             #A_i
        matriz[i,1]= -(v_agua*Cp_agua+v_ar*Cp_ar)           #B_i
        matriz[i,2]= v_agua*Cp_agua                         #C_i
        matriz[i,3]=  0                                     #D_i   
        matriz[i,4]=matriz[i,2]/(matriz[i,1]-matriz[i,0]*matriz[i-1,4])                            #P_i
        matriz[i,5]=(matriz[i,3]-matriz[i,0]*matriz[i-1,5])/(matriz[i,1]-matriz[i,0]*matriz[i-1,4])  #Q_i

    for j in range(estag,0,-1):   #Interativo
        matriz[j,6]= matriz[j,5]-matriz[j,4]*matriz[j+1,6]        
    return matriz
