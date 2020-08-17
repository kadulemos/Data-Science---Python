# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <h2>Visualização de Dados Reais</h2>

# %%
import pandas as pd
import numpy as np


# %%
# importando Cufflinks
import cufflinks as cf
from plotly.offline import plot, iplot


# %%
# Importando dados para serem trabalhados
df2 = pd.read_csv('olist_classified_public_dataset.csv')

# %% [markdown]
# <h3>Perguntas aos dados</h3>
# 
# * Quais a distribuições dos status dos pedidos? <br>
# * Quais os meses do ano houve mais vendas? <br>
# * Qual a distribuição de itens de um pedido? (média) <br>
# * Qual a quantidade de vendedores em um pedido? (média) <br>
# * O valor do frete tende aumentar com o preço do produto? <br>
# * Qual o tempo médio de entrega? <br>
# * Como foi as vendas por mês? <br>
# * Quais meses superaram a meta de vendas? <br>
# * Como foi a venda por mês se comparado ao ano de 2016? <br>

# %%
df2.head()

# %% [markdown]
# **Status dos pedidos**

# %%
# Ativando o modo offline
cf.go_offline()


# %%
df2.order_status.value_counts()


# %%
df2.order_status.value_counts().iplot(kind='bar')


# %%
df2.info()

# %% [markdown]
# **Transformando colunas para o formato datetime**

# %%
df2.order_purchase_timestamp = pd.to_datetime(df2.order_purchase_timestamp)


# %%
df2.order_aproved_at = pd.to_datetime(df2.order_aproved_at)

# %% [markdown]
# Visualizando as colunas agora em Datetime

# %%
df2.info()

# %% [markdown]
# * Use o método to_period() com 'M' para obter informações no formato de meses
# * Criando a coluna order_purcharse_month

# %%
df2['order_purchase_month'] = df2.order_purchase_timestamp.dt.to_period('M').astype(str)


# %%
df2.order_purchase_month.head()

# %% [markdown]
# **Visualizando a nova coluna no dataframe**

# %%
df2.head()

# %% [markdown]
# <h3>Cria a variável vendas_por_mes que é a soma do valor dos produtos agrupados por mês</h3>

# %%
vendas_por_mes = df2.groupby(by='order_purchase_month').order_products_value.sum()


# %%
type(vendas_por_mes)

# %% [markdown]
# <h3>Visualizando os valores de vendas por mês</h3>

# %%
vendas_por_mes.head()


# %%
vendas_por_mes.index.item


# %%
vendas_por_mes.values

# %% [markdown]
# **Pontos importantes a lembrar**
# * init_notebook_model()
# * plotly.offline.iplot()
# %% [markdown]
# <h3>Vendas por mês</h3>
# * por padrão o iplot() plota um gráfico de linha, com sentido de valor acumulado

# %%
import plotly.graph_objs as go
import plotly.offline as py


# %%
data = [go.Scatter(x=vendas_por_mes.index, y=vendas_por_mes.values)]
py.iplot(data)

# %% [markdown]
# <h3>Gráfico de Barras</h3>
# * Customizando gráficos de barras: títulos e labels dos eixos

# %%



