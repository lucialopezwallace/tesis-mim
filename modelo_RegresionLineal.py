# Archivo donde desarollamos nuestro modelo de Regresion Lineal
############################################################### 

#%%
i

#%%
# Changing the file read location to the location of the dataset
datos_meli = pd.read_excel('data_ready_to_model.xlsx')
datos_kavak = pd.read_csv('base_kavak.csv', sep=";")
#%%
# Uno los DF
#%%
frames = [datos_meli, datos_kavak]
datos = pd.concat(frames)
#%%
datos = one_hot_encoder(datos,10)
datos_meli = datos[(datos['type_meli'] == 1)] 
datos_meli = datos_meli.drop('type_kavak',axis=1)
datos_meli = datos_meli.drop('type_meli',axis=1)
#%%

#separate the other attributes from the predicting attribute
x = datos_meli.drop('precio',axis=1)

#separte the predicting attribute into Y for model training 
y = datos_meli['precio']
y_ln = np.log(datos_meli['precio'])


X_train, X_test, y_train_ln, y_test_ln = train_test_split(
                                        x,
                                        y_ln,
                                        train_size   = 0.8,
                                        random_state = 1234,
                                        shuffle      = True
                                    )

#%%
print("Partición de entrenamiento")
print("-----------------------")
print(y_train_ln.describe())

print("Partición de test")
print("-----------------------")
print(y_test_ln.describe())


#%%
#----------------------------------------Modelo de Regresion Lineal
model = LinearRegression()
model.fit(X_train, y_train_ln)
y_pred_ln = model.predict(X_test)

#  Saco exponencial de los valores de Y
y_test = np.exp(y_test_ln)
y_pred = np.exp(y_pred_ln)

#%%
#%%
print('Mean Absolute Error:', round(metrics.mean_absolute_error(y_test, y_pred)/1000000,2))

# MAE: Mean Absolute Error: 1.03 --> Con outliers
# MAE: Mean Absolute Error: 0.56 --> Sin ourliers
# Mean Absolute Error: 0.48 --> Aplicando LN a Precio (error)
# Mean Absolute Error: 0.86
#%%

#%%
print('Mean Squared Error:', round(metrics.mean_squared_error(y_test, y_pred)/1000000,2))
# MSE: Mean Squared Error: 3,732,143.07
# MSE: Mean Squared Error: 6,599,540.41 --> Con LN   
print('Root Mean Squared Error:', round(np.sqrt(metrics.mean_squared_error(y_test, y_pred))/1000000,2))
# Root Mean Squared Error: 1.93
# Root Mean Squared Error: 0.74
# Root Mean Squared Error: 2.57 --> Con LN




####################################################
#### Prueba de datos de Kavak
#%%
# Separo en Y y X
datos_kavak = datos[(datos['type_kavak'] == 1)] 
datos_kavak = datos_kavak.drop('type_kavak',axis=1)
datos_kavak = datos_kavak.drop('type_meli',axis=1)

#separate the other attributes from the predicting attribute
x_kavak = datos_kavak.drop('precio',axis=1)

#separte the predicting attribute into Y for model training 
y_kavak = datos_kavak['precio']

#%%
# Predigo las x_kavak
y_pred_kavak_ln = model.predict(x_kavak)
#%%

#%%
#  Saco exponencial de los valores de Y
y_pred_kavak = np.exp(y_pred_kavak_ln)/1000
#%%
print('Mean Absolute Error:', round(metrics.mean_absolute_error(y_kavak, y_pred_kavak)/1000000,2))
# Mean Absolute Error: 126.93
#%%