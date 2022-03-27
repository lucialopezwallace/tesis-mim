 
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

# Variable precio 
plt.title('Precio')
plt.xlabel("precio ('000)")
plt.hist(datos['precio']/1000, bins = 70)
plt.show() 

# Cómo ver outliers
sns.boxplot(x=datos['precio'])
sns.show()

# Otra manera de ver outliers
fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(datos['precio'], datos['year'])
ax.set_xlabel('Precio')
ax.set_ylabel('KM')
plt.show()

# Sacamos los outliers
from scipy import stats
z = np.abs(stats.zscore(datos['precio']))
print(z)

threshold = 3
print(np.where(z > 3))

datos_sin_o = datos[(z < 3)]
datos_sin_o.shape
datos_sin_o.info()
# (35435, 9)
plt.title('Precio')
plt.xlabel("precio ('000)")
plt.hist(datos_sin_o['precio']/1000, bins = 70)

# Variable KMT --------------------------- 
plt.title('Kilometros')
plt.xlabel("KM")
plt.hist(datos['km'], bins = 70)

# Grafico los outliers
sns.boxplot(x=datos['km'])

z = np.abs(stats.zscore(datos['km']))
print(z)

threshold = 1
print(np.where(z > 1))

def outlier_treatment(datacolumn):
    sorted(datacolumn)
    Q1,Q3 = np.percentile(datacolumn , [25,75])
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    return lower_range,upper_range

lowerbound,upperbound = outlier_treatment(datos.km)
print(lowerbound)
print(upperbound)
datos[(datos.km < lowerbound) | (datos.km > upperbound)]

# Variable Year --------------------------- 
plt.title('Años')
plt.xlabel("Año")
plt.hist(datos['year'], bins = 70)