from math import fabs
from math import sqrt
from sys import exit
import numpy as np

def symmetricMatrix(A):
	"""Calcula la matriz simetrica de A"""

	for i in range(len(A)):
		for j in range(i+1,len(A)):
			if A[i][j] != A[j][i]:
				return False
	return True

def diagonalDominante(X):
    D = np.diag(np.abs(X)) 
    S = np.sum(np.abs(X), axis=1) - D 
    if np.all(D > S):
        return True
    else:
        return False

	   
def cholesky(A):
	if not symmetricMatrix(A):
		exit('La matriz no es simetrica')
	n = len(A)
	G = [[0.0]*n for j in range(n)]
	for i in range(n):
		suma = A[i][i]
		for k in range(i):
			suma -= A[k][i]**2
		if suma < 0:
			exit('No es definida positiva')	
		A[i][i] = sqrt(suma)
		for j in range(i+1, n):
			suma = A[i][j]
			for k in range(i):
				suma -= A[k][i]*A[k][j]
			A[i][j] = suma / A[i][i]

	for j in range(n):
		for i in range(n):
			if(i > j):
				A[i][j] = 0.0
	return A



def seidel(a, x ,b):         
    if not symmetricMatrix(a):
	    exit('La matriz no es simetrica')
    if not diagonalDominante(a):
	    exit('La matriz no diagonal dominante')
    n = len(a)                    
    for j in range(0, n):         
         
        d = b[j]                   
           
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i] 
                 
        x[j] = d / a[j][j] 
                
    return x     
   
                 
n = 4                              
a = []                             
b = []         
                      
x = [0, 0, 0,0]                         
a = [[5, 1, -5,0],[1, 2, 0,0],[-2, 0, 4,1], [0, 0, 1,3]] 
b = [1,5,14,15]

 
  
 
for i in range(0, 36):             
    x = seidel(a, x, b)
    print("solucion en la iteracion: ",i)
    print(x)

print()
A = cholesky(a)
print(A)





