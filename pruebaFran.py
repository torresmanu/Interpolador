def sumita(listaDatos,listaDominio):
    matriz = []
    numero_filas = len(listaDatos)
    numero_columnas = len(listaDatos)+1

    for i in range(numero_filas):
        matriz.append([])
        for j in range(numero_columnas):
            matriz[i].append(None)

    for i in range(numero_filas):
        for j in range(numero_columnas):
            matriz[i][j] = (0,1,1)

    for i in range(numero_filas): #datos iniciales
            matriz[i][0] = listaDominio[i]
            matriz[i][1] = listaDatos[i]


    for i in range(1,numero_filas):
        matriz[i-1][2] = ( (matriz[i][1] - matriz[i-1][1] )/ ( matriz[i][0]-matriz[i-1][0] ),matriz[i][0],matriz[i-1][0] )



    contador = 1
    for j in range(3,numero_columnas):
        #contador+=1
        for i in range(1,numero_filas-contador):
            matriz[i-1][j] = ( (matriz[i][j-1][0]- matriz[i-1][j-1][0])/(matriz[i][j-1][1]-matriz[i-1][j-1][2]) ,matriz[i][j-1][1],matriz[i-1][j-1][2])
        contador += 1


    for i in range (len(listaDatos)):
        print(matriz[i])

    return matriz

"""
    for h in range(1,numero_columnas):
        for i in range(numero_filas-1):
            matriz[i][h] = (matriz[i+1][h-1]-matriz[i][h-1])
"""

sumita([0,8,27,125,216],[0,2,3,5,6])
print("---------------")
sumita([0,8,27],[0,2,3])
print("---------------")
sumita([0,8],[0,2])