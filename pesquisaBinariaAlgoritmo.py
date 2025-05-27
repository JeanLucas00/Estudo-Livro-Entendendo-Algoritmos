def pesquisaBinaria(lista, item):
    baixo = 0   #baixo e alto acompanham a parte da lista que você está procurando.
    alto = len(lista) - 1

    while baixo <= alto:    #Enquanto ainda não conseguiu chegar a um único elemento...

        meio = (baixo + alto) // 2  #verica o elemento central.
        chute = lista[meio]

        if chute == item:   #Acha o item.
            return meio


        if chute > item:    #O chute foi muito alto
            alto = meio - 1
        else:   #O chute foi muito baixo.
            baixo = meio + 1
    return None     #Retorna None se o item não existir na lista

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(pesquisaBinaria(lista, 5))
print(pesquisaBinaria(lista, 15))