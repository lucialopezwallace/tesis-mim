 
# Archivo donde graficaremos nuestros datos
############################################################# 

# Importo las librerias que utilizaremos
import matplotlib.pyplot as plt
import seaborn as sns

# Levantamos los datos procesados

datos = pd.read_csv('data_publications_process.csv', sep=";")

# Observamos nuestro dataset
datos.shape
# (31869, 10)

# Variable precio ---------------------
plt.title('Precio')
plt.xlabel("precio ('000)")
plt.hist(datos['precio']/1000, bins = 70)
plt.show() 

# Cómo ver outliers
sns.boxplot(x=datos['precio'])
plt.show() 

# Otra manera de ver outliers para Precio & Año
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(datos['year'], datos['precio'])
ax.set_xlabel('Year')
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
plt.xlabel("Año")
plt.hist(datos['year'], bins = 70)
plt.show()

# Grafico los outliers
sns.boxplot(x=datos['year'])
plt.show()