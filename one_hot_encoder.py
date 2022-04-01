
# Archivo utilizado para crear la función de One Hot Encoding
############################################################# 
#%%
# Función auxiliar: Toma un df de variables categoricas y selección el top_x de categorias
def one_hot_top_x(cat_df, variable,top_x_labels):
    for label in top_x_labels:
        cat_df[variable+'_'+label] = np.where(cat_df[variable]==label,1,0)

# Función One Hot Encoder: Toma un DF y le hace una transformación de One Hot Encoder para con las categorias más repetidas 
def one_hot_encoder(df,top_x):
    # Separo variables categoricas de númericas
    num_cols = df.select_dtypes(include=['float64', 'int']).columns.to_list()
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.to_list()
    
    # Armo un DF solo con variables categoricas
    cat_df = df.drop(num_cols,axis=1)
    # Armo un DF solo con variables categoricas
    num_df = df.drop(cat_cols,axis=1)
   
    # Itero entre las variables categoricas y me quedo con el top 10 variables
    for variable in cat_cols:
        top_10 = [x for x in cat_df[variable].value_counts().sort_values(ascending=False).head(top_x).index]
        one_hot_top_x(cat_df,variable,top_10)
    
    cat_df = cat_df.drop(cat_cols,axis=1)
    df = pd.concat([cat_df,num_df], axis =1)
    
    return df
#%%