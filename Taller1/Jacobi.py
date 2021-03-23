import numpy as np

Limite_itera = 20

A = np.array([[5., 1., -2., 0.],
              [1., 2., 0., 0.],
              [-2., 0., 4., 1.],
              [0.0, 0., 1., 3.]])

b = np.array([1., 5., 14., 15.])


x = np.zeros_like(b)
for iteracion in range(Limite_itera):
    if iteracion != 0:
        print("iteracion {0}: {1}".format(iteracion, x))
        error = np.dot(A, x) - b
        print("Error:")
        print(error)

    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if x_new[i] == x_new[i-1]:
          break

    if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        break

    x = x_new

print("solucion:")
print(x)
error = np.dot(A, x) - b
print("Error:")
print(error)
