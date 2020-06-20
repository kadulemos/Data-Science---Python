# -*- coding: utf-8 -*-
"""PANDAS_Merge_Datasets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tl-hpZnuk6VCN8kR7K47d-8l29o62U7B

<h2>Python para Análise de Dados</h2>

**Consulta os dados em mais de um dataset**
"""

import pandas as pd

"""**Carregando o dataset de pedidos**"""

orders = pd.read_csv('/content/drive/My Drive/Colab Notebooks/ Data Science - Minerando Dados/datasets/olist_orders_dataset.csv')

orders.head()

"""**Carregando o dataset de itens pedidos**"""

orders_items = pd.read_csv('/content/drive/My Drive/Colab Notebooks/ Data Science - Minerando Dados/datasets/olist_order_items_dataset.csv')

orders_items.head()

"""**Opções de merge**

**Tipos de *join* (ligações)**

*   INNER JOIN (Padrão) - Retorna apenas os resgistros que contém a mesma chave em ambos os DataFrames.
*   LEFT JOIN - Retorna todos os registros do DataFrame à esquerda independente se contémk um correspondente à direita.
*   RIGHT JOIN - Retorna todos os registros do DataFrame à direita independente se contém um correspondente à esquerda.
*   OUTER JOIN - Retorna todos os registros de ambos os DataFrames.
"""

from IPython.display import Image
Image('/content/drive/My Drive/Colab Notebooks/ Data Science - Minerando Dados/datasets/joins.png')

"""**Consultando os dados nos dois datasets e ligando através da chave order_id**

* Selecionando os atributos do dataset **orders (pedidos)**
  * order_id (id do pedido)
  * order_status (status do pedido)
  * order_approved_at (data e hora da aprovação do pedido)

* Selecionando os atributos do dataset **orders_items (itens dos pedidos)
  * product_id (id do produto)
  * seller_id (id do vendedor)
  * price (preço do produto)
  * freight_value (valor do frete)
"""

query = pd.merge(orders[['order_id', 'order_status', 'order_approved_at']], orders_items[['order_id', 'product_id', 'seller_id', 'price', 'freight_value']], on='order_id')

query.head()

"""**Consulta todos os pedidos independete se contém itens associados - Left Join**"""

query = pd.merge(orders[['order_id', 'order_status', 'order_approved_at']], 
                 orders_items[['order_id', 'product_id', 'seller_id', 'price', 'freight_value']], 
                 on='order_id', how='left')

query.isnull().sum()

"""**Consultando todos itens pedidos independente se contém pedidos assoiados - Right Join**"""

query = pd.merge(orders[['order_id', 'order_status', 'order_approved_at']], 
                 orders_items[['order_id', 'product_id', 'seller_id', 'price', 'freight_value']],
                 on='order_id', how='right')

query.isnull().sum()

"""**Consulta todos os registros nos dois DataFrames - Outer Join**"""

query = pd.merge(orders[['order_id', 'order_status', 'order_approved_at']],
                 orders_items[['order_id', 'product_id', 'seller_id', 'price', 'freight_value']],
                 on='order_id', how='outer')

query.isnull().sum()
