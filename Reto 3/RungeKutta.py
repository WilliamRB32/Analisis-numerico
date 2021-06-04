import math
import matplotlib.pyplot as plt

N = 48223786
S = N-34709 - 197
I = 34709
R = 197
taxis=[ ]
xaxis=[ ]
yaxis=[ ]
zaxis=[ ]
beta=0.185/N
gamma=0.022
dt=0.001
t = 0
cnt=0

while t<200:
    if cnt%100==0:
        taxis.append(t)
        xaxis.append(S)
        yaxis.append(I)
        zaxis.append(R)
# Paso 1 RungeKutta
    kx1 = - beta*S*I
    ky1 = beta*S*I - gamma*I
# Paso 2 RungeKutta
    t2 = t+dt
    x2 = S + kx1*dt
    y2 = I + ky1*dt
    kx2 = - beta*x2*y2
    ky2 = beta*x2*y2 - gamma*y2
# Ingreso de los datos en S, I y N
    S = S + (kx1+kx2)*dt/2
    I = I + (ky1+ky2)*dt/2
    R = N - S - I
    t = t + dt
    cnt = cnt + 1
    
plt.title("MODELO SIR RUNGE KUTTA")
plt.plot(taxis,xaxis,  linewidth=1.0, label='S')
plt.plot(taxis,yaxis,  linewidth=1.0, label='I')
plt.plot(taxis,zaxis,  linewidth=1.0, label='R')
plt.xlim(0,200)
plt.legend()
plt.xlabel('DIAS')
plt.grid(True)
plt.show()
print(xaxis)
