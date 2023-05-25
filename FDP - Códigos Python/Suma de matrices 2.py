def suma_matrices(matriz_a, matriz_b):
   
    if len(matriz_a) != len(matriz_b) or len(matriz_a[0]) != len(matriz_b[0]):
        raise ValueError("Las matrices deben tener la misma dimensión")

    resultado = []
    for i in range(len(matriz_a)):
        fila = []
        for j in range(len(matriz_a[0])):
            fila.append(matriz_a[i][j])
        resultado.append(fila)

    for i in range(len(matriz_b)):
        for j in range(len(matriz_b[0])):
            resultado[i][j] += matriz_b[i][j]

    return resultado
