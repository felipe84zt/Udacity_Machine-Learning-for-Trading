#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import altair as alt
alt.data_transformers.disable_max_rows()

alt.renderers.enable('notebook')


# In[183]:


def plot_stocks(df_precos_acoes,lista_acoes):
    
    df_acoes=df_precos_acoes[df_precos_acoes['symbol'].isin(lista_acoes)]
    df_acoes.loc[df_acoes['volume']>=0,'volume']=df_acoes['close_adjusted']*df_acoes['volume']
    df_acoes.loc[df_acoes['close_adjusted']>=0,'close_adjusted']=np.log(df_acoes['close_adjusted'])
    
    brush = alt.selection(type='interval',encodings=['x'],fields=['date:T','symbol:N'])
    pts=alt.selection(type="multi",encodings=['x'])
    
    bar = alt.Chart(df_acoes).mark_bar().encode(alt.X('symbol:N',axis=alt.Axis(titleOpacity=0)),alt.Y('median(split_coefficient):Q',axis=None),                                                color=alt.condition(pts,alt.ColorValue("steelblue"), alt.ColorValue("grey"))).properties(width=800,height=100).add_selection(pts)
       
    lower=alt.Chart(df_acoes).mark_circle(size=4).encode(alt.X('date:T'),alt.Y('close_adjusted:Q',axis=alt.Axis(title='log_close_adjusted')),color='symbol:N',facet=alt.Facet('symbol:N',title='Stocks'),tooltip=['date:T']).properties(title='Prices',width=180,height=180,columns=4).transform_filter(pts)
    
    upper = alt.Chart(df_acoes, height=400, width=800).mark_area(interpolate='monotone').encode(alt.X('yearmonth(date):T',axis=alt.Axis(format=('%b %Y'),domain=False,tickSize=0)),                                                                                               alt.Y('sum(volume):Q',stack='normalize'),alt.Color('symbol:N',scale=alt.Scale(scheme='dark2'))).properties(title='Volume').transform_filter(pts)
    
    
    
    return bar & upper & lower


# In[89]:


def plot_stock_year(acao,df_acoes):
    
    serie_ = df_acoes[df_acoes['symbol']==acao]
    grafico=alt.Chart(serie_).mark_area().encode(alt.X('month(date):T'),alt.Y('close_adjusted:Q',axis=alt.Axis(format='~s')),                                        facet=alt.Facet('year(date):O')).properties(title=acao,width=90,height=80,columns=5)
    
    return grafico


# In[ ]:




