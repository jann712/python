# python
Projetos de Python: 

FILTRO DE RESTAURANTE POR NOTA E DISTÂNCIA

  Juntamente ao meu grupo da FIAP conseguimos montar um código que permite a organização de restaurantes pelos critérios de avaliação e distância, caso haja um empate.
  
  Ao criar uma lista com índices de nome, review e distância respectivamente e atribuí-la o nome "restaurants_list", você obteria uma lista organizada dos restaurantes.
  
 
     #Ínicio

    def orderByDistance(item):
        return item['distance'] 

    def orderByReview(item):
        return item['review']

    restaurants_list.sort(key=orderByReview, reverse=True)

    temp = []
    x = 1



    for restaurant in restaurants_list:
        if x < len(restaurants_list) - 1:
            if restaurant['review'] == restaurants_list[x]['review']:
                if restaurant['distance'] > restaurants_list[x]['distance']:
                    temp.append(restaurant)
                    temp.append(restaurants_list[x])
                    restaurants_list.insert(x, temp[0])
                    restaurants_list.insert(x - 1, temp[1])
                    temp = []


                    for restaurant in restaurants_list:
                        o = 0
                        z = 1
                        y = 0
                        while z < len(restaurants_list):
                            if restaurant['name'] == restaurants_list[z]['name']:
                                y += 1

                                if y > 1:
                                    while restaurant['review'] != restaurants_list[o]['review']:
                                        o += 1
                                    if restaurants_list[o]['distance'] > restaurants_list[o + 1]['distance']:
                                        restaurants_list.remove(restaurants_list[z])
                                    else:
                                        restaurants_list.reverse()
                                        restaurants_list.remove(restaurants_list[z])
                                        restaurants_list.reverse()

                                    z -= 1

                            z += 1

            x += 1


    for restaurant in restaurants_list:
        print(restaurant['name'], restaurant['review'], restaurant['distance'])



MULTIPLICAÇÃO DE MATRIZES

O código a seguir cria e multiplica matrizes, com as funções 'cria_matriz' e 'multi_matrizes'

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
