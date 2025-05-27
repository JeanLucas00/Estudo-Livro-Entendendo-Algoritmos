
#Recursão é quando uma função chama a si mesma

#caso-base e caso recursivo

def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i - 1)

regressiva(40)