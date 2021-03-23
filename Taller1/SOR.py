import numpy as np

def SOR(A, b, w, valor_incial, criterioCon):
  
    iteracion = 0
    phi = valor_incial[:]
    residuo = np.linalg.norm(np.matmul(A, phi) - b)  
    while residuo > criterioCon:
        for i in range(A.shape[0]):
            sigma = 0
            for j in range(A.shape[1]):
                if j != i:
                    sigma += A[i, j] * phi[j]
            phi[i] = (1 - w) * phi[i] + (w / A[i, i]) * (b[i] - sigma)
        residuo = np.linalg.norm(np.matmul(A, phi) - b)
        iteracion += 1
        print("iteracion {} residuo: {:10.6g}".format(iteracion, residuo))
    return phi


tol = 1e-8
w = 1.96453 

A = np.array([[5, 1, -2, 0],
              [1, 2, 0, 0],
              [-2, 0, 4, 1],
              [0, 0, 1, 3]])

b = np.array([1, 5, 14, 15])

valor_incial = np.zeros(4)

phi = SOR(A, b, w, valor_incial, tol)
print(phi)
print ("W = ",w)
