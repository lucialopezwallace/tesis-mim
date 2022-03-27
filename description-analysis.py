 
# Archivo donde graficaremos nuestros datos
############################################################# 

# Importo las librerias que utilizaremos
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Levantamos los datos procesados
datos = pd.read_csv('data_publications_process.csv', sep=";")

# Observamos nuestro dataset
datos.shape
datos.info
# (31869, 10)

# Variable precio ---------------------
plt.title('Precio')
plt.xlabel("precio ('000)")
plt.hist(datos['precio']/1000, bins = 70)
plt.show() 

# Cómo ver outliers
sns.boxplot(x=datos['precio'])
plt.show() 

# Variable precio con logartimo ---------------------
plt.title('Precio')
plt.xlabel("precio ('000)")
plt.hist(np.log(datos['precio']), bins = 70)
plt.show() 

# Cómo ver outliers
sns.boxplot(x=np.log(datos['precio']))
plt.show() 


# Otra manera de ver outliers para Precio & Año
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(datos['year'], datos['precio'])
ax.set_xlabel('Año')
ax.set_ylabel('Precio')
plt.show()

# Otra manera de ver outliers para Precio & KM
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(datos['km'], datos['precio'])
ax.set_xlabel('KM')
ax.set_ylabel('Precio')
plt.show()


# Variable KMT --------------------------- 
plt.title('Kilometros')
plt.xlabel("KM")
plt.hist(datos['km'], bins = 70)
plt.show()

# Grafico los outliers
sns.boxplot(x=datos['km'])
plt.show()

# Variable Year --------------------------- 
plt.title('Años')
plt.xlabel('year')
plt.hist(datos['year'], bins = 70)
plt.show()

# Grafico los outliers
sns.boxplot(x=datos['year'])
plt.show()

# Relación entre km & precio --------------------------- 

fig, ax = plt.subplots()
fig.set_size_inches(8, 8)
sns.regplot(x="km", y="precio", data=datos,
            scatter_kws={'color':'green', 'alpha':0.3},
            line_kws={'color':'red'})
ax.set_title('Precio vs Kilometraje',
             fontsize=16, weight="bold")
plt.show()

# Relación entre year & precio --------------------------- 

fig, ax = plt.subplots()
fig.set_size_inches(8, 8)
sns.regplot(x="year", y="precio", data=datos,
            scatter_kws={'color':'green', 'alpha':0.3},
            line_kws={'color':'red'})
ax.set_title('Precio vs Año',
             fontsize=16, weight="bold")
plt.show()

# Relación entre marca & precio --------------------------- 

marca_cnt = datos['marca'].value_counts(sort=False).sort_values(ascending=True)

marca_cnt_bar = marca_cnt.plot(kind='barh', y="marca", 
                           legend=False, figsize=(8, 8))
marca_cnt_bar.set_title("# Publicaciones por Marca",
                      fontsize=16, weight="bold")
marca_cnt_bar.set_xlabel("# publicaciones")

plt.show()

# Busco los promedios
precio_marca = datos.pivot_table(index="marca",
                          values=["precio"],
                          aggfunc='mean')
precio_marca.head()

# Los grafico

precio_marca.sort_values("precio", ascending=True, inplace=True)
precio_marca_bar = precio_marca.plot(kind="barh", y="precio", figsize=(8, 8), legend=False)

precio_marca_bar.set_xlabel("Precio promedio")
precio_marca_bar.set_title("Precio promedio por marca",
                  fontsize=16, weight="bold")
plt.show()

# Relación entre provincia & precio --------------------------- 

provincia_cnt = datos['provincia'].value_counts(sort=False).sort_values(ascending=True)
provincia_cnt_bar = provincia_cnt.plot(kind='barh', y="provincia", 
                           legend=False, figsize=(8, 8))
provincia_cnt_bar.set_title("# Publicaciones por Provincia",
                      fontsize=16, weight="bold")
provincia_cnt_bar.set_xlabel("# publicaciones")
plt.show()

# Busco los promedios
precio_provincia = datos.pivot_table(index="provincia",
                          values=["precio"],
                          aggfunc='mean')
precio_provincia.head()

# Los grafico

precio_provincia.sort_values("precio", ascending=True, inplace=True)
precio_provincia_bar = precio_provincia.plot(kind="barh", y="precio", figsize=(8, 8), legend=False)

precio_provincia_bar.set_xlabel("Precio promedio")
precio_provincia_bar.set_title("Precio promedio por provincia",
                  fontsize=16, weight="bold")
plt.show()

# Relación entre localidad & precio --------------------------- 

loc_cnt = datos['localidad'].value_counts(sort=False).sort_values(ascending=True)
loc_cnt_bar = loc_cnt.plot(kind='barh', y="localidad", 
                           legend=False, figsize=(8, 8))
loc_cnt_bar.set_title("# Publicaciones por Localidad",
                      fontsize=16, weight="bold")
loc_cnt_bar.set_xlabel("# publicaciones")
plt.show()

# Busco los promedios
precio_loc = datos.pivot_table(index="localidad",
                          values=["precio"],
                          aggfunc='mean')
precio_loc.head()

# Los grafico

precio_loc.sort_values("precio", ascending=True, inplace=True)
precio_loc_bar = precio_loc.plot(kind="barh", y="precio", figsize=(8, 8), legend=False)

precio_loc_bar.set_xlabel("Precio promedio")
precio_loc_bar.set_title("Precio promedio por localidad",
                  fontsize=16, weight="bold")
plt.show()

# Relación entre modelo & precio --------------------------- 

mod_cnt = datos['modelo'].value_counts(sort=False).sort_values(ascending=True)
mod_cnt_bar = mod_cnt.plot(kind='barh', y="modelo", 
                           legend=False, figsize=(8, 8))
mod_cnt_bar.set_title("# Publicaciones por Modelo",
                      fontsize=16, weight="bold")
mod_cnt_bar.set_xlabel("# publicaciones")
plt.show()

# Busco los promedios
precio_mod = datos.pivot_table(index="modelo",
                          values=["precio"],
                          aggfunc='mean')
precio_mod.head()

# Los grafico

precio_mod.sort_values("precio", ascending=True, inplace=True)
precio_mod_bar = precio_mod.plot(kind="barh", y="precio", figsize=(8, 8), legend=False)

precio_mod_bar.set_xlabel("Precio promedio")
precio_mod_bar.set_title("Precio promedio por localidad",
                  fontsize=16, weight="bold")
plt.show()