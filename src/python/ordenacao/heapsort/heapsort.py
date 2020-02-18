# TODO: comentar

# Cógigo comentado em português,
# para melhor entendimento da estrutura
# pelo público brasileiro.

from sys import argv
from random import shuffle
# from time import sleep

########## FUNÇÕES DO ALGORITMO DE ORDENAÇÃO ##########


def heapify(vetor, tamanho_do_vetor, indice_atual):
    maior = indice_atual  # maior = 10
    filho_da_esquerda = (2 * indice_atual) + 1  # 20 + 1 = 21
    filho_da_direita = (2 * indice_atual) + 2  # 20 + 2 = 22

    if filho_da_esquerda < tamanho_do_vetor and vetor[indice_atual] < vetor[filho_da_esquerda]:
        maior = filho_da_esquerda

    if filho_da_direita < tamanho_do_vetor and vetor[maior] < vetor[filho_da_direita]:
        maior = filho_da_direita

    if maior != indice_atual:
        vetor[indice_atual], vetor[maior] = vetor[maior], vetor[indice_atual]

        heapify(vetor, tamanho_do_vetor, maior)


def heapSort(vetor):  # vetor = [2, 4, 6, 5, 8, 10, 1, 7, 9, 3]
    tamanho_do_vetor = len(vetor)  # tamanho_do_vetor = 10

    # (tamanho_do_vetor, parada, passo) # indice_atual = 10, 9, 8,..., 2, 1, 0
    for indice_atual in range(tamanho_do_vetor, -1, -1):
        # heapfy(vetor, tamanho_do_vetor = 10, indice_atual= 10)
        heapify(vetor, tamanho_do_vetor, indice_atual)

    for indice_atual in range(tamanho_do_vetor-1, 0, -1):
        vetor[indice_atual], vetor[0] = vetor[0], vetor[indice_atual]
        heapify(vetor, indice_atual, 0)


########## FIM DAS FUNÇÕES DO ALGORITMO DE ORDENAÇÃO ##########

# def buildLista(inicio, fim):
#     vetor = list(range(inicio, fim))
#     return shuffle(vetor)


def show(inicio, fim):
    vetor = list(range(inicio, fim+1))
    shuffle(vetor)

    print('\nEmbaralhando vetor de', inicio, 'até', fim, '. . .')
    # sleep(1)
    print('\nVetor embaralhado -> ', vetor)

    heapSort(vetor)
    vetor_ordenado = vetor

    print('\nOrdenando o vetor com HeapSort . . .')
    # sleep(1)
    print('\nVetor ordenado -> ', vetor_ordenado)


########## MAIN ##########

# show(1, 100)

argumentos = argv

try:
    if argumentos[1] == 'range':
        show(int(argumentos[2]), int(argumentos[3]))
    elif argumentos[1] == 'help':
        print('para executar este programa informe o argumento "range" seguido do "valor inicial" da lista e \no "valor final" ex.: "python heapsort.py range 1 100".')
    else:
        print('Argumento inválido.\nDigite "help", ex.: "python arquivo.py help" para mais informações.')
except IndexError as error:
    print('Nenhum argumento foi passado.\nDigite "help", ex.: "python heapsort.py help" para mais informações.')
except Exception as error:
    print('Ocorreu o seguinte erro não esperado:', error,
          '\nDigite "help", ex.: "python heapsort.py help" para mais informações.')
