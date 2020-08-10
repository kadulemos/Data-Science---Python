# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# <h2>Minerando Dados - Visualização de Dados</h2>
# 
# **Trabalhando com Seaborn**
# 
# * Biblioteca para Visualização de dados em Matplotlib;
# * Interface de alto nível para gráficos *estatísticos*;
# * Fornece uma Interface atraente e profissional para os gráficos;
# * Simples e muito intuitiva de usar.
# %% [markdown]
# **Quando utilizar?**
# 
# * Útil par análise e exploração de dados;
# * Apresenta análises visuais.
# %% [markdown]
# <h3>Carregando Dataset</h3>

# %%
import seaborn as sns


# %%
tips = sns.load_dataset('tips')

# %% [markdown]
# <h3>Plotando dados categóricos</h3>
# 
# * Quando trabalhamos com variáveis categóricas temos que visualizar dados de formas diferentes;
# * O *Seaborn* fornece o método *catplot()* que já contém diversos tipos de gráficos embutidos;
# * Isso facilita, pois, você pode usar diferentes gráficos usando um mesmo método.
# %% [markdown]
# **Gráficos de barras ou também conhecidos como gráficos de colunas**

# %%
sns.catplot(x='sex', kind='count', palette='Set2', data=tips)

# %% [markdown]
# **Gráficos de barras horizontais usando a coluna *day* **

# %%
sns.catplot(y='day', kind='count', palette='Set1', data=tips)

# %% [markdown]
# **Scatter plot com dados categóricos**

# %%
sns.catplot(x='day', y='total_bill', palette='Set2', data=tips)

# %% [markdown]
# **O parâmetro *swarm* evita sobreposições de pontos**

# %%
sns.catplot(x='day', y='total_bill', kind='swarm', data=tips)

# %% [markdown]
# **O parâmetro *hue* permite adicionarmos uma terceira variável a nossa visualização**

# %%
sns.catplot(x='day', y='total_bill', kind='swarm', hue='sex', palette='Dark2', data=tips)

# %% [markdown]
# * O parâmetro **order** permite alterarmos a ordem padrão das categorias que estão sendo exibidas;
# * Isso é útil quando temos mais de um gráfico na mesma figura e queremos manter as mesmas ordens.

# %%
sns.catplot(x='day', y='total_bill', kind='swarm', hue='sex', order=['Sat', 'Sun', 'Fri', 'Thur'], data=tips)

# %% [markdown]
# **Invertendo a visualização para plots horizontais**

# %%
sns.catplot(x='total_bill', y='day', kind='swarm', data=tips)

# %% [markdown]
# <h3>Gráficos com Regressão</h3>
# 
# * Quando temos muitas variáveis quantitativas em nossos dados é interessante visualizar como estas se relacionam;
# * Podemos visualizar essas informações com linhas de Regressão;
# * Com modelos de regressão simples é possível checar se existe alguma correlação entre algumas variáveis.
# %% [markdown]
# **Exibe a linha de regressão para visualizar a correlação entre as variáveis**

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
sns.lmplot(x='total_bill', y='tip', hue='sex', palette='Pastel1', data=tips)

# %% [markdown]
# **Usando o parâmetro col para segregar os gráficos pelo valor da coluna categórica *time* **

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
sns.lmplot(x='total_bill', y='tip', hue='smoker', col='time', palette='Set2', data=tips)

# %% [markdown]
# **Parâmetros scatter_kws e line_kws**

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
sns.lmplot(x='total_bill', 
y='tip', hue='smoker', 
col='time', 
palette='Set1', 
data=tips, 
scatter_kws={'s': 90, 'alpha': 0.5}, 
line_kws={'lw': 4})

# %% [markdown]
# **Segregando gráficos pelo parâmetro *col* e pelo parâmetro *row* **

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
sns.lmplot(x='total_bill', y='tip', hue='smoker', col='time', row='sex', palette='Set2', data=tips)

# %% [markdown]
# <h2>Visualizando distribuições de observações</h2>
# 
# * Um dataset muito grande será difícil de visualizar variáveis categóricas;
# * É preciso sumarizar a distribuição dos dados para facilitar a visualização;
# * Podemos usar um gráfico do tipo Boxplot para visualizar a distribuição de tais variáveis;
# * Esse tipo de gráfico é muito útil para visualizar ** *Outliers* **.
# %% [markdown]
# **Boxplot de Dias da semana por total de conta**

# %%
sns.catplot(x='day', y='total_bill', kind='box', data=tips)

# %% [markdown]
# **Gráfico de Boxplot dos dias por total de conta e se a pessoa é fumante ou não**

# %%
sns.catplot(x='day', y='total_bill', hue='smoker', kind='box', data=tips)

# %% [markdown]
# **Boxen**
# 
# * Tipo de boxplot com foco maior dos dados do que nos *outliers*;
# * Esse tipo de gráfico é interessante quando temos grandes datasets.

# %%
sns.catplot(x='day', y='total_bill', kind='boxen', data=tips)

# %% [markdown]
# **Stripplot**
# 
# * Esse método permite plotar a distribuição dos dados;
# * Podemos combinar os dois gráficos para ter mais informação.

# %%
sns.catplot(x='day', y='total_bill', kind='boxen', data=tips)
sns.stripplot(x='day', y='total_bill', data=tips, color='blue')

# %% [markdown]
# ** O método *catplot()* permite usarmos facetgrid assim podemos combinar gráficos em uma única figura**

# %%
get_ipython().run_line_magic('matplotlib', 'inline')
sns.catplot(x='sex', y='total_bill', hue='smoker', col='time', data=tips, kind='boxen', height=4)

# %% [markdown]
# <h2>Violin Plot</h2>
# 
# * Gráfico ideal para visualizar a distribuição de variáveis;
# * Combinação do Boxplot com o KDE;
# * Funciona bem para distribuições com picos;
# * Permite uma visualização mais rica do que com o Boxplot normal. 
# %% [markdown]
# **Violin Plot**

# %%
sns.catplot(x='day', y='total_bill', kind='violin', data=tips)

# %% [markdown]
# **Violin Horizontal**

# %%
sns.catplot(x='total_bill', y='day', kind='violin', data=tips)

# %% [markdown]
# **Usando o parâmetro Hue para ter uma terceira variável**

# %%
sns.catplot(x='day', y='total_bill', hue='time', kind='violin', data=tips)

# %% [markdown]
# **Split**
# 
# * É possível dividir o violin plot com o parâmetro split;
# * Sendo útil quando temos muitos dados para exibir.

# %%
sns.catplot(x='day', y='total_bill', hue='sex', split=True, kind='violin', data=tips)

# %% [markdown]
# **Inner**
# 
# * Usando o parâmetro *inner* para preencher o violin plot com observações;
# * Útil para destacar bem as partes que possuem mais dados.

# %%
sns.catplot(x='day', y='total_bill', hue='sex', split=True, inner='stick', palette='pastel', kind='violin', data=tips)

# %% [markdown]
# **Swarm**
# 
# * Podemos combinar também um gráfico de swarm com o Violin Plot;
# * Dessa forma fica mais explícito ainda a frequência de pontos nas partes do 'violino'.

# %%
sns.catplot(x='day', y='total_bill', hue='sex', split=True, palette='pastel', kind='violin', data=tips)
sns.swarmplot(x='day', y='total_bill', color='k', size=3, data=tips)

# %% [markdown]
# <h2>Visualizando a distribuição de um Dataset</h2>
# %% [markdown]
# **Histograma**
# 
# * O método histograma tenta encontrar a melhor quantidade de bins.

# %%
sns.set(color_codes=True)


# %%
sns.distplot(tips.total_bill, kde=False)

# %% [markdown]
# **Plotando um histograma para uma distribuição normal**
# 
# * Importa o Numpy para geração aleatória de dados

# %%
import numpy as np

# %% [markdown]
# * Gera 100 valores aleatórios em uma distribuição normal

# %%
x = np.random.normal(size=100)

# %% [markdown]
# * Mostra Dados aleatórios na variável **x**

# %%
x

# %% [markdown]
# * Plota o histograma para a variável **x**

# %%
sns.distplot(x)

# %% [markdown]
# * Plota o Histograma com bins=20 e KDE = True

# %%
sns.distplot(tips.total_bill, bins=20, kde=True)

# %% [markdown]
# Visualizando apenas o KDE

# %%
sns.distplot(tips.total_bill, hist=False)

# %% [markdown]
# Parâmetro RUG

# %%
sns.distplot(tips.total_bill, hist=False, rug=True)

# %% [markdown]
# <h2> Jointplot (ScatterPlot e Histograma) </h2>
# 
# * Quando queremos ver a distribuição de duas variáveis podemos usar o Jointplot;
# * União de gráficos do tipo Plot e Histogramas para as duas variáveis;
# * Mostra o ScatterPlot para as duas variáveis e um Histograma para cada variável separadamente.

# %%
sns.jointplot(x='tip', y='total_bill', color='r', data=tips)

# %% [markdown]
# <h2> Hexbin Plots </h2>
# 
# * Adequado para visualização de grande conjunto de dados;
# * Tende a funcionar melhor com as cores em branco de fundo.

# %%
sns.jointplot(x='tip', y='total_bill', color='b', kind='hex', data=tips)

# %% [markdown]
# **Usando o KDE para mais de uma variável**

# %%
sns.jointplot(x='tip', y='total_bill', color='b', kind='kde', data=tips)

# %% [markdown]
# <h2>Visualizando relacionamentos emparelhados</h2>
# 
# * Plot multiplas variáveis de um dataset;
# * Cria uma matriz de eixos de mostrar a relação de cada par de colunas no dataframe;
# * Por padrão plota também um histograma de cada coluna no dataframe na diagonal da matriz;

# %%
sns.pairplot(tips)

# %% [markdown]
# **Carrega o dataset iris**

# %%
iris = sns.load_dataset('iris')


# %%
iris.head()

# %% [markdown]
# **Plot pares emparelhando segregando pela coluna species**

# %%
sns.pairplot(iris, hue='species', palette='Set1')

# %% [markdown]
# **Plotando Scatter plots com regressão**

# %%
sns.pairplot(iris, kind='reg')

# %% [markdown]
# **Plotando histograma na diagonal**

# %%
sns.pairplot(iris, hue='species', diag_kind='hist')

# %% [markdown]
# **Plotando apenas duas colunas do dataframe**

# %%
sns.pairplot(iris, hue='species', vars=['sepal_width', 'sepal_length'], palette='Set1')

# %% [markdown]
# <h2>Gráficos de Correlação</h2>
# 
# * Útil para visualizar se existem correlações positivas entre colunas;
# * Método corr() do pandas possibilita calcular correlações por tipo *spearman* ou *pearson*;

# %%
correlacoes = tips.corr()


# %%
ax = sns.heatmap(correlacoes)

# %% [markdown]
# **Exibe os valores de correlação**

# %%
ax = sns.heatmap(correlacoes, annot=True)

# %% [markdown]
# **Visualizando a correlação de colunas do Dataframe Iris**

# %%
correlacoes = iris.corr()


# %%
ax = sns.heatmap(correlacoes, cmap= 'PuOr', annot= True)


# %%



