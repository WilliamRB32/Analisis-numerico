import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#np.seterr(divide='ignore', invalid='ignore')

def df_dt(x, tiempo, alpha, beta, delta, gamma):
    """Función del sistema en forma canónica"""
    dx = alpha * x[0] - beta * x[0] * x[1]
    dy = - delta * x[1] + gamma * x[0] * x[1] 
    return np.array([dx, dy])


# Parámetros
alpha = 0.1 # Tasa de crecimiento Presas
beta = 0.02 # encuentros entre depredador y presas.
gamma = 0.3 # Tasa de decrecimiento depredador
delta = 0.01   # Exito en caza
# Condiciones iniciales
x0 = 100   # Presas
y0 = 4    # Depredadores
conds_iniciales = np.array([x0, y0])
# Condiciones para integración
tf = 200
N = 800
t = np.linspace(0, tf, N)
solucion_ecuacion = odeint(df_dt, conds_iniciales, t, args=(alpha, beta, gamma, delta))

z = plt.plot(t, solucion_ecuacion[:, 0], label='presa')
w = plt.plot(t, solucion_ecuacion[:, 1], label='depredador')
plt.xlabel("Tiempo")
plt.ylabel("Numero Animales")
plt.legend()

plt.show()

x_max = np.max(solucion_ecuacion[:,0]) * 1.05
y_max = np.max(solucion_ecuacion[:,1]) * 1.05
x = np.linspace(0, x_max, 25)
y = np.linspace(0, y_max, 25)
xx, yy = np.meshgrid(x, y)
uu, vv = df_dt((xx, yy), 0, alpha, beta, gamma, delta)
norm = np.sqrt(uu**2 + vv**2)
uu = uu / norm
vv = vv / norm
plt.quiver(xx, yy, uu, vv, norm, cmap=plt.cm.gray)
plt.plot(solucion_ecuacion[:, 0], solucion_ecuacion[:, 1])
plt.xlabel("Presas")
plt.ylabel("Depredadores")
plt.show()


def C(x, y, a, b, c, d):
    return a * np.log(y) - b * y + c * np.log(x) - d * x

x = np.linspace(0, x_max, 100)
y = np.linspace(0, y_max, 100)
xx, yy = np.meshgrid(x, y)
constant = C(xx, yy, alpha, beta, gamma, delta)

plt.figure('distintas_soluciones', figsize=(8,5))
plt.contour(xx, yy, constant, 50, cmap=plt.cm.Blues)
plt.xlabel('presas')
plt.ylabel('depredadores')

plt.show()