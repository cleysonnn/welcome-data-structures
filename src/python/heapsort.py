# TODO: comentar

# Cógigo comentado em português, 
# para melhor entendimento da estrutura
# pelo público não bilingue.

########## FUNÇÕES ##########

from random import shuffle
from time import sleep

def heapify(vetor, tamanho_do_vetor, indice_atual):
  maior = indice_atual
  filho_da_esquerda = (2 * indice_atual) + 1
  filho_da_direita = (2 * indice_atual) + 2

  if filho_da_esquerda < tamanho_do_vetor and vetor[indice_atual] < vetor[filho_da_esquerda]:
    maior = filho_da_esquerda
  
  if filho_da_direita < tamanho_do_vetor and vetor[maior] < vetor[filho_da_direita]:
    maior = filho_da_direita

  if maior != indice_atual:
    vetor[indice_atual], vetor[maior] = vetor[maior], vetor[indice_atual]

    heapify(vetor, tamanho_do_vetor, maior)

def heapSort(vetor):
  tamanho_do_vetor = len(vetor)

  for indice_atual in range(tamanho_do_vetor, -1, -1):
    heapify(vetor, tamanho_do_vetor, indice_atual)

  for indice_atual in range(tamanho_do_vetor-1, 0, -1):
    vetor[indice_atual], vetor[0] = vetor[0], vetor[indice_atual]
    heapify(vetor, indice_atual, 0)

########## MAIN ##########

vetor = list(range(1,21))
shuffle(vetor)

print('Embaralhando vetor de 1 até 20...')
sleep(1)
print('Vetor embaralhado -> ', vetor)

heapSort(vetor)
vetor_ordenado = vetor

print('\nOrdenando o vetor com HeapSort...')
sleep(1)
print('Vetor ordenado -> ', vetor_ordenado)