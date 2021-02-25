# FUNCION A RESOLVER

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1, 2, 0.1)
tolerancia = [10**-8, 10**-16, 10**-32, 10**-56]


def f(x):
    return x**3-2*x**2+(4/3)*x-(8/27)


def secant(x0,x1,e,N):
    step = 1
    con = True
    funcion = []
    valores = np.arange(x0, x1, 0.1)
    
    for k in valores:
        funcion.append(f(k))

    while con:
        if f(x0) == f(x1):
            print('Error, No se pude dividir en cero')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Iteracion-%d, x2 = %0.8f Y f(x2) = %0.8f ' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step <= 3:
            tol = str(e)
            x =[x0, x1, x2]
            y =[f(x0), f(x1), f(x2)]
            plt.plot(valores,funcion)
            plt.plot(x, y)
            plt.title("Metodo de la secante en xsin(x)-1 con tol: " + tol)
            plt.ylabel("F(x)")
            plt.xlabel("x")
            plt.show()
        
        if step > N:
            print('No Convergente')
            break
        
        con = abs(f(x2)) > e
    print('\n Resultado de la raiz: %0.8f' % x2)




##Gráfica de la funcion
funcion = []
for k in x:
    funcion.append(f(k))
    
plt.plot(x,funcion)
plt.show()



x0 = 0.5
x1 = 2
N = 12
#secant(x0,x1,10**-8,N)

for i in tolerancia:
    print("Tolerancia: ", i)
    secant(x0,x1,i,N)

    

#x = np.arange(0,10,0.1)



