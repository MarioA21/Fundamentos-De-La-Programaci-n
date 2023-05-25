from fractions import Fraction
nom = input("Ingresa tu nombre: ")
C1 = int(input(nom + ", Ingresa el número de columnas: "))
F1 = int(input(nom + ", Ingresa el número de filas: "))
A = [[0 for a in range (C1)] for b in range (F1)]
B = [[0 for a in range (C1)] for b in range (F1)]
C = [[0 for a in range (C1)] for b in range (F1)]
print("Matriz 1")
for a in range (F1):
    for b in range (C1):
        A[a][b]=int(input(nom + ", Ingresa los valores de la matriz 1:  "))
print("Matriz 2")
for a in range (F1):
    for b in range (C1):
        B[a][b]=int(input(nom + ", Ingresa losM M valores de la matriz 2:  "))
for a in range (F1):
    for a in range (C1):
        C[a][b] = A[a][b] + B[a][b]
print("Suma de las matrices")
for a in range (F1):
    for b in range (C1):
        print(C[a][b])
print(nom + ", el resultado de la suma de las dos matrices")