n=2

A=[]
valor = 4.23
for i in range (n):
    valor = valor + i + 0.21
    A.append([valor]*n)
    print (A[i])
    
resultado = 0    
for i in range(n):
    for j in range (n):
        resultado = resultado + A[i][j]

print ("Resultado para n=2: ",resultado)

n=3

A=[]
valor = 4.23
for i in range (n):
    valor = valor + i + 0.21
    A.append([valor]*n)
    print (A[i])
    
resultado = 0    
for i in range(n):
    for j in range (n):
        resultado = resultado + A[i][j]

print ("Resultado para n=3: ",resultado)

n=4

A=[]
valor = 4.23
for i in range (n):
    valor = valor + i + 0.21
    A.append([valor]*n)
    print (A[i])
    
resultado = 0    
for i in range(n):
    for j in range (n):
        resultado = resultado + A[i][j]
       

print ("Resultado para n=4: ",resultado)

