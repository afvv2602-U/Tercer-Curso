# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:26:29 2023

@author: Adri
"""

#%%  Imports
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


#%% Data Clean and KMean

data = pd.read_excel("C:/Users/Adri/Documents/Tercer-Curso/Data Science/Ejercicios/Machine Learning/Proyecto Final/HR Data.xlsx")

datos_kmeans = data.loc[:,['CF_age band','Monthly Income','Education']]

# Convertir datos categóricos en numéricos
age = LabelEncoder()
education = LabelEncoder()
datos_kmeans['CF_age band'] = age.fit_transform(datos_kmeans['CF_age band'])
datos_kmeans['Education'] = education.fit_transform(datos_kmeans['Education'])

# Normalización de los datos
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(datos_kmeans)

# Mostramos los primeros registros del conjunto de datos normalizado
pd.DataFrame(normalized_data, columns=datos_kmeans.columns).head()


#%% Metodo del codo

distortions = []
K = range(1, 10)
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(normalized_data)
    distortions.append(kmeanModel.inertia_)

# Graficando el método del codo
plt.figure(figsize=(12, 6))
plt.plot(K, distortions, 'bx-')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Distorsión')
plt.title('Método del Codo para determinar el número óptimo de clusters')
plt.show()


#%% Silueta
from sklearn.metrics import silhouette_score

silhouette_scores = []
K = range(2, 10)  # Empezamos desde 2 porque no se puede calcular la silueta para k=1
for k in K:
    kmeanModel = KMeans(n_clusters=k)
    cluster_labels = kmeanModel.fit_predict(normalized_data)
    silhouette_scores.append(silhouette_score(normalized_data, cluster_labels))

# Graficando el análisis de silueta
plt.figure(figsize=(12, 6))
plt.plot(K, silhouette_scores, 'bo-')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Puntaje de Silueta')
plt.title('Análisis de Silueta para determinar el número óptimo de clusters')
plt.show()


#%% Creacion de los clusters

for k in range(3,6):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(normalized_data)
    # Creando el scatter plot de los clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(normalized_data[:, 1], normalized_data[:, 2], c=labels, cmap='viridis', marker='o')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 1], centers[:, 2], c='red', s=200, alpha=0.75, marker='x')
    plt.title(f'Visualización de los clusters para k={k}')
    plt.xlabel('Ingreso Mensual Normalizado')
    plt.ylabel('Educación Normalizada')
    plt.show()

