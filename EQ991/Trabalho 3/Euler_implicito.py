import matplotlib.pyplot as plt
import main

# Todos parametros fornecidos
C_a0 = 1.8
C_a1 = 0.4
C_a2 = 0.2
C_a3 = 0.1
tau_1 = 10
tau_2 = 15
tau_3 = 20
k = 0.15

# Valores para diferentes passos de integração
EI_1 = main.Euler_implicito(40, C_a1, C_a2, C_a3, 1)     # Passo 1 minuto
EI_2 = main.Euler_implicito(40, C_a1, C_a2, C_a3, 2)     # Passo 2 minutos
EI_5 = main.Euler_implicito(40, C_a1, C_a2, C_a3, 5)      # Passo 5 minutos
EI_10 = main.Euler_implicito(40, C_a1, C_a2, C_a3, 10)    # Passo 10 minutos

# Gráficos
fig, axs = plt.subplots(2, 2, layout='constrained')
axs[0, 0].plot([i for i in range(40)], EI_1, linewidth=2,
               marker='.', label=("$C_{A1}$", "$C_{A2}$", "$C_{A3}$"))
axs[0, 0].set_title('\u0394 = 1 minuto', fontsize=10)
axs[0, 1].plot([i for i in range(0, 40, 2)], EI_2, linewidth=2,
               marker='.', label=("$C_{A1}$", "$C_{A2}$", "$C_{A3}$"))
axs[0, 1].set_title('\u0394 = 2 minutos', fontsize=10)
axs[1, 0].plot([i for i in range(0, 40, 5)], EI_5, linewidth=2,
               marker='.', label=("$C_{A1}$", "$C_{A2}$", "$C_{A3}$"))
axs[1, 0].set_title('\u0394 = 5 minutos', fontsize=10)
axs[1, 1].plot([i for i in range(0, 40, 10)], EI_10, linewidth=2,
               marker='.', label=("$C_{A1}$", "$C_{A2}$", "$C_{A3}$"))
axs[1, 1].set_title('\u0394 = 10 minutos', fontsize=10)

fig.suptitle('Método de Euler Implicito')
for ax in axs.flat:
    ax.set_xlabel('Tempo (minutos)', fontsize=9)
    ax.set_ylabel('Concentração ($kgmol/m^3$)', fontsize=9)
    ax.grid(True)
    ax.legend(loc='upper right')
    ax.set_xlim(0)

# plt.tight_layout()
plt.show()
