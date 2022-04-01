# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:36:30 2022

@author: lucia.lopez_kavak
"""
#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_selector
from sklearn.model_selection import cross_val_score
from sklearn import metrics
#%%
#%%
# Changing the file read location to the location of the dataset
df = pd.read_csv('data_ready_to_model.csv', sep=";")
#%%
# Observamos nuestro dataset
df.info()
df.shape
df.isna().sum().sort_values()
df = df.drop('title',axis=1)

#%%
#separate the other attributes from the predicting attribute
x = df.drop('precio',axis=1)
print(x)
type(x)
x = one_hot_encoder(x,10)
#separte the predicting attribute into Y for model training 
y = df['precio']
y_ln = np.log(df['precio'])
#%%

#%%
# V0
#X_train, X_test, y_train, y_test = train_test_split(
#                                        x,
#                                        y,
#                                        train_size   = 0.8,
#                                        random_state = 1234,
#                                        shuffle      = True
#                                    )

# V1
X_train, X_test, y_train_ln, y_test_ln = train_test_split(
                                        x,
                                        y_ln,
                                        train_size   = 0.8,
                                        random_state = 1234,
                                        shuffle      = True
                                    )

#%%
print("Partición de entrenamento")
print("-----------------------")
print(y_train.describe())

print("Partición de test")
print("-----------------------")
print(y_test.describe())


#%%
#----------------------------------------Modelo de Regresion Lineal
model = LinearRegression()
model.fit(X_train, y_train_ln)
y_pred_ln = model.predict(X_test)
y_test = np.exp(y_test_ln)
y_pred = np.exp(y_pred_ln)
df = pd.DataFrame({'Actual': y_test_ln/1000000, 'Predicted': y_pred_ln/1000000})
#%%
#%%
print('Mean Absolute Error:', round(metrics.mean_absolute_error(y_test, y_pred)/1000000,2))
print('Mean Absolute Error:', round(metrics.mean_absolute_error(y_test, y_pred)/1000000,2))

# MAE: Mean Absolute Error: 1.03 --> Con outliers
# MAE: Mean Absolute Error: 0.56 --> Sin ourliers
# Mean Absolute Error: 0.48 --> Aplicando LN a Precio
#%%

#%%
print('Mean Squared Error:', round(metrics.mean_squared_error(y_test, y_pred)/1000000,2))
# MSE: Mean Squared Error: 3,732,143.07
# MSE: Mean Squared Error:     
print('Root Mean Squared Error:', round(np.sqrt(metrics.mean_squared_error(y_test, y_pred))/1000000,2))
# Root Mean Squared Error: 1.93
# Root Mean Squared Error: 0.74
#%%
