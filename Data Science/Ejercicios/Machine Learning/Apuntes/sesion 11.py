# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:32:51 2023

@author: Javi
"""


# =============================================================================
# ##~ Cargamos librerias
# =============================================================================



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



# =============================================================================
# ~ Ejercicio pokemon!!
# =============================================================================

from sklearn.neighbors import KNeighborsClassifier
import sklearn.metrics as sm
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split


# cargamos datos
pokemon = pd.read_excel("C:/Users/Javi/Desktop/INMUNE/CURSO IMMUNE 3AÑO/Datos/pokemon_Pandas.xlsx")
pokemon.rename(columns = {"Type 1":"Type1", "Type 2": "Type2"},inplace=True)

## Convertimos variables factor a numerico
conversortype1 = preprocessing.LabelEncoder()
conversortype1.fit(pokemon.Type1.astype(str))
pokemon["type1numerico"] = conversortype1.transform(pokemon.Type1.astype(str)) 

conversortype2 = preprocessing.LabelEncoder()
conversortype2.fit(pokemon.Type2.astype(str))
pokemon["type2numerico"] = conversortype2.transform(pokemon.Type2.astype(str)) 

# dividimos en variable a predecir (y) y variables predictoras (x)
y = pokemon.loc[:,["Legendary"]]
x = pokemon.loc[:,~ pokemon.columns.isin (['Legendary',"Name","Type2","Type1","#"])]
x.fillna(value=x.mean(), inplace=True)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

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





