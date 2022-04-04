# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:05:22 2022

@author: lucia.lopez_kavak
"""

# Archivo utilizado para procesar la base de datos con la que trabajaremos
###########################################################################
 
#%%
# Importo las liberías que utilizaremos
import pandas as pd
import numpy as np
#%%
##################################### Dataset de datos privados####
###################################################################
#%%
# Levanto la base de datos privados con la que trabajeremos
df_k = pd.read_csv('base_kavak.csv', sep=";")

# Observamos nuestro dataset
df_k.info()
df_k.shape
# (2532, 15)

# Armo una lista de los modelos disponibles en el dataset
modelos = df_k['modelo'].unique().tolist()
# 146 modelos




##################################### Dataset de datos públicos####
###################################################################
#%% 
# Levanto la base de datos públicos con la que trabajeremos
df = pd.read_csv('data_publications.csv', sep=";")

# Observamos nuestro dataset
df.info()
df.shape
# (51360, 9)

# Evaluamos si tiene duplicados
print(df.duplicated().sum())
# 7624 filas duplicadas

# Sacamos los valores duplicados
df_new = df.drop_duplicates()
df_new.shape
# (43736, 9)

# Evaluamos si tiene nulos
df_new.isna().sum().sort_values()
# provincia      9

# Sacamos aquellas publicadas con valor en Dolares
df_new_ars = df_new.drop(df_new[df_new['currency']=='U$S'].index)

df_new_ars.shape
df_new_ars.info()
df_new_ars.describe()
# (35705, 9)

 
# Sumamos la columna modelo al data set público (a partir de los datos privados)
df_new_ars['modelo'] = pd.NaT
i = 0
for t in df_new_ars['title']:
    for m in modelos:
        if m.lower() in t.lower():
            df_new_ars['modelo'][i] = m
    i = i + 1


  
# Vemos la forma
df_new_ars.shape
# (35705, 10)


# Evaluo valores con nulos
df_new_ars.isna().sum().sort_values()
# provincia         8
# modelo         14711
 
# Eliminamos los valores con modelo nulo
df_new_ars = df_new_ars.drop(df_new_ars[df_new_ars['modelo'].isna()].index)
df_new_ars = df_new_ars.drop('title',axis=1)

df_new_ars.shape
# (20994, 9)


# Guardamos la información en un csv
# df_new_ars.to_csv('data_publications_process.csv',mode='a', sep=';', encoding='utf-8-sig', index=False)
# datos.to_excel('data_ready_to_model.csv',mode='a', sep=';', encoding='utf-8-sig', index=False)
#%%
# Exporto a un Excel
datos = df_new_ars
datos.to_excel('data_ready_to_model.xlsx', index=False)





################################################## Limpieza de datos##
######################################################################

# 1 - Sacamos los outliers

# Función que termina los outliers
def outlier_treatment(df,datacolumn):
    sorted(datacolumn)
    Q1,Q3 = np.percentile(datacolumn , [25,75])
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    df.drop(df[(datacolumn < lower_range) | (datacolumn > upper_range)].index, inplace=True)
    return df

# Saco outlier KM
# datos = outlier_treatment(datos, datos.km)
# datos.shape
# (30808, 10)

# Saco outlier Year
# datos = outlier_treatment(datos, datos.year)
# datos.shape
# (30404, 10)

# Saco outlier Price
# datos = outlier_treatment(datos, datos.precio)
# datos.shape
# (28600, 10)

