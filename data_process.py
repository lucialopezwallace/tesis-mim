# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 10:05:22 2022

@author: lucia.lopez_kavak
"""
import pandas as pd
import numpy as np

# Changing the file read location to the location of the dataset
df = pd.read_csv('data_publications.csv', sep=";")

# Observamos nuestro dataset
df.info()
df.shape
# (51360, 9)

# Evaluamos si tiene duplicados
df_new = df.drop_duplicates()
df_new.shape
# (43736, 9)
# 7624 filas eliminadas

# Evaluamos si tiene nulos
df_new.isna().sum().sort_values()
# provincia      9

# Sacamos los datos que estan en USD
df_new_ars = df_new.drop(df_new[df_new['currency']=='U$S'].index)
df_new_ars.shape
df_new_ars.info()
df_new_ars.describe()
# (35705, 9)

##################################### Dataset de datos privados####

# Changing the file read location to the location of the dataset
df_k = pd.read_csv('base_kavak.csv', sep=";")

# Observamos nuestro dataset
df_k.info()
df_k.shape
# (2532, 15)

modelos = df_k['iin_model'].unique().tolist()

####################################################################

# Sumamos la columna modelo
df_new_ars['modelo'] = pd.NaT
i = 0
for t in df['title']:
    for m in modelos:
        if m.lower() in t.lower():
            df_new_ars['modelo'][i] = m
    i = i + 1
            
        
# Vemos la forma
df_new_ars.shape
# (35705, 10)
df_new_ars.isna().sum().sort_values()
# provincia         8
# modelo         3836

df_new_ars = df_new_ars.drop(df_new_ars[df_new_ars['modelo'].isna()].index)
df_new_ars.shape
# (31869, 10)

# Guardamos la información en un csv
df_new_ars.to_csv('data_publications_process.csv',mode='a', sep=';', encoding='utf-8-sig', index=False)
datos = df_new_ars

################################################## Limpieza de datos

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
datos = outlier_treatment(datos, datos.km)
datos.shape
# (30808, 10)

# Saco outlier Year
datos = outlier_treatment(datos, datos.year)
datos.shape
# (30404, 10)

# Saco outlier Price
datos = outlier_treatment(datos, datos.precio)
datos.shape
# (28600, 10)

# Exporto a un CSV
datos.to_csv('data_ready_to_model.csv',mode='a', sep=';', encoding='utf-8-sig', index=False)
