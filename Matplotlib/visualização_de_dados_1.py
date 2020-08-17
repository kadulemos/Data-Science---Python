# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# <h2>Minerando Dados - Visualização de Dados</h2>
# %% [markdown]
# **Trabalhando com Matplotlib**
# 
# * Ideal para plotagem de gráficos **simples**;
# * Aumenta a produtividade do Cientista de Dados;
# * Fornece uma interface próxima do Matlab, o que é interessante para gráficos com expressõe matemáticas;
# * A maior vantagem é o **layout**.
# %% [markdown]
# **Quando utilizar**
# 
# * Útil para análise e exploração dos dados.
# %% [markdown]
# **Instalação da Biblioteca**
# 
# * Caso não esteja usando anaconda instale o matplotlib com o gerenciador de pacotes pip ou usando o conda. Exemplo: <br>
# !pip install matplotilib<br>
# !conda install matplotlib
# %% [markdown]
# **Se estiver usando o Anaconda, o matplotlib já está disponível por padrão**

# %%
# Importando o pyplot
from matplotlib import pyplot as plt

# %% [markdown]
# **Define que os gráficos serão plotados na célula e podem ser ajustados**

# %%
get_ipython().run_line_magic('matplotlib', 'notebook')

# %% [markdown]
# **Define que os gráficos ficarão fixos na célula do jupyter notebook**

# %%
get_ipython().run_line_magic('matplotlib', 'inline')

# %% [markdown]
# **Plotando gráficos de linhas simples**

# %%
from IPython.display import Image
Image('anatomia.png')

# %% [markdown]
# <h2>Gráfico de Linhas</h2>
# 
# * Gráfico normalmente utilizado para visualizaçõa de dados em uma linha do tempo;
# * Normalmente utilizado com eixo X relacionado a dados temporais e eixo Y a dados quantitativos;
# * Cuidado ao plotar várias linhas, a leitura pode ficar prejudicada.

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
# Eixo_x, Eixo_y
plt.plot([1,2,3,4], [1,4,9,16])
plt.show()

# %% [markdown]
# Definindo label aos eixos

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot([1,2,3,4], [1,4,9,16])
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')
plt.show()

# %% [markdown]
# Alterando a forma dos pontos

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot([1,2,3,4], [1,4,9,16], 'o')
plt.show()

# %% [markdown]
# Definindo limites de visualização dos eixos x e y

# %%
# Opção do método axis()
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot([1,2,3,4], [1,4,9,16], 'o')
plt.axis([0,6,0,20]) #[xmin, xmax, ymin, ymax]
plt.show()

# %% [markdown]
# **Importando a biblioteca Numpy**

# %%
import numpy as np

# %% [markdown]
# Plot duas séries de dados, no caso x1, x2 e y2, x3 e y3

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
x1 = np.array([1,2,3,4,5,6,7,8,9,11])

x2 = x1
y2 = x1**2      #Número elevado ao quadrado

x3 = x1
y3 = x1**3      #Número elevado ao cubo

plt.plot(x1, x1, 'r--', x2, y2, 'bs', x3, y3, 'g^')

plt.show()

# %% [markdown]
# <h2>Plotando dados categóricos</h2>
# 
# * Trabalhando com gráficos de barras;
# * Ideal para quando estamos trabalhando com **comparação de valores**;
# * Normalmente utilizado para visualizar frequências ou percentrual de valores.
# %% [markdown]
# **Plotando gráfico de barras verticais ou gráfico de colunas**

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
grupos = ['Produto A', 'Produto B', 'Produto C']
valores = [1,10,100]

plt.bar(grupos, valores)        #Eixo_X, Eixo_Y
plt.show()

# %% [markdown]
# **Plota gráficos de Barra juntos**

# %%
get_ipython().run_line_magic('matplotlib', 'inline')

#Quantidade de vendas para o Produto A
valores_produto_A = [6,7,8,4,4]

#Quantidade de vendas para o Produto B
valores_produto_B = [3,12,3,4.1,6]

#Cria eixo x para produto A e produto B com uma separação de 0.25 entre as barras
x1 = np.arange(len(valores_produto_A))
x2 = [x + 0.25 for x in x1]

# Plota as barras
plt.bar(x1, valores_produto_A, width=0.25, label = 'Produto A', color = 'b')
plt.bar(x2, valores_produto_B, width=0.25, label = 'Produto B', color = 'y')

meses = ['Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
plt.xticks([x + 0.25 for x in range(len(valores_produto_A))], meses)

plt.legend()

plt.title('Quantidade de Vendas')
plt.show()

# %% [markdown]
# **Gráfico de Barras Horizontais**
# 
# * Gráfico muito usado quando queremos fazer **comparações**;
# * Muito usado em pesquisas de campanhas eleitorais;
# * Leitura muito simples e intuitiva.

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
grupos = ['Produto A', 'Produto B', 'Produto C']
valores = [1, 10, 100]

plt. barh(grupos, valores)

plt.show()

# %% [markdown]
# **Rotacionando Labels**

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
grupos = ['Produto A', 'Produto B', 'Produto C']
valores = [1, 10, 100]

plt.barh(grupos, valores)
plt.barh(grupos, valores)
plt.yticks(rotation = 45)

plt.show()

# %% [markdown]
# <h2>Gráfico de Pizza</h2>

# %%
get_ipython().run_line_magic('matplotlib', 'inline')

vendas = [3000, 2300, 1000, 500]
labels = ['E-commerce', 'Loja Física', 'E-mail', 'Marketplace']

plt.pie(vendas, labels = labels)
plt.show()

# %% [markdown]
# **Customizando gráficos**
# 
# * Adicionando informações de percentual, sombra, separação das partes e legenda

# %%
get_ipython().run_line_magic('matplotlib', 'inline')

vendas = [3000, 2300, 1000, 500]
labels = ['E-commerce', 'Loja Física', 'E-mail', 'Marketplace']

# Define o nívél de separabilidade entre as partes, ordem do vetor representa as partes
explode = (0.1, 0, 0, 0)

plt.pie(vendas, labels = labels, autopct='%1.1f%%', shadow=True, explode=explode)
plt.legend(labels, loc=2)

# Define que o gráfico será plotado em círculo
plt.axis('equal')

plt.show()

# %% [markdown]
# <h2>MATPLOTLIB, PYPLOT E PYLAB</H2>
# 
# * Pyplot é um módulo do pacote matplotlib que implicitamente cria figuras e eixos nos gráficos;
# * Pylab é outro módulo do matplotlib que já importa o numpy e pyplot. Este módulo é projetado para plots de arrays e cálculos matemáticos;
# * Pylab está depreciado.

# %%
import matplotlib.pyplot as plt
import numpy as np

# Cria uma figura
fig = plt.figure()

# Define eixos
ax = fig.add_subplot(111)

# Scatter plot usando numpy
ax.scatter(np.linspace(0,1,5), np.linspace(0,5,5))

# Show the plot
plt.show()

# %% [markdown]
# <h2>Criando Subplots</h2>
# 
# * Para criar *subplots* defina o número de linhas de gráficos e número de colunas (quantidade de gráfico em cada linha)

# %%
plt.subplots(nrows=1, ncols=2)

# %% [markdown]
# **1 linha com 3 colunas**

# %%
plt.subplots(nrows=1, ncols=3)

# %% [markdown]
# **2 linhas com 2 colunas**

# %%
plt.subplots(nrows=2, ncols=2)

# %% [markdown]
# **Para acessar subplots usa-se o método *subplot* (atenção para o nome correto no singular)**

# %%
x = [1,2,3,4]
y = [10,20,25,40]

plt.subplot(1,2,1)
plt.plot(x,y,'o')

plt.subplot(1,2,2)
plt.plot(x,y, color='r')

# %% [markdown]
# **Criação de instâncias de classes figure**
# 
# * Aumenta o controle do nível de customização das funções do Matplotlib;
# * Gera menos código devido a orientação a objetos.

# %%
# Cria um objeto do tipo figure
fig = plt.figure()

# Define o tamanho em percentual do gráfico
# Altura e largura do eixo na figura
axes_a = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Plota o gráfico
axes_a.plot(x,y)

# %% [markdown]
# **Uma figura com dois gráficos de proporções diferentes**

# %%
# Cria um objeto do tipo figure
fig = plt.figure()

# Define o tamanho em percentual do gráfico
# Altura e largura do eixo na figura
axes_a = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes_b = fig.add_axes([0.2, 0.5, 0.3, 0.3])

# Plota a figura com dois eixos
# O "r--" siginifica linha tracejada em vermelho (r)
axes_a.plot(x,y)
axes_b.plot(x,y,'r--')

# %% [markdown]
# **É possível customizar a largura ou altura do gráfico para acomodar melhor seus dados**
# 
# * Exemplo: gráficos de dados financeiros em uma granularidade muito baixa (minutos)

# %%
x = [1,2,3,4]
y = [10,20,25,40]

# Altera a largura e altura do gráfico (width, height)
fig, ax = plt.subplots(figsize=(20,5))

# Plota o gráfico
ax.plot(x,y, 'r--')

# %% [markdown]
# **Plotando dois gráficos (eixos) na mesma figura**

# %%
# Define as configurações dos plots
# Cada plot terá o mesmo tamanho de figuras
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,5))

# Dados para cada subplot
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])

plt.show()

# %% [markdown]
# **Define configurações dos eixos com o métoa "set()"**

# %%
import matplotlib.pyplot as plt

# Define as configurações dos plots
# Cada plot terá o mesmo tamanho de figuras
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,5))

# Dados para cada subplot
ax1.bar([1,2,3],[3,4,5], color ='r')
ax2.barh([0.5,1,2.5],[0,1,2])

# Usa o método set para definir configurações do gráfico
ax1.set(title='Gráfico de Barras Verticais', xlabel='Eixo X', ylabel='Eixo Y')
ax2.set(title='Gráfico de Barras Horizontais', xlabel='Eixo X', ylabel='Eixo Y')

plt.show()

# %% [markdown]
# <h2>Customizando Layouts</h2>

# %%
# Define o estilo para ggplot
plt.style.use('ggplot')


# %%
# Criando o mesmo gráfico anterior, mas com o estilo GGPLOT
# Define as configurações dos plots
# Cada plot terá o mesmo tamanho de figuras
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,5))

# Dados para cada subplot
ax1.bar([1,2,3],[3,4,5], color ='r')
ax2.barh([0.5,1,2.5],[0,1,2])

# Usa o método set para definir configurações do gráfico
ax1.set(title='Gráfico de Barras Verticais', xlabel='Eixo X', ylabel='Eixo Y')
ax2.set(title='Gráfico de Barras Horizontais', xlabel='Eixo X', ylabel='Eixo Y')

plt.show()

# %% [markdown]
# **Matplotlib funciona também com cores em RGB. Para fazer isso use o parâmetro color**

# %%
# Define as configurações dos plots
# Cada plot terá o mesmo tamanho de figuras (10,5)
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(10,5))

# Dados para cada subplot
ax1.bar([1,2,3],[3,4,5], color ='#00BFFF')
ax2.barh([0.5,1,2.5],[0,1,2], color='#00FF00')

# Usa o método set para definir configurações do gráfico
ax1.set(title='Gráfico de Barras Verticais', xlabel='Eixo X', ylabel='Eixo Y')
ax2.set(title='Gráfico de Barras Horizontais', xlabel='Eixo X', ylabel='Eixo Y')

plt.show()

# %% [markdown]
# 
