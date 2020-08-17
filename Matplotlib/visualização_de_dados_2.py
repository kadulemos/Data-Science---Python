# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# <h2>Adiciona textos em gráficos</h2>

# %%
# Importando a biblioteca NUMPY
import numpy as np


# %%
# Importando o PYPLOT
from matplotlib import pyplot as plt


# %%
get_ipython().run_line_magic('matplotlib', 'inline')
#100 valores no intervalo de 0 a 2
x = np.linspace(0,2,num=100)

# Define a legenda e tamanho das linhas (linewidth - espessura da linha)
plt.plot(x, x, label='linear')
plt.plot(x, x ** 2, label='quadrático', linewidth=5)

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Gráfico de Linhas Simples')

# Exibe a legenda e por padrão usa o label de cada plot
plt.legend()

# Configurações do texto
plt.text(1.00, 1.0, 'Cruzamento das Linhas', fontsize=10, horizontalalignment = 'right')

plt.show()

# %% [markdown]
# <h2>Plotando Histogramas</h2>
# 
# * Histogramas são úteis quando queremos visualizar a distribuição de **uma** variável;
# * Esse é um gráfico muito utilizado em estatística descritiva;
# * Facilita a visualização de dados extremos;
# * É útil em tarefas de **análise** e **exploração** de dados.
# %% [markdown]
# **Gera dados aleatórios com média em torno de 0 e desvio padrão em torno de 1**

# %%
d = np.random.normal(0,1,size=500)

# %% [markdown]
# **Plota histograma com 10 bins**

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
plt.hist(d, bins=10, color='r')

# %% [markdown]
# <h2>Trabalhando com datafrmaes Pandas</h2>
# 
# * O Matplotlib trabalha com o Pandas;
# * É possível usar recursos de dataframes usando o parâmetro **data**.

# %%
import pandas as pd

# %% [markdown]
# **Cria um dicionário de valores**

# %%
data = {'a': np.arange(50), 'c': np.random.randint(0,50,50), 'd': np.random.randn(50)}


# %%
data = pd.DataFrame(data)


# %%
data.head()

# %% [markdown]
# **Gera dados aleatórios para as colunas *b* e *d* **

# %%
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 200


# %%
data.b.head()

# %% [markdown]
# **Dados Absolutos**

# %%
data.d.head()


# %%
# Visualizando todos os campos
data.head()

# %% [markdown]
# **Plota gráfico de dispersão usando pandas dataframe**

# %%
# scatter(axis_x, axis_y, color, size, data)
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# %%


