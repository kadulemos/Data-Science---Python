# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <h2>Visualização de dados com Plotly</h2>
# %% [markdown]
# **Cufflinks conecta o pandas ao plot.ly**
# 
# * Instalação do Plot.ly e Cufflinks
# 
# !pip install cufflinks <br>
# !pip install plotly

# %%
import cufflinks as cf
from plotly.offline import plot, iplot
import pandas as pd
import numpy as np

# %% [markdown]
# Cria um dataframe com dados aleatórios divididos em 4 colunas

# %%
df = pd.DataFrame(np.random.randn(100,4), columns=['A', 'B', 'C', 'D'])


# %%
df.head()

# %% [markdown]
# **É preciso habilitar o modo offline primeiramente**

# %%
cf.go_offline()

# %% [markdown]
# Ao tentar usar o Cufflinks veja o resultado

# %%
df.iplot()

# %% [markdown]
# <h3>Gráficos do tipo scatter</h3>

# %%
df.iplot(kind='scatter', x='A', y='B', mode='markers')

# %% [markdown]
# <h3>Gráficos de Barras</h3>

# %%
df.sum().iplot(kind='bar')

# %% [markdown]
# <h3>Gráfico de Boxplot</h3>
# 
# * Basta clicar no item da legenda a direita para habilitar ou desabilitar o dado da coluna

# %%
df.iplot(kind='box')

# %% [markdown]
# <h3>Histograma</h3>
# * Compare com os histogramas padrões do matplotlib e seaborn

# %%
df['A'].iplot(kind='hist')

# %% [markdown]
# * Histograma aninhado de todas as colunas (mesmo tipo de dados)

# %%
df.iplot(kind='hist')

# %% [markdown]
# <h3>Spread plots</h3>

# %%
df[['A', 'D', 'C', 'B']].iplot(kind='spread')

# %% [markdown]
# <h3>Bubble Plots</h3>

# %%
df.iplot(kind='bubble', x = 'A', y = 'B', size = 'C')

# %% [markdown]
# <h3>Scatter Matrix</h3>
# * Similar ao pairplot do Seaborn <br>
# * Se o dataframe for muito grande pode travar o seu notebook

# %%
df.scatter_matrix()


