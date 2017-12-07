# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd
import lifelines as ll
import numpy as np

#%%

df = pd.read_csv("Documents\\Sobrevivencia_final\\Untitled Folder\\dados_Lista.csv",
                 encoding = "latin-1")
df1 = df.assign(data_inicio = pd.to_datetime(df.data_inicio_dor + ' ' + df.hora_inicio_dor).values,
                data_fim = pd.to_datetime(df.data_fim_dor + ' ' + df.hora_fim_dor).values,
                data_coleta = pd.to_datetime('2016-06-05' + ' ' + df.hora_ultimo_contato).values,
                censura = np.where(np.isnan(df.data_fim_dor), 0, 1),
                tempo = np.where(np.isnan(df.data_fim_dor), df.data_coleta - df.data_inicio,
                                 df.data_fim - df.data_inicio))

print(df1.head())

#%%

