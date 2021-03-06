# -*- coding: utf-8 -*-
"""Notebook_Aula_Python01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nY4frRDtSO14l54gb_n7Rcj6ERX5G0dv

<h1>Minerando Dados - Linguagem Python
"""

#Esse é um comentário

print('Hello World')

'Hello World'

# Operações matemáticas. Pressione Shift + Enter para executar a célula

# Adição

2 + 10

#Subtração

2 - 2

# Multiplicação

2 * 2

#Divisão

2 / 2

# Numeros Float

3.2 + 6.6

8.8 / 2

10.2 + 2.5

"""<h2>Funções no Python"""

type(5)

type(6.6)

type('Minerando Dados')

"""<h2>Funções de Conversão"""

int(6)

int(6.5)

float(6.5)

str(5)

# Arredondamento de Valore

round(2.8989898989)

round(2.4545455,3)

"""<h2>Trabalhando com Variáveis"""

var1 = 1
var2 = 2
var3 = 3

var1

type(var1)

var1 + var2

# Reatribuindo um valor var1 graça a TIPAGEM DINÂMICA

var1 = 'Rock Forever'

type(var1)

var2 = 6.78

type(var2)

"""<h2>Operações Matemáticas e Variáveis"""

resultado = var2 * 10

resultado

resultado = 200/3

resultado

## Declarando vários valores a variáveis

variavel1, variavel2 = 1, 'Teste'

variavel1

variavel2

"""<h2>Restrições para criação de variáveis"""

variavel_teste = 2

variavel_teste

var1 = 10

var1

# Palavras Reservadas não são permitidas: break, if, else, print, for, etc...

"""<h2>Trabalhando com Strings"""

# Criando uma variável do tipo String

frase = 'Python é uma linguagem Sensacional'

frase

# Indexando Strings

#Importante!! O índice começa com o número 0.
frase[0]

frase [1]

# Não é permitido realizar a substituição de strings
# Ex. => frase[0] = 'R'

# Slicing: Percorrendo Strings

frase [0:6]

frase[6:]

frase[:6]

# Concatenando Strings

frase1 = 'Python é uma Linguagem Fenomenal'

frase2 = 'para qualquer cientista de dados'

frase1 + frase2

# Objeto String - Métodos

frase = 'Minerando Dados a maior comunidade de Data Science do Brasil.'

frase.count('Dados')

# A função lower()

frase.lower()

frase.upper()

frase.capitalize()

frase.islower()

# Quebrando a string em uma lista de termos
frase.split()

"""<h2> Trabalhando com Listas </h2>"""

# Sitanxe para criar listas no Python
bixos = [1,2,3]
bixos

# Listas com tipos de dados diferentes
bixos = ['dog', 'cat', 122344545, 13.9, [0,0,1]]

bixos

# Índices de elementos

bixos[0]

bixos [3]

# Atualizando o valor 1 da Lista

bixos[0] = 'Horse'

bixos

# Slicing em Listas

bixos[1:]

# Removendo elementos
bixos.remove('cat')

bixos

"""<h2> Operações em Listas </h2>"""

len (bixos)

# Concatenando Listas

bixos + [200,'Minerando', 'Dados']

# Check elementos

'cat' in bixos

# Valor máximo da Lista

lista = [1,500,23,90,56788]

max(lista)

# Valor mínimo da Lista

min(lista)

# Multiplicação de Elementos

['Olá'] * 3

"""<h2> Métodos em Listas </h2>"""

# É possível visualizar os métodos existentes do objeto lista (digite o nome do objeto + . + tab)
bixos.append('snake')

bixos

# Extend a lista com mais de um elemento.
bixos.extend(['lion',10.5])

bixos

bixos.index('snake')

bixos.remove('snake')

bixos.count('snake')

bixos

# Ordenação de lista de inteiros
lista =[1,500,23,90,56788]
lista2 = ['casa', 'rio', 'lua', 'agua']

lista.sort()

lista

lista2.sort()

lista2

"""<h2> Lista Aninhadas </h2>"""

# Lista que contém 3 listas
listas = [['cat', 'dog', 'snake'], ['Audi', 'Ferrari', 'Porshe'], [10, 100, 200]]

# Imprimindo o primeiro elemento (lista de animais)
listas [0]

# Imprimindo o segundo elemento (lista de carros)
listas [1]

# Imprimindo o terceiro elemento (lista de inteiros)
listas [2]

# Imprimindo o primeiro carro da lista de carros
listas [1] [0]

# Imprimindo o segundo carro da lista de carros
listas [1] [1]

# Imprimindo o último valor da lista de números
listas [2] [2]

# Operação de repetição de elementos de linhas aninhadas
listas [0] * 3

