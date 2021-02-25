import math

def biseccion(f,a,b, TOL):
    if (f(a)*f(b) >= 0):
        print("You have not assumed the right interval.")
        return
    mid = a
    iteracion = 0
    while ((b-a) >= TOL):
        mid = (a+b)/2
        resultado = f(mid)
        if (resultado == 0):
            break
        if (resultado*f(a) < 0):
            b = mid
        else:
            a = mid
        iteracion += 1
        print(f'P{iteracion}: {mid:.8f}\tResultado: {resultado}')
    print(f'Resultado de la Raiz: {mid:.8f}\nIteraciones: {iteracion}')

if __name__ == '__main__':
    f = lambda x: x**3 - 2*x**2 + (4/3)*x - (8/27)
    biseccion(f, 0, 1, 0.000000001)
