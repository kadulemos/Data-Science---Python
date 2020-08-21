# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# <h2>Visualização de dados Reais<h2>

# %%
import pandas as pd
import numpy as np


# %%
# Importando Cufflinks
import cufflinks as cf
from plotly.offline import plot, iplot


# %%
# Ativando o modo Offline
cf.go_offline()


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


# %%
df2.order_status.value_counts()


# %%
df2.order_status.value_counts().iplot(kind='bar')


# %%
df2.info()

# %% [markdown]
# Transformando colunas para o formato datetime

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
#  <h3>Cria a variável vendas_por_mes que é a soma do valor dos produtos agrupados por mês</h3>

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
# 
# * Customizando gráficos de barras: títulos e labels dos eixos

# %%
data = [go.Bar(x = vendas_por_mes.index, y = vendas_por_mes.values, marker = {'color': 'lightblue'})]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Vendas no Período', 
                                yaxis = {'title': 'Valores em Vendas'}, 
                                xaxis = {'title':'Periodo'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# **Definindo ajustes em linhas e cores**
# * Parâmetro opacity e width

# %%
data = [go.Bar(x = vendas_por_mes.index, 
                y = vendas_por_mes.values, 
                marker = {'color': 'lightblue',
                            'line': {'color': '#333',
                                        'width': 2}
                                    },
                            opacity = 0.7
                )
        ]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Vendas no Período', 
                                yaxis = {'title': 'Valores em Vendas'}, 
                                xaxis = {'title':'Periodo'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# **Destacando uma barra**

# %%
cores = []


# %%
vendas_por_mes.index


# %%
vendas_por_mes

# %% [markdown]
# Valor de média para ser testado

# %%
media = vendas_por_mes.values.mean()


# %%
media

# %% [markdown]
# Alimentando a lista de cores

# %%
# Se o valor de vendas do mês for menor que a média a lista de cor será vermelha, senão azul
for x in vendas_por_mes.values:
    if x < media:
        cores.append('red')
    else:
        cores.append('lightblue')

# %% [markdown]
# Visulizando a lista de cores

# %%
cores

# %% [markdown]
# **Plotando o gráfico com a regra criada**

# %%
data = [go.Bar(x = vendas_por_mes.index, 
                y = vendas_por_mes.values, 
                marker = {'color': cores, # lista de cores
                            'line': {'color': '#333',
                                        'width': 2}
                                    },
                            opacity = 0.7
                )
        ]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Vendas no Período', 
                                yaxis = {'title': 'Valores em Vendas'}, 
                                xaxis = {'title':'Periodo'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# **Gráficos de Vendas no Período**
# * Destaca a barra com o maior valor e minimiza a visão de todas as outras

# %%
maximo_de_vendas = vendas_por_mes.values.max()


# %%
maximo_de_vendas

# %% [markdown]
# **Alimenta a lista de cores**

# %%
cores = []
for x, y in zip (vendas_por_mes.values, vendas_por_mes.index):
    if x == maximo_de_vendas:
        mes_maximo_de_vendas = y
        cores.append('blue')
    else:
        cores.append('lightgray')


# %%
mes_maximo_de_vendas


# %%
cores

# %% [markdown]
# **Plotando o gráfico com o valor máximo estabelecido**

# %%
data = [go.Bar(x = vendas_por_mes.index, 
                y = vendas_por_mes.values, 
                marker = {'color': cores, # lista de cores
                            'line': {'color': '#333',
                                        'width': 2}
                                    },
                            opacity = 0.7
                )
        ]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Vendas no Período', 
                                yaxis = {'title': 'Valores em Vendas'}, 
                                xaxis = {'title':'Periodo'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# **Plotando o gráfico de vendas com um destaque de cor e anotação para o mês que teve mais vendas**

# %%
data = [go.Bar(x = vendas_por_mes.index, 
                y = vendas_por_mes.values, 
                marker = {'color': cores, # lista de cores
                            'line': {'color': '#333',
                                        'width': 2}
                                    },
                            opacity = 0.7
                )
        ]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Vendas no Período', 
                                yaxis = {'title': 'Valores em Vendas'}, 
                                xaxis = {'title':'Periodo'},
                                # texto na barra de destaque
                                annotations= [{'text': 'Mês destaque de vendas',
                                                'x': mes_maximo_de_vendas,
                                                'y': maximo_de_vendas}
                                                ]
                                )

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# **Visualizando duas informações no mesmo gráfico**
# * Vamos definir alguns valores fictícios para vendas do ano anterior

# %%
vendas_ano_anterior = vendas_por_mes - 10000.00

# %% [markdown]
# Gráfico de barras aninhadas

# %%
data = [go.Bar(x = vendas_por_mes.index, 
                y = vendas_por_mes.values, 
                marker = {'color': cores, # lista de cores
                            'line': {'color': '#333',
                                        'width': 2}
                                    },
                            opacity = 0.7,
                            name = '2017'
                ),
    #Definindo outro plot de barras com valores dos meses passados
        go.Bar(x = vendas_ano_anterior.index, 
                y = vendas_ano_anterior.values,
                name='2016',
                marker = {'color': 'lightgreen',
                            'line': {'color': '#333',
                                        'width': 2}
                                    },
                            opacity = 0.7,
                )
        ]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Vendas no Período', 
                                yaxis = {'title': 'Valores em Vendas'}, 
                                xaxis = {'title':'Periodo'},
                                 # texto na barra de destaque
                                annotations= [{'text': 'Mês destaque de vendas',
                                                'x': mes_maximo_de_vendas,
                                                'y': maximo_de_vendas}
                                                ]
                                )

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# **Vendas por categorias de produtos**
# * Conta quantos produtos por categoria e coloca dentro da variável vendas_produto_por_categoria

# %%
vendas_produto_por_categoria = df2.groupby(by='product_category_name').id.count()


# %%
vendas_produto_por_categoria

# %% [markdown]
# Filtra categorias com quantidade de vendas maiores que 1

# %%
vendas_produto_por_categoria = vendas_produto_por_categoria.loc[vendas_produto_por_categoria > 1]

# %% [markdown]
# Ordena valores do maior para o menor

# %%
vendas_produto_por_categoria.sort_values(ascending=False, inplace=True)

# %% [markdown]
# **Plota gráfico de barras verticais**

# %%
trace0 = go.Bar(x = vendas_produto_por_categoria.index, 
                y = vendas_produto_por_categoria.values, 
                marker = {'color': '#00FF2A'},
                            orientation='v'
                )
data = [trace0]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Vendas por Categoria de Produtos', 
                                xaxis = dict(titlefont = dict(size=40, 
                                color = 'lightgrey'),
                                tickangle = 75),
                                yaxis = {'title':'Quantidade Vendida'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# Alterando Faixa de valores dos eixos somando 10% ao valor máximo

# %%
max_y = max(vendas_produto_por_categoria.values) * 1.10


# %%
trace0 = go.Bar(x = vendas_produto_por_categoria.index, 
                y = vendas_produto_por_categoria.values, 
                marker = {'color': '#00FF2A'},
                            orientation='v'
                )
data = [trace0]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Vendas por Categoria de Produtos', 
                                xaxis = dict(titlefont = dict(size=40, 
                                color = 'lightgrey'),
                                tickangle = 75),
                                #valor máximo da faixa + 10%
                                yaxis = {'title':'Quantidade Vendida',
                                        'range' : [0,max_y]})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig, filename='Vendas por categoria de Produtos')

# %% [markdown]
# **Valor do frete vs Valor de Produto: Existe alguma tendência?**

# %%
trace = go.Scatter(x = df2['order_freight_value'], 
                y = df2['order_products_value'], 
                mode = 'markers',
                marker= {'color' : '#941229'}
                )
# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Valor de Frete x Valor de Produto', 
                                yaxis = {'title':'Valor do Produto'},
                                xaxis = {'title':'Valor do Frete'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# Usando o parâmetro text na visualização (parâmetro hover)

# %%
trace = go.Scatter(x = df2['order_freight_value'], 
                y = df2['order_products_value'], 
                mode = 'markers',
                #Customização do texto a ser exibido no hover
                text='Status do pedido: ' + df2['order_status'] +
                    '<br>' + 'Classe: ' + df2['most_voted_class'],
                #Exibição do hover
                hoverinfo='text+x+y',
                marker= {'color' : '#941229'}
                )
# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Valor de Frete x Valor de Produto', 
                                yaxis = {'title':'Valor do Produto'},
                                xaxis = {'title':'Valor do Frete'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# Customização dos eixos com formato em reais R$

# %%
trace = go.Scatter(x = df2['order_freight_value'], 
                y = df2['order_products_value'], 
                mode = 'markers',
                #Customização do texto a ser exibido no hover
                text='Status do pedido: ' + df2['order_status'] +
                    '<br>' + 'Classe: ' + df2['most_voted_class'],
                #Exibição do hover
                hoverinfo='text+x+y',
                marker= {'color' : '#941229'}
                )
# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Valor de Frete x Valor de Produto',
                                #Definindo exibição dos eixos x e y
                                yaxis = {'title':'Valor do Produto', 'tickformat':'.', 'tickprefix':'R$'},
                                xaxis = {'title':'Valor do Frete', 'tickformat':'.', 'tickprefix':'R$'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# Gráfico de Bolhas: Valor de Frete vs Valor do Produto por número de vendedores

# %%
trace = go.Scatter(x = df2['order_freight_value'], 
                y = df2['order_products_value'], 
                mode = 'markers',
                #Customização do texto a ser exibido no hover
                text='Status do pedido: ' + df2['order_status'] +
                    '<br>' + 'Classe: ' + df2['most_voted_class'],
                #Exibição do hover
                hoverinfo='text+x+y',
                #Parâmetro size e sizemode especifica o comportamento dos pontos
                marker= {'color' : '#941229', 'size': df2['order_sellers_qty']*10, 'sizemode':'area'}
                )
# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
configuracoes_layout = go.Layout(title = 'Valor de Frete x Valor de Produto',
                                #Definindo exibição dos eixos x e y
                                yaxis = {'title':'Valor do Produto', 'tickformat':'.', 'tickprefix':'R$'},
                                xaxis = {'title':'Valor do Frete', 'tickformat':'.', 'tickprefix':'R$'})

#Objeto figura
fig = go.Figure(data=data, layout=configuracoes_layout)

# Plotando o gráfico
py.iplot(fig)

# %% [markdown]
# Valor de Frete vs Valor de Produto por status de entrega

# %%
df2.iplot(x='order_freight_value', 
            y= 'order_products_value', 
            categories='most_voted_subclass', 
            title= 'Valor de Frete vs Valor de Produto', 
            xTitle='Valor de Frete', 
            yTitle= 'Valor Produto')

# %% [markdown]
# Quantidade em média de Itens de um pedido

# %%
data = [go.Histogram(x=df2.order_items_qty)]

layout = go.Layout(title='Quantidade média de itens de um pedido')

fig = go.Figure(data=data, layout=layout)

py.iplot(fig)

# %% [markdown]
# Quantidade média de vendedores de um pedido

# %%
trace1 = go.Histogram(x=df2.order_items_qty, 
                        name='itens', 
                        opacity=0.75)

trace2 = go.Histogram(x=df2.order_sellers_qty, 
                        name='vendedores', 
                        opacity=0.75)

layout = go.Layout(title='Quantidade de itens e Vendedores por pedido',
                    barmode='overlay'
                    )

dados = [trace1, trace2]

fig = go.Figure(data=dados, layout=layout)

py.iplot(fig)

# %% [markdown]
# **Plotando um gráfico de pizza**
# * Qual a distribuição da classificação dos pedidos pelos clientes?

# %%
df2.order_status.value_counts()


# %%
classes_mais_votadas = df2.groupby(by='most_voted_class').id.count()


# %%
classes_mais_votadas


# %%
# mesmo resultado do código acima
classes_mais_votadas = df2.most_voted_class.value_counts()


# %%
classes_mais_votadas


# %%
# Criando gráfico
trace = go.Pie(labels = classes_mais_votadas.index,
                values = classes_mais_votadas.values)

# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
layout = go.Layout(title='Classificação de Clientes sobre Pedidos')

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)

# %% [markdown]
# Parâmetro Direction

# %%
# Criando gráfico
trace = go.Pie(labels = classes_mais_votadas.index,
                values = classes_mais_votadas.values,
                direction='clockwise')

# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
layout = go.Layout(title='Classificação de Clientes sobre Pedidos')

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)

# %% [markdown]
# Customizando gráficos de pizza

# %%
# Criando gráfico

cores = ['#96D38C', 'FEBFFB3', '#E1396C'] #Personalizando as cores

trace = go.Pie(labels = classes_mais_votadas.index,
                values = classes_mais_votadas.values,
                direction='clockwise',
                marker= {'colors' : cores})

# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
layout = go.Layout(title='Classificação de Clientes sobre Pedidos')

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)

# %% [markdown]
# Adicionando linha de contorno, cores

# %%
# Criando gráfico

cores = ['#96D38C', 'FEBFFB3', '#E1396C'] # Personalizando as cores

trace = go.Pie(labels = classes_mais_votadas.index,
                values = classes_mais_votadas.values,
                direction='clockwise',
                marker= {'colors' : cores,
                        'line' : {'color' : '#000000', 'width' : 2} # Linha de contono
                        },
                hoverinfo= 'label+percent+value'
                )

# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
layout = go.Layout(title='Classificação de Clientes sobre Pedidos')

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)

# %% [markdown]
# Destacando porções do gráfico

# %%
# Criando gráfico

cores = ['#96D38C', 'FEBFFB3', '#E1396C'] # Personalizando as cores

trace = go.Pie(labels = classes_mais_votadas.index,
                values = classes_mais_votadas.values,
                direction='clockwise',
                marker= {'colors' : cores,
                        'line' : {'color' : '#000000', 'width' : 2} # Linha de contono
                        },
                hoverinfo= 'label+percent+value',
                pull= [0,0,0.1] # Destacando uma porção do gráfico através da posição da fatia
                )

# Armazenamento gráfico em uma lista
data = [trace]

#Criando Layout
layout = go.Layout(title='Classificação de Clientes sobre Pedidos')

# Criando figura que será exibida
fig = go.Figure(data=data, layout=layout)

py.iplot(fig)

# %% [markdown]
# <h2>Exportando nosso gráfico para conta do Plotly na nuvem</h2>
# 
# * Criar conta no portal plot.ly
# * Obter credenciais da API
# * Importa métodos para plot **online**
# * Substitua o método iplot() pelo método plot()

# %%



