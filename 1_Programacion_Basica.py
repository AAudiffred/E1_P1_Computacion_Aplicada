def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


y = 0
while y != 1:

    m = int(input("Introduzca la dimensión de la matriz A: "))
    while m < 3:
        m = int(input("La dimensión dene ser mayor o igual a 3. \nIntroduzca la dimensión de la matriz A: "))

    matrix_values = []
    x = 2
    while len(matrix_values) < m*m:
        if es_primo(x):
            matrix_values.append(x)
        x += 1

    matrix_zeros = []
    for i in range(m):
        row = []
        for j in range(m):
            row.append(None)
        matrix_zeros.append(row)

    for i in range(m):
        for j in range(m):
            matrix_zeros[i][j] = matrix_values[i*m + j]
    matrix_final = matrix_zeros

    for row in matrix_final:
        print(row)

    suma = 0
    for i in range(m):
        for j in range(i, m):
            suma += matrix_final[i][j]

    print("La suma de los elementos en la matriz diagonal superior es:", suma)
    z = str(input("¿Quiere probar otra dimensión de matriz?: "))
    if z.lower() in ["no", "nein", "non"]:
        y = 1
