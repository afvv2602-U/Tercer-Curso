# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:24:52 2023

@author: Adri
"""

# =============================================================================
# ##~ Decima Clase
# =============================================================================

# =============================================================================
# ##~K-Means  (CLUSTERIZACION)
# =============================================================================

#%%
#Carga de librerías.
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

#carga del data set:
   
pokemon= pd.read_excel("C:/Users/Adri/Documents/Tercer-Curso/Data Science/Ejercicios/Machine Learning/pokemon.xlsx")
pokemon.drop("#",axis=1,inplace=True)

#Patrones de agrupamiento
datoskmeans = pokemon.loc[:,["Attack","Defense"]]

#elimiar valores nulos
datoskmeans =datoskmeans.dropna()
datoskmeans =datoskmeans.reset_index(drop=True)

#normlizar los datos


min_max_scaler= preprocessing.MinMaxScaler()
datos_escalados= min_max_scaler.fit_transform(datoskmeans)

datos_escalados = pd.DataFrame(datos_escalados)
datos_escalados= datos_escalados.rename(columns={0:"Attack",1:"Defense"})

#Representacion grafica de los datos

x= datos_escalados["Attack"].values
y= datos_escalados["Defense"].values

plt.xlabel("Attack")
plt.ylabel("Defense")
plt.title("Attack vs Defense")
plt.plot(x,y, "o", markersize=1)



#Curva elbow para determinar valor óptimo de k.
from plotnine import *
elbow_values = []
for i in range(1,11,1):
    km = KMeans(n_clusters=i)
    km.fit(datos_escalados)
    elbow_values.append(km.inertia_)
elbow = pd.DataFrame({"clusters":range(1,11,1), "elbow" : elbow_values})    
   
ggplot(aes(x = "clusters", y ="elbow"),elbow)\
    +geom_line()+geom_point()\
        +ggtitle("Elbow graph")

#vamos a aplicar el algortimo KMEANS
kmeans = KMeans(n_clusters=5).fit(datos_escalados)
centroids =kmeans.cluster_centers_
print(centroids)

#etiquetamos nuestro dataframe con los clusters
cluster= kmeans.predict(datos_escalados)
pokemon["cluster"] = cluster


#Representacion grafica de los clusters

colores=['red','green','blue','yellow','fuchsia']
asignar=[]
for row in cluster:
     asignar.append(colores[row])
plt.scatter(x, y, c=asignar, s=1)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*',
            c='black', s=20) # Marco centroides.
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Pokemon Attack Defense k-means clustering')
plt.show()

#representacion en excel
centroids = pd.DataFrame(centroids)
centroids = pokemon.groupby('cluster')[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Generation']].mean()
centroids.to_excel("C:/Users/Adri/Documents/Tercer-Curso/Data Science/Ejercicios/Machine Learning/pokemoncluster.xlsx")
pokemon.cluster.value_counts()


# Crear un writer de pandas con xlsxwriter como engine
writer = pd.ExcelWriter('C:/Users/Adri/Documents/Tercer-Curso/Data Science/Ejercicios/Machine Learning/pokemoncluster_colors.xlsx', engine='xlsxwriter')
centroids.to_excel(writer, sheet_name='Sheet1')

# Acceder al objeto workbook y worksheet de xlsxwriter
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Definir el formato para las celdas
cell_format = workbook.add_format({'bold': True, 'font_color': 'black'})

# Aplicar el formato condicional
# Ajustar el rango según la cantidad de datos
worksheet.conditional_format('B2:H140', {'type': '3_color_scale',
                                         'min_color': "#63be7b", # Verde
                                         'mid_color': "#fbea84", # Amarillo
                                         'max_color': "#f8696b"}) # Rojo

# Guardar el archivo
writer._save()

#%% Ejercicio samsung

import pandas as pd
from sklearn import preprocessing 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Carga del dataframe.
samsung = pd.read_csv("C:/Users/Javi/Desktop/INMUNE/CURSO IMMUNE 3AÑO/Datos/Samsung.csv")
datoskmeans = samsung.loc[:,["Close","Volume"]]


datoskmeans = datoskmeans.dropna()
datoskmeans= datoskmeans.reset_index(drop=True)




#%% Se normalizan los datos con MinMax()
min_max_scaler = preprocessing.MinMaxScaler() 
datos_escalados = min_max_scaler.fit_transform(datoskmeans)
datos_escalados = pd.DataFrame(datos_escalados) # Hay que convertir a DF el resultado.
datos_escalados = datos_escalados.rename(columns = {0: 'Close', 1: 'Volume'})



x = datos_escalados['Close'].values
y = datos_escalados['Volume'].values
plt.xlabel('Close price')
plt.ylabel('Volume')
plt.title('Samsung stocks CLOSE vs. VOLUME')
plt.plot(x,y,'o',markersize=1)

from plotnine import * 
elbow_values = []
for i in range(1,11,1):
    km = KMeans(n_clusters=i)
    km.fit(datos_escalados)
    elbow_values.append(km.inertia_)
elbow = pd.DataFrame({"clusters":range(1,11,1), "elbow" : elbow_values})    
    
ggplot(aes(x = "clusters", y ="elbow"),elbow)+geom_line()+geom_point()+ggtitle("Elbow graph")

#%% Aplicación de k-means con k = 5.
kmeans = KMeans(n_clusters=4).fit(datos_escalados)
centroids = kmeans.cluster_centers_
print(centroids)


#%% Etiquetamos nuestro dataframe.
cluster = kmeans.predict(datos_escalados)
samsung['cluster'] = cluster

colores=['red','green','blue','yellow']
asignar=[]
for row in cluster:
     asignar.append(colores[row])
plt.scatter(x, y, c=asignar, s=1)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='black', s=20) # Marco centroides.
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.title('Pokemon Attack Defense k-means clustering')
plt.show()

import seaborn as sns
correlaciones = samsung.corr()
#pokemon = pokemon.drop("cluster",axis=1)
sns.clustermap(correlaciones,method="complete",cmap="RdBu",annot=True,annot_kws={"size":15},vmin=-1,vmax=1,figsize=(15,12))


centroides = samsung.groupby(by=("cluster"),as_index=False).mean()
centroides.to_excel("Samusng2.xlsx")
samsung.cluster.value_counts()

#%% Clase 2 

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

# Cargar el dataset
digits = datasets.load_digits()
X = digits.data
y = digits.target

# Dividir el conjunto de datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Ejecutar el modelo
model = KNeighborsClassifier(n_neighbors=5, weights="uniform")
model.fit(x_train, y_train)

# Realizar predicciones en el conjunto de prueba
predictions = model.predict(x_test)

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(conf_matrix)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Mostrar algunos ejemplos de imágenes y predicciones
fig, axes = plt.subplots(1, 5, figsize=(12, 3))
for i in range(5):
    random_index = np.random.randint(0, len(x_test))
    axes[i].imshow(x_test[random_index].reshape(8, 8), cmap='gray')
    axes[i].set_title(f"Predicted: {predictions[random_index]}, Actual: {y_test[random_index]}")
    axes[i].axis('off')

plt.show()