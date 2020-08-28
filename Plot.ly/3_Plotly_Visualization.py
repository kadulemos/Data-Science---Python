# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Visualização de dados com Plot.ly##
# %% [markdown]
# ## Trabalhando com dados financeiros.
# %% [markdown]
# - `Séries temporais`
# - `Dados de Ações ou ativos do mercado financeiro.`
# %% [markdown]
# **Importe o pandas e ler dados de preços**

# %%
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

# %% [markdown]
# **Visulizando a série de dados**

# %%
df.head()

# %% [markdown]
# **Plotando preços de fechamento da ação AAPL (apple)**

# %%
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

data = [go.Scatter(
          x=df.Date,
          y=df['AAPL.Close'])]

data_obj = go.Figure(data = data) 

pio.show(data_obj)

# %% [markdown]
# **Customizando Faixas de Eixos (Range)**

# %%
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

trace_high = go.Scatter(
                x=df.Date,
                y=df['AAPL.High'],
                name = "AAPL High",
                line = dict(color = '#17BECF'),
                opacity = 0.8)

trace_low = go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name = "AAPL Low",
                line = dict(color = '#7F7F7F'),
                opacity = 0.8)

data = [trace_high,trace_low]

layout = go.Layout(
    title = "Faixa de Data Customizada",
    xaxis = dict(
        range = ['2016-07-01','2016-12-31'])
)

fig = go.Figure(data = data, layout = layout)
pio.show(fig, filename = "Manually Set Range")

# %% [markdown]
# **Rangeslider e Rangeselector**

# %%
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

trace_high = go.Scatter(
    x=df.Date,
    y=df['AAPL.High'],
    name = "AAPL High",
    line = dict(color = '#17BECF'),
    opacity = 0.8)

trace_low = go.Scatter(
    x=df.Date,
    y=df['AAPL.Low'],
    name = "AAPL Low",
    line = dict(color = '#7F7F7F'),
    opacity = 0.8)

data = [trace_high,trace_low]

layout = go.Layout(
    title="Série com Rangeslider e Botoes",
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

fig = go.Figure(data=data, layout=layout)
pio.show(fig)

# %% [markdown]
# **Trabalhando com Candlesticks**

# %%
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.io as pio

import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])

data = go.Figure(trace)
pio.show(data, filename='simple_candlestick')

# %% [markdown]
# **Sem rangerslider**

# %%
import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])

layout = go.Layout(
    xaxis = dict(
        rangeslider = dict(
            visible = False
        )
    )
)

data = [trace]

fig = go.Figure(data=data,layout=layout)
pio.show(fig, filename='simple_candlestick_without_range_slider')

# %% [markdown]
# **Customizando candlesticks**

# %%
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(
    x=df['Date'],
    open=df['AAPL.Open'],
    high=df['AAPL.High'],
    low=df['AAPL.Low'],
    close=df['AAPL.Close'],
    increasing=dict(line=dict(color= '#17BECF')),
    decreasing=dict(line=dict(color= '#7F7F7F'))
)
data = [trace]

data_obj = go.Figure(data)
pio.show(data_obj, filename='styled_candlestick')

# %% [markdown]
# **Inserindo anotações**

# %%
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
from datetime import datetime

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

trace = go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])
data = [trace]

layout = {
    'title': 'Apple Preços no Periodo',
    'yaxis': {'title': 'AAPL Stock'},
    'shapes': [{
        'x0': '2016-12-09', 'x1': '2016-12-09',
        'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
        'line': {'color': 'rgb(30,30,30)', 'width': 2}
    }],
    'annotations': [{
        'x': '2016-12-09', 'y': 0.05, 'xref': 'x', 'yref': 'paper',
        'showarrow': False, 'xanchor': 'left',
        'text': 'Inicio do ciclo de alta'
    }]
}
fig = go.Figure(data=data, layout=layout)
pio.show(fig)


