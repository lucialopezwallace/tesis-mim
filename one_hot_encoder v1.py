# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 10:38:01 2022

@author: lucia.lopez_kavak
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:45:00 2022

@author: lucia.lopez_kavak
"""
df = pd.read_csv('data_publications_pesos.csv', sep=";")

# Observamos nuestro dataset
df.info()
df.shape
df.isna().sum().sort_values()
df = df.drop('title',axis=1)

def one_hot_top_x(cat_df, variable,top_x_labels):
    for label in top_x_labels:
        cat_df[variable+'_'+label] = np.where(cat_df[variable]==label,1,0)

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
    
new_df = one_hot_encoder(df,10)  

# Verifico mi one hot encoder
for col in new_df.columns:
    print(col,":", len(new_df[col].unique()), 'labels')
