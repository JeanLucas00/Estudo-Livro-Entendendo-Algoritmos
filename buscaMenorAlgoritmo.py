def buscaMenor(arr):
    menor = arr[0]  #Armazena o menor valor
    menor_indice = 0    #Armazena o indice do menor valor

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice



def ordenacaoPorSelecao(arr):   #Ordenações em um Array
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)     #Encontra o menor elemento do Array e adiciona ao novo Array
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))
