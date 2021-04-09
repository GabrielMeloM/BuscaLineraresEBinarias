def busca_linear(lista, chave):
    for i in range(len(lista)):     # Percorre lista do índice 0 a n–1
        if lista[i] == chave:
            return i                # Encontrou elemento na posição i
    return -1                       # Não encontrou o elemento


def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:     # Encontrou elemento
            return meio
        elif chave > lista[meio]:    # Busca na segunda metade
            inicio = meio + 1
        else:                        # Busca na primeira metade
            fim = meio - 1
    return -1                        # Não encontrou o elemento


'''
EXERCÍCIO 1:
Implemente a função 'ordem_crescente' que recebe uma lista e retorna True caso
a lista esteja ordenada em ordem crescente e False caso contrário
'''


def ordem_crescente(lista):
    tamanho = len(lista)-1
    primeiro = 0
    segundo = 0
    for indice in range(tamanho):
        primeiro = lista[indice]
        segundo = lista[indice+1]
        if primeiro > segundo:
            return False
    return True


'''
EXERCÍCIO 2:
Implemente a função 'busca_linear_alteracao', modificando o algoritmo de
busca linear para que ele se torne um algoritmo de atualização.
Caso seja encontrado o elemento chave, ele faz a alteração para um novo valor,
passado por parâmetro.
'''


def busca_linear_alteracao(lista, chave, novo_valor):
    indice = busca_linear(lista, chave)
    if indice != -1:
        lista[indice] = novo_valor
        return lista
    return -1


'''
EXERCÍCIO 3:
Implemente a função 'busca_binaria_alteracao', modificando o algoritmo de
busca binária para que ele se torne um algoritmo de atualização.
Caso seja encontrado o elemento chave, ele faz a alteração para um novo valor,
passado por parâmetro.
'''


def busca_binaria_alteracao(lista, chave, novo_valor):
    indice = busca_binaria(lista, chave)
    if indice != -1:
        lista[indice] = novo_valor
        return indice
    return -1


'''
EXERCÍCIO 4:
Implemente a função 'insere_ordenado', que recebe uma lista ordenada de forma
crescente e um novo item que deve ser inserido na lista, de forma que a lista
continue ordenada.
Você NÃO DEVE utilizar a função sort ou qualquer outra
função pronta do python para fazer a ordenação.
'''


def insere_ordenado(lista, item):
    inicio = 0
    fim = len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        if item < lista[meio]:
            fim = meio
        else:
            inicio = meio + 1

    lista.insert(inicio, item)
