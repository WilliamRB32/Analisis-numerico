import sympy as sy
from sympy.functions import *
import numpy as np
import math
from sympy.functions import sin,cos

# funcion para encontrar el factorial
def fac(n):
    if n<=0:
        return 1
    else:
        return n*fac(n-1)

# aproximación por taylor
def taylor(function,c,n):
    a = 0
    b = 0
    while a <= n:
        b = b + (function.diff(x,a).subs(x,c))/(fac(a))*(x-c)**a
        a += 1
    return b

def cifras(x, digits=6):
    if x == 0 or not math.isfinite(x):
        return x
    digits -= math.ceil(math.log10(abs(x)))
    return round(x, digits)


if __name__ == '__main__':


    #x = 0.005
    #x = 0.0001
    x =  0.499999999
    
    # Función que se va a aproximar
    funcion = ln(1 + 2*(x))

    func = taylor(funcion,-0.5,0.5) #Limites en -0.5 y 0.5
    print("La funcion 'f(x)' es: f(x) = ln(1 + 2x)")

    # evaluar en x
    y = 1

    print("\nResultado funcion evaluada en x =",x,":",cifras(func.subs(x,y),9))