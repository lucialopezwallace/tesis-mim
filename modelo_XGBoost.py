# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:27:43 2022

@author: lucia.lopez_kavak
"""

from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV
import pandas as pd

# Changing the file read location to the location of the dataset
df = pd.read_csv('data_ready_to_model.csv', sep=";")

# Observamos nuestro dataset
df.info()
df.shape
df.isna().sum().sort_values()
df = df.drop('title',axis=1)
#separate the other attributes from the predicting attribute
x = df.drop('precio',axis=1)
print(x)
type(x)
x = one_hot_encoder(x,10)
#separte the predicting attribute into Y for model training 
y = df['precio']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)

xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)

xg_reg.fit(X_train,y_train)

y_pred = xg_reg.predict(X_test)

print('Mean Absolute Error:', round(metrics.mean_absolute_error(y_test, y_pred)/1000000,2))
# MAE: Mean Absolute Error: 1.08
# MAE: Mean Absolute Error: 0.87
print('Mean Squared Error:', round(metrics.mean_squared_error(y_test, y_pred)/1000000,2))
# MSE: Mean Squared Error: 7,272,534.09
# MSE: Mean Squared Error: 1,430,040.43
print('Root Mean Squared Error:', round(np.sqrt(metrics.mean_squared_error(y_test, y_pred))/1000000,2))
# Root Mean Squared Error: 2.7
# Root Mean Squared Error: 1.2


########################################## Optimizando los hiperparametros
########################################## GridSearchCV
from sklearn.model_selection import GridSearchCV

params = { 'max_depth': [3,6,10],
           'learning_rate': [0.01, 0.05, 0.1],
           'n_estimators': [100, 500, 1000],
           'colsample_bytree': [0.3, 0.7]}

xgbr = xgb.XGBRegressor(seed = 20)
clf_GS = GridSearchCV(estimator=xgbr, 
                   param_grid=params,
                   # scoring='neg_mean_squared_error',
                   scoring = 'neg_mean_absolute_error'
                   verbose=1)
clf_GridS.fit(X_train, y_train)
print("Best parameters:", clf.best_params_)

y_pred_test = clf_GridS.best_estimator_(X_test)
y_pred_train = clf_GridS.best_estimator_(X_train)

print('Root Mean Squared Error:', round(np.sqrt(metrics.mean_squared_error(y_test, y_pred_test))/1000000,2))
print('Root Mean Squared Error:', round(np.sqrt(metrics.mean_squared_error(y_train, y_pred_train))/1000000,2))


# Best parameters: {'colsample_bytree': 0.7, 'learning_rate': 0.1, 'max_depth': 10, 'n_estimators': 1000}
print("Lowest RMSE: ", round(((-clf_GridS.best_score_)**(1/2.0)/1000000),2))
# Lowest RMSE:  0.44
print("Lowest MSE: ", round((-clf_GridS.best_score_/1000000),2))
# Lowest MSE:  197.270.95

########################################## RandomSearch

params = { 'max_depth': [3, 5, 6, 10, 15, 20],
           'learning_rate': [0.01, 0.1, 0.2, 0.3],
           'subsample': np.arange(0.5, 1.0, 0.1),
           'colsample_bytree': np.arange(0.4, 1.0, 0.1),
           'colsample_bylevel': np.arange(0.4, 1.0, 0.1),
           'n_estimators': [100, 500, 1000]}

xgbr = xgb.XGBRegressor(seed = 20)
clf_RandomS = RandomizedSearchCV(estimator=xgbr,
                         param_distributions=params,
                         scoring='neg_mean_squared_error',
                         n_iter=25,
                         verbose=1)
clf_RandomS.fit(X_train, y_train)
print("Best parameters:", clf_RandomS.best_params_)
# print("Best parameters:", clf_RandomS.best_params_)
# Best parameters: {'subsample': 0.8999999999999999, 'n_estimators': 500, 'max_depth': 15, 'learning_rate': 0.2, 'colsample_bytree': 0.8999999999999999, 'colsample_bylevel': 0.7}
print("Lowest RMSE: ", round(((-clf_RandomS.best_score_)**(1/2.0)/1000000),2))
# Lowest RMSE:  0.46
print("Lowest MSE: ", round((-clf_RandomS.best_score_/1000000),2))
# Lowest MSE:  213.030.49