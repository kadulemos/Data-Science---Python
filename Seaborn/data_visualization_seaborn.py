# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# <h2>Minerando Dados - Visualização de Dados</h2>
# 
# **Trabalhando com Seaborn**
# 
# * Biblioteca para visualização de dados baseado em MATPLOTLIB;
# * Interface de alto nível para gráficos estatísticos;
# * Fornece uma interface atraente e profissional para os gráficos;
# * Simples e muito intuitiva de usar.
# %% [markdown]
# **Quando utilizar**
# 
# * Útil para análise e exploração de dados;
# * Apresentar análises visuais.
# %% [markdown]
# **Instalação da Biblioteca**
# 
# * Caso não esteja usando anaconda intalar matplotlib com o gerenciador de pacotes pip ou usando o conda.
# %% [markdown]
# <h1>SEABORN</h1>

# %%
# !pip install seaborn == 0.9.0
# !conda install seaborn == 0.9.0

# %% [markdown]
# <h2>Datasets</h2>

# %%
import seaborn as sns


# %%
# Dataset já disponível junto com a bilioteca seaborn, utilizada como exemplo
df_tips = sns.load_dataset('tips')


# %%
df_tips.head()

# %% [markdown]
# <h2>Visualizando Relações Estatísticas nos Dados</h2>
# 
# *A análise estatística é o processo de entender como variáveis no conjunto de dados se relacionam uma com a outra e como essas relações dependem de outras variáveis. A visualização de dados se torna uma peça essencial nesse processo, pois, quando os dados são visualizados adequandamente, as pessoas conseguem descobrir padrões que indicam relações nos dados.*
# %% [markdown]
# <h3>Função relplot()</h3>
# Método de alto nível para visualização de relações estatísticas entre variáveis. O método relplot() já combina o **scatter plot** e **line plots**.
# Muito útil para ver relações entre duas ou mais variáveis com o uso de parâmetros de semântica dos dados.
# %% [markdown]
# <h2>Relação de Variáveis com Scatter Plots</h2>
# %% [markdown]
# **Visualizando a relação entre a variável valor da conta e gorjeta.**

# %%
tips = sns.load_dataset('tips')
sns.relplot(x='total_bill', y='tip', data=tips)

# %% [markdown]
# **Visualizando a relação entre as variáveis total da conto e gorjeta e colrindo cada ponto com a variável smoker(fumante)**

# %%
sns.relplot(x='total_bill', y='tip', hue='smoker', data=tips)

# %% [markdown]
# **Visualizando a relação entre as variáveis total da conta e gorjeta, colorindo cada ponto com a variável sexo (Male, Female)**

# %%
sns.relplot(x='total_bill', y='tip', hue='sex', data=tips)

# %% [markdown]
# **Visualizando a relação entre as variáveis total da conta e gorjeta, colorindo cada ponto com a varável sexo e definindo um estilo também baseado na variável sexo**

# %%
sns.relplot(x='total_bill', y='tip', hue='sex', style='sex', data=tips)

# %% [markdown]
# **É possível representar quatro variáveis alterando a tonalidade e estilo de cada ponto. Mas é preciso cautela, pois, a visualização pode ficar confusa.**

# %%
sns.relplot(x='total_bill', y='tip',hue='sex', style='smoker', data=tips)

# %% [markdown]
# **Em casos de variáveis *numéricas* para definir a tonalidade a paleta de cores altera de forma sequencial.**

# %%
sns.relplot(x='total_bill', y='tip', hue='size', data=tips);

# %% [markdown]
# **É possível customizar a paleta de cores sequenciais no link:**
# * https://seaborn.pydata.org/generated/seaborn.cubehelix_palette.html#seaborn.cubehelix_palette

# %%
sns.set_palette(sns.color_palette('Blues_d'))
sns.relplot(x='total_bill', y='tip', hue='size', data=tips)

# %% [markdown]
# **Usando a opção 'size' para definir o tamanho de cada ponto baseado em alguma coluna da base de dados.**

# %%
sns.relplot(x='total_bill', y='tip', size='size', data=tips)


# %%
# Definindo uma faixa para os valores de size (alterando a representação gráfica, sem mexer nos dados)
sns.relplot(x='total_bill', y='tip', size='size', sizes=(15,300), data=tips)

# %% [markdown]
# <h2>Scatterplot</h2>
# 
# * Caso não queira usar o *relplot()* o método *scatterplot()* já atende perfeitamente quando queremos ver relações nos dados.
# * A única diferença é que o scatterplot plota gráfico de dispersão apenas, logo este não contém a função *lineplot()*
# %% [markdown]
# **Visualizando relação entre as 4 variáveis *total_bill, tipo, day, smoker* **

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
sns.scatterplot(x='total_bill', y='tip', hue='day', style='time', data=tips)

# %% [markdown]
# <h2>Redimensionando Figuras no SEABORN</h2>

# %%
import matplotlib.pyplot as plt


# %%
# 'f' represents figure and 'ax' represents the axis
f, ax = plt.subplots(figsize=(12,5))

sns.scatterplot(x='total_bill', y='tip', hue='day', data=tips)

