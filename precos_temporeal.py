#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import yfinance as yf
import time


# In[2]:


def precos_temporeal(acao,tempo,intervalo):
    
    acao_alvo=yf.Ticker(acao)
    t=0
    prices=[]
    delta_time=[]
    start=time.time()
    total_iteracoes=tempo

    while t<total_iteracoes:
        try:
            prices.append(acao_alvo.history(period='max').tail(1)[['Close']].values[0][0])
            delta_time.append(time.time()-start)
            time.sleep(intervalo)
          
            t+=1
        
        except:
            time.sleep(1)
            
    
    df_acao=pd.DataFrame(columns=['Price','Delta_Time'])
    df_acao['Price']=prices
    df_acao['Delta_Time']=delta_time
    
    return df_acao


# In[38]:


def historico(lista_acoes, inicio='1980-01-01', fim='2025-01-01'):
    
    lista_historicos=[]
    
    for acao in lista_acoes:
       
        t=0
        q=0
        p=0
        while t==0:
            try:
                acao_alvo = yf.Ticker(acao)
                historico_acao = acao_alvo.history(start=inicio, end=fim)
                lista_historicos.append(historico_acao)
                t=1
                p+=1
            
            except:
                time.sleep(1)
                p+=1
                q+=1
                print('Download em Andamento: ',q,'/',p,' tentativas sem sucesso.')
         
    return lista_historicos
        


# In[ ]:





# In[ ]:





# In[ ]:




