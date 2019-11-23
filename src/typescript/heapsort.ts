// TODO: construir

// Leia o arquivo.

// FUNÇÕES

// Solução para tornar a função de embaralhar disponível em toda a aplicação
// Array.prototype.shuffle = function() {

//     let indice = this.length;
  
//     while(indice) {
  
//       const indiceAleatorio = Math.floor(Math.random() * indice);
//       indice--;
//       [this[indice], this[indiceAleatorio]] = [this[indiceAleatorio], this[indice]];
//     }
//     return this;
//   }

function heapify(vetor: number[], tamanho_do_vetor: number, indice_atual: number) {
  let maior: number = indice_atual;
  let filho_da_direita: number = (2 * indice_atual) + 1;
  let filho_da_esquerda: number = (2 * indice_atual) + 2;

  if (filho_da_esquerda < tamanho_do_vetor && vetor[indice_atual] < vetor[filho_da_esquerda]) {
    maior = filho_da_esquerda;
  }

  if (filho_da_direita < tamanho_do_vetor && vetor[maior] < vetor[filho_da_direita]) {
    maior = filho_da_direita;
  }

  if (maior != indice_atual) {
    const var_auxiliar = vetor[maior];
    vetor[indice_atual], vetor[maior] = vetor[maior], vetor[indice_atual];

    heapify(vetor, tamanho_do_vetor, maior);
  }
}

function heapSort(vetor: number[]) {
  let tamanho_do_vetor: number = vetor.length;

  for (let indice_atual: number = tamanho_do_vetor; indice_atual >= 0; indice_atual--) {
    heapify(vetor, tamanho_do_vetor, indice_atual);
  }

  for (let indice_atual: number = tamanho_do_vetor - 1; indice_atual > 0; indice_atual--) {
    vetor[indice_atual], vetor[0] = vetor[0], vetor[indice_atual];
    heapify(vetor, indice_atual, 0);
  }
}

// MAIN

let vetor: number[] = [];
for (let i: number = 1; i <= 20; i++) {
  vetor.push(i);
}

// vetor.shuffle();

console.log('Embaralhando vetor de 1 até 20...');
setTimeout('', 1000);
console.log('Vetor embaralhado -> ', vetor);

heapSort(vetor);
const vetor_ordenado = vetor;

console.log('\nOrdenando o vetor com HeapSort...')
setTimeout('', 1000);
console.log('Vetor ordenado -> ', vetor_ordenado)