import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def f(x):
    return x**3-2*x**2+(4/3)*x-(8/27)

def brent(f, a, b, tol, maxItera):
    c = a
    n = 0
    arr = []
    while (abs(c-b)>tol*(abs(b)+1) or ((n< maxItera) or (f(b)> tol))):
        n = n+1
        x = 0
        if np.complex128((a) * f(b)) < 0:
            a, b, x = secante(f, a, b)
        else:
            if(iteraSecante(a, b, c, f) is True):
                a, b, x = secante(f, a, b)
            else:
                b = b-0.5*(c-b)
                c, b = metodobiseccion(f, c, b)
        if np.complex128(f(a) * f(b)) < np.complex128(0):
            c = a
        arr.append(b)
        
        if(np.complex128(f(b))<tol):
            return (n,b,arr)
        if(type(b)=='complex'):
                return (n,b,arr)
        else:
                return (n,b,arr)
        
    return (n,b,arr)
        

#Comprueba si el resultado está en el otro intervalo
def iteraSecante(a, b, c, f):
    x2 = 0 
    x22 = 0
    x2 = secante (f, a, b)[2]
    x22 = secante (f, c, b)[2]
    if(x2 == x22):
        return True
    else:
        return False
    
def secante (f, x0, x1):
    x2 = 0 
    if abs(f(x1)) != abs(f(x0)):
        x2 = np.complex128(x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0))))
        x0 = np.complex128(x1)
        x1 = x2
    return (x0, x1, x2)


def metodobiseccion(f, x0, x1):
    x2 = 0
    x2=np.float128((x0+x1)/2)
    if f(x0)*f(x2)>0: 
        x0=x2
    else:
        x1=x2
    return (x0, x1)


#tolerancias = [10**-8, 10**-16, 10**-32]
numeros = []
itera = []


numeros = brent(f, -2, 2, 10**-8, 10)[2]
itera = brent(f, -2, 2, 10**-8, 100)
    
print("Iteraciones: ",itera[0])
print("Resulado: ", itera[1])

