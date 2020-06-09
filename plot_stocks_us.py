#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import altair as alt
alt.data_transformers.disable_max_rows()

alt.renderers.enable('notebook')


# In[62]:


def plot_stocks(df_precos_acoes,lista_acoes,data=['1998-01-01','2021-01-01'],normalizacao='div_index_0'):
    
    df_acoes=df_precos_acoes[df_precos_acoes['symbol'].isin(lista_acoes)]
    df_acoes=df_acoes[(df_acoes['date']>=data[0]) & (df_acoes['date']<=data[1])]
    df_acoes.loc[df_acoes['volume']>=0,'volume']=df_acoes['close_adjusted']*df_acoes['volume']
    df_acoes=df_acoes.sort_values(by=['date'])
    
    if normalizacao=='div_index_0':
        
        for acao in lista_acoes:
            df_acoes.loc[(df_acoes['close_adjusted']>=0) & (df_acoes['symbol']==acao),'close_adjusted']=            df_acoes.loc[(df_acoes['close_adjusted']>=0) & (df_acoes['symbol']==acao),'close_adjusted']/df_acoes.loc[(df_acoes['close_adjusted']>=0) & (df_acoes['symbol']==acao),'close_adjusted'].iloc[0]
        
        y_title = 'close_adjusted_normalized'
        
    elif normalizacao=='log':
        
        df_acoes.loc[df_acoes['close_adjusted']>=0,'close_adjusted']=np.log(df_acoes['close_adjusted'])
        y_title = 'close_adjusted_log'
        
    else:
        
        for acao in lista_acoes:
            df_acoes.loc[(df_acoes['close_adjusted']>=0) & (df_acoes['symbol']==acao),'close_adjusted']=            df_acoes.loc[(df_acoes['close_adjusted']>=0) & (df_acoes['symbol']==acao),'close_adjusted']/df_acoes.loc[(df_acoes['close_adjusted']>=0) & (df_acoes['symbol']==acao),'close_adjusted'].iloc[0]
        
        df_acoes.loc[df_acoes['close_adjusted']>=0,'close_adjusted']=round(np.log(df_acoes['close_adjusted']),2)
        y_title = 'close_adjusted_log_normalized'
    
    brush = alt.selection(type='interval',encodings=['x'],fields=['date:T','symbol:N'])
    pts=alt.selection(type="multi",encodings=['x'])
    
    bar = alt.Chart(df_acoes).mark_bar().encode(alt.X('symbol:N',axis=alt.Axis(titleOpacity=0)),alt.Y('median(split_coefficient):Q',axis=None),                                                color=alt.condition(pts,alt.ColorValue("steelblue"), alt.ColorValue("grey"))).properties(width=800,height=100).add_selection(pts)
       
    lower=alt.Chart(df_acoes).mark_circle(size=4).encode(alt.X('date:T'),alt.Y('close_adjusted:Q',axis=alt.Axis(title=y_title)),color='symbol:N',facet=alt.Facet('symbol:N',title='Stocks'),tooltip=['date:T','close_adjusted:Q']).properties(title='Prices',width=180,height=180,columns=4).transform_filter(pts)
    
    upper = alt.Chart(df_acoes, height=400, width=800).mark_area(interpolate='monotone').encode(alt.X('yearmonth(date):T',axis=alt.Axis(format=('%b %Y'),domain=False,tickSize=0)),                                                                                               alt.Y('sum(volume):Q',stack='normalize'),alt.Color('symbol:N',scale=alt.Scale(scheme='dark2'))).properties(title='Volume').transform_filter(pts)
    
    
    return bar & upper & lower


# In[4]:


def plot_stock_year(acao,df_acoes):
    
    serie_ = df_acoes[df_acoes['symbol']==acao]
    grafico=alt.Chart(serie_).mark_area().encode(alt.X('month(date):T'),alt.Y('close_adjusted:Q',axis=alt.Axis(format='~s')),                                        facet=alt.Facet('year(date):O')).properties(title=acao,width=90,height=80,columns=5)
    
    return grafico


# In[5]:


precos_acoes_us = pd.read_csv(r'C:\Users\Felipe\Documents\GitHub\Udacity_Machine-Learning-for-Trading\Data\US_stocks\stocks_latest\stock_prices_latest.csv')


# In[ ]:





# In[ ]:




