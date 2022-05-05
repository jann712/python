def cria_matriz(num_linhas,num_colunas):
    matriz = []
    lin = 0
    col = 0

    for i in range(int(num_linhas)):
        linha = []

        for j in range(int(num_colunas)):
            linha.append(str(lin) + str(col))
            col += 1

        matriz.append(linha)
        lin += 1
        col = 0

    return matriz

def multi_matrizes(matriz1, matriz2):
    if len(matriz1[0]) == len(matriz2):
        matriz3 = cria_matriz(len(matriz1), len(matriz2[0]))
        n_linha = 0
        
        for linha in matriz3:    
            y = 0
            for coluna in linha:
                temp = 0
                x = 0
                while x < len(matriz2):
                    temp += matriz1[int(coluna[0])][x]*matriz2[x][int(coluna[1])]
                    x += 1

                matriz3[n_linha][y] = temp
                print(matriz3)

                y += 1

            n_linha += 1

        return(matriz3)

a = [[3, 2], [5, -1]]
b = [[6, 4, -2], [0, 7, 1]]


print(multi_matrizes(a, b))
