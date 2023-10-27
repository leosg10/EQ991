# EQ991-A – 3º Trabalho - Processos em Regime Transiente
import numpy as np

# Todos parametros fornecidos
C_a0 = 1.8
C_a1 = 0.4
C_a2 = 0.2
C_a3 = 0.1
tau_1 = 10 
tau_2 = 15
tau_3 = 20
k = 0.15


#Funções para resolução do sistema de EDO's
def Sistema(CA_0, CA1, CA2, CA3):
    f_C1 = 1/tau_1*(CA_0-CA1) - k*CA1
    f_C2 = 1/tau_2*(CA1-CA2) - k*CA2
    f_C3 = 1/tau_3*(CA2-CA3) - k*CA3
    return np.array((f_C1,f_C2,f_C3))


def Euler (Sistema, periodo, y1_0, y2_0, y3_0, h):
    matriz = np.zeros((periodo,3))  # Matriz para salvar os resultados de cada interação
    matriz[0] = [y1_0, y2_0, y3_0]  # Condições Iniciais
    y1, y2, y3 = y1_0, y2_0, y3_0
    for i in range(1, periodo):
        f = Sistema(C_a0, y1, y2, y3)
        matriz[i][0] = y1 + f[0]*h
        matriz[i][1] = y2 + f[1]*h
        matriz[i][2] = y3 + f[2]*h
        y1, y2, y3 = [valor for valor in matriz[i]]
    return matriz


def Euler_implicito (periodo, y1_0, y2_0, y3_0, h):
    matriz = np.zeros((periodo,3))  # Matriz para salvar os resultados de cada interação
    matriz[0] = [y1_0, y2_0, y3_0]  # Condições Iniciais
    y1, y2, y3 = y1_0, y2_0, y3_0
    for i in range(1, periodo):
        função = lambda y1,c,tau: (y1 + (h*c)/tau) / (1 + h/tau + h*k)  # Equação para encontrar y(n+1)
        y1 = função(y1, C_a0,tau_1)
        y2 = função(y2,y1,tau_2)
        y3 = função(y3,y2,tau_3)
        matriz[i] = [y1, y2, y3]
    return matriz

