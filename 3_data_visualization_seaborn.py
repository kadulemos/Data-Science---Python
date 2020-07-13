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


# %%


