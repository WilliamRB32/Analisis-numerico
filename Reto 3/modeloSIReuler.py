from numpy import zeros, linspace
import matplotlib.pyplot as plt
import pandas as pd
from openpyxl import load_workbook

xl = pd.ExcelFile("CasosCovid.xlsx")
df = xl.parse("Hoja1")
Infectados = 0
Recuperados = 0

#   Se realiza la lectura del excel con los datos de contagio de covid 

for i in range(1995):
    x = df['Covid'][i]
    aux = x.split(',')
    if aux[10] == 'Recuperado':
        Recuperados = Recuperados + 1
    if aux[10] == 'Leve' or aux[10] == 'Moderado' or aux[10] == 'Grave':
        Infectados = Infectados + 1

# Unidad de tiempo: DIAS
beta = 0.185/48223786 # Tasa de infección.

gamma = 0.022 # Tasa de recuperación.
dt = 0.1             
D = 10               # Simulado por D dias
N_t = int(D*24/dt)   
t = linspace(0, N_t*dt, N_t+1)
S = zeros(N_t+1)
I = zeros(N_t+1)
R = zeros(N_t+1)

# Condiciones iniciales
S[0] = 48223786 - 34709 - 197
I[0] = 34709
R[0] = 197

# Ecuación realizada con el metodo de Euler
for n in range(N_t):
    S[n+1] = S[n] - dt*beta*S[n]*I[n]
    I[n+1] = I[n] + dt*beta*S[n]*I[n] - dt*gamma*I[n]
    R[n+1] = R[n] + dt*gamma*I[n]

# Mostrar la grafica resultante del modelo.
fig = plt.figure()
print(beta)
plt.title("MODELO SIR EULER")
l1, l2, l3 = plt.plot(t, S, t, I, t, R,linewidth=1.0)
fig.legend((l1, l2, l3), ('S', 'I', 'R'), 'center right')

plt.xlabel('DIAS')
plt.grid(True)
plt.show()
