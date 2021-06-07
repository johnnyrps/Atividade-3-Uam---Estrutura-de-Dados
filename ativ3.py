"""
Implemente um projeto no qual serão inseridos números de forma ordenada, e que atenda as especificações a
seguir:

Passo 1: Insira os números [1, 2, 3, 4 e 5] em uma lista - com 5 células;
Passo 2: Remova todos os dados da lista e insira-os em uma Pilha - com 5 células.
    Deve-se sempre remover os dados da célula inicial da lista;
Passo 3: Remova os dados da Pilha e insira-os em uma Fila - com 10 células);
Passo 4: Insira os números [6, 7, 8, 9 e 10] na lista;
Passo 5: Repita os passos 2 e 3.
Passo 6: Exiba todos os números que foram inseridos na fila.

Analise a ordem dos números exibidos e verifique se estão na mesma forma que foram inseridos.
Se a exibição foi diferente, justifique o ocorrido.

O programa desenvolvido pelo aluno e a sua justificativa deverá ser postado em um ambiente virtual.
Esse programa será avaliado pelo tutor responsável pela disciplina.
"""


class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, dado):
        return self.dados.append(dado)

    def desempilha(self):
        return self.dados.pop(-1)

    def imprime_pilha(self):
        for i in range(len(self.dados)):
            print(self.dados[i], end=' ')
        print('')

    def quantos_elementos(self):
        return len(self.dados)

    def e_vazia(self):
        if len(self.dados) == 0:
            return True
        else:
            return False


class Fila(object):
    def __init__(self):
        self.dados = []

    def insere(self, dado):
        self.dados.append(dado)

    def retira(self):
        self.dados.pop(0)

    def insere_na_posicao(self, posicao, dado):
        self.dados[posicao] = dado

    def insere_no_inicio(self, dado):
        self.dados.insert(0, dado)
        self.dados.pop(-1)

    def imprime_fila(self):
        for i in range(len(self.dados)):
            print(self.dados[i], end=' ')
        print(' ')

    def quantos_elementos(self):
        return len(self.dados)

    def e_vazia(self):
        if len(dados) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    # Passo 1
    print('Passo 1: ')
    lista = [1, 2, 3, 4, 5]
    print(lista)

    # Passo 2
    print('Passo 2: ')
    pilha1 = Pilha()
    for _ in range(len(lista)):
        pilha1.empilha(lista[0])
        lista.pop(0)
    pilha1.imprime_pilha()
    print(f'A pilha contém {pilha1.quantos_elementos()} elementos.')

    # Passo 3
    print('Passo 3: ')
    fila1 = Fila()
    # Criando lista com 10 elementos.
    for _ in range(10):
        fila1.insere('')
    print(f'A fila contem {fila1.quantos_elementos()} elementos.')
    for i in range(pilha1.quantos_elementos()):
        fila1.insere_no_inicio(pilha1.desempilha())
    fila1.imprime_fila()

    # Passo 4
    print('Passo 4: ')
    lista = [6, 7, 8, 9, 10]
    print(lista)

    # Passo 5
    print('Passo 5: ')
    for _ in range(len(lista)):
        pilha1.empilha(lista[0])
        lista.pop(0)
    pilha1.imprime_pilha()
    print(f'A pilha contém {pilha1.quantos_elementos()} elementos.')

    print(f'A fila contem {fila1.quantos_elementos()} elementos.')
    for i in range(pilha1.quantos_elementos()):
        fila1.insere_no_inicio(pilha1.desempilha())
    fila1.imprime_fila()

    # Passo 6
    print('Passo 6: ')
    fila1.imprime_fila()
