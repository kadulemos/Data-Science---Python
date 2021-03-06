# -*- coding: utf-8 -*-
"""Python_para_Análise_de_Dados_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fCtsjWQHtBVCpy31l__5NgG8zz_NI5eY

<h2>Python para Análise de Dados - Numpy</h2>

Iremos aprender a trabalhar com a biblioteca Numpy.
"""

# Importando a biblioteca numpy
import numpy as np

# Criando um array de 1 dimensão
one_dim = np.array([1,2,3,4])

# Verificando a dimensão de um array
one_dim.ndim

# Imprimindo um array
one_dim

# Criando um array de 2 dimensões
two_dim = np.array([(1,2,3),(4,5,6)])

# Verificando a dimensão do array
two_dim.ndim

# Imprimindo o array
two_dim

# Cria um array de números aleatórios
# Um array de cinco linhas e duas dimensões
np.random.random((5,2))

# Cria um array com valores esparsos iniciando com o valor 10, menor que 50 e incrementando de 5 em 5
np.arange(10,50,5)

# Cria um array linear de 0 a 2 de no máximo 9 elementos
np.linspace(0,2,9)

# Cria um array de valores zero
# Cria um array com 3 linhas e 4 dimensões
np.zeros((3,4))

"""<h2>Numpy Arrays Vs Listas</h2>



*   Arrays Numpy permitem fazer operações em **arrays inteiros** de forma rápida;
*   Listas não permitem operações em todos os elementos da lista;
* Para operações em todos os elementos é preciso interar sobre toda a lista;
* Listas em Python armazenam diferentes tipos de objetos;
* Arrays Numpy considera todos os elementos distintos como strings.
"""

# Criando uma lista em Python
lista = [1,2,3]

# Imprimindo a lista
lista

# Multiplicar valores da lista por 2
lista * 2

# Transforme a variável lista em um array Numpy
lista = np.array(lista)

# Imprimindo a lista transformada em Array
lista

# Imprimindo o tipo do objeto
type(lista)

# Multiplicando cada elemento por 2
lista * 2

# Calcular IMC de pessoas
pesos = [67,81,120,90]
altura = [1.68,1.70,1.75,1.85]

# Fazendo o cálculo usando as listas
# Ocorre um erro pois listas não podem ser utilizadas em cálculo
pesos / altura ** 2

# Transforme isso em arrays NUMPY
pesos = np.array(pesos)
altura = np.array(altura)

# Imprime o cálculo de cada valor
pesos / altura ** 2

# Arrays Numpy armazena elementos como strings quando estes não são inteiros ou float
a = np.array([1,3,'Casa',True])

a

# Ocorre um erro se for realizado um cálculo com array desse tipo
a * 2

"""<h2>Métodos e atributos Úteis</h2>"""

# Métodos disponíveis (digite o ponto(.) pressione o tab)
two_dim

# Retorna a forma do array no formato linhas e colunas
two_dim.shape

# Retorna a quantidade de dimensões
two_dim.ndim

# Imprimindo o valor máximo do array
two_dim.max()

# Imprimindo o valor mínimo do array
two_dim.min()

# Imprimindo o valor médio
two_dim.mean()

# Imprimindo o desvio padrão
two_dim.std()

two_dim

# Mostrar o tipo de dados pertecentes ao array
two_dim.dtype

# Mostra a quantidade de elementos do array 
two_dim.size

# Mostra a quantidade em bytes dos elementos no array
two_dim.itemsize

# Somando todos os elementos do array
two_dim.sum()

"""<h2>Transformando Arrays</h2>"""

two_dim

# Gera a Transposta da Matriz (Linha -> Coluna)
two_dim.T

# Verificando que usando o atributo Transposta, o array original não é modificado
two_dim

# Transformar em uma matriz de uma linha
# É muito comum em bibliotecas como scikit-learn e Keras
two_dim.reshape(-1)

tree = np.random.random((5,3))

tree

tree.shape

# Transforma em uma matriz com 3 linhas e 5 colunas
tree.reshape(3,5)

tree.shape

tree.reshape(-1).shape

t = tree.reshape(1,15)
t.shape

tree

# Adicionando elemetntos a um array
two_dim = np.insert(two_dim,0,10)

# Transforma em um array de uma linha
two_dim

# Apagando o elemento da primeira posição do array
two_dim = np.delete(two_dim,[0])

two_dim

# Gerando um arquivo .txt a partir de um array
np.savetxt('dataset_array.txt', two_dim, delimiter=',')

