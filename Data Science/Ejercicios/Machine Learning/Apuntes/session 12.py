# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:27:20 2023

@author: Javi
"""
# =============================================================================
# ##~~SVM
# =============================================================================

#1.Importamos librerías
from sklearn import datasets
import sklearn.metrics as sm
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#Cargamos data set


flores = datasets.load_iris()

x= flores.data
y= flores.target

x_flores= pd.DataFrame(x)
y_flores= pd.DataFrame(y)

x_flores.columns=["PL","PW","SL","SW"]

#Dividir el data set en train 80% y el test 20%
x_train, x_test, y_train, y_test = train_test_split(x_flores, y_flores, test_size=0.20)

# entrenamos el modelo con el train (PARAMETRO KERNEL = LINEAR)
model= SVC(kernel = "poly")
model.fit(x_train,y_train)

#Vemos como de bueno es el modelo
model.score(x_test,y_test)
predictions = model.predict(x_test)
confusion_matrix(y_test,predictions)

# =============================================================================
# ##~ Pram grid
# =============================================================================

#1.Importamos librerías
from sklearn import datasets
import sklearn.metrics as sm
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC


#Cargamos data set
flores = datasets.load_iris()

x= flores.data
y= flores.target

x_flores= pd.DataFrame(x)
y_flores= pd.DataFrame(y)

x_flores.columns=["PL","PW","SL","SW"]

#Dividir el data set en train 80% y el test 20%
x_train, x_test, y_train, y_test = train_test_split(x_flores, y_flores, test_size=0.20)

# entrenamos el modelo con el train (PARAMETRO KERNEL = LINEAR)
param_grid = {'C': [1000, 5000], 'gamma': [0.0001, 0.005, 0.1]}
model = GridSearchCV(estimator = SVC(kernel='rbf'), param_grid = param_grid, cv = 3)
model = model.fit(x_train, y_train)

# ver el mejor estimator, mejor parameters, y mejor score
best_estimator = model.best_estimator_
best_params = model.best_params_
best_score = model.best_score_

# ver resultados
print("mejor estimador:\n", best_estimator)
print("\n mejor parametro:\n", best_params)
print("\n mejor puntuacion:\n", best_score)

# Additional evaluation metrics
y_pred = model.predict(x_test)

# Confusion matrix 
conf_matrix = confusion_matrix(y_test, y_pred)


# =============================================================================
# ##~ Ejercicio 3 SVM
# =============================================================================


from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow, show    

caras = datasets.fetch_lfw_people(min_faces_per_person=70)
X = caras.data
y = caras.target
y_names = caras.target_names

X_caras = pd.DataFrame(X)
y_caras = pd.DataFrame(y)

import time
for i in range(0,50,1):
    aux = X[i].reshape((62,47))
    plt.imshow(aux)
    show()
    time.sleep(0.2)


# Dividimos el train y test en 80 y 20
X_train, X_test, y_train, y_test = train_test_split(X_caras, y_caras, test_size=0.20, random_state=42)

# DEfinimos los parametros
param_grid = {'C': [1000, 5000], 'gamma': [0.0001, 0.005, 0.1]}

# creamos el modelo svc y grid search CV
model = GridSearchCV(estimator=SVC(kernel='linear'), param_grid=param_grid, cv=3)
model.fit(X_train, y_train)

# acceso al mejor estimador, parametro y score
best_estimator = model.best_estimator_
best_params = model.best_params_
best_score = model.best_score_

# vemos resultados
print("mejor Estimator:\n", best_estimator)
print("\nmejor Parameters:\n", best_params)
print("\nmejor Score:\n", best_score)


# =============================================================================
# ##~ Decision TREE
# =============================================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Cargar el conjunto de datos de Pokémon (asegúrate de tener el archivo .csv)
pokemon_data = pd.read_excel('C:/Users/Javi/Desktop/INMUNE/CURSO IMMUNE 3AÑO/Datos/pokemon.xlsx')
pokemon_data.columns
# Seleccionar las características (variables independientes) y la variable objetivo (clase)
features = ['HP', 'Attack', 'Defense', 'Sp. Atk',
       'Sp. Def', 'Speed']
target = ['Legendary']

x = pokemon_data[features]
y = pokemon_data[target]

# Dividir el conjunto de datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn import tree
model= tree.DecisionTreeClassifier(max_depth=3)
model.fit(x_train,y_train)
model.feature_importances_


def create_df():
    data={"nombres":x.columns,"Important":model.feature_importances_}
    df= pd.DataFrame(data)
    return df

variables_importantes= create_df()

from plotnine import * 
ggplot(aes(x="nombres",y="Important",fill="Important"),variables_importantes)\
    +geom_bar(stat="identity",position="stack")+coord_flip()



plt.figure(figsize=(15, 10))
plot_tree(model, filled=True, feature_names=features, class_names=['Not Legendary', 'Legendary'], rounded=True, fontsize=10)
plt.show()





# =============================================================================
# ##~ Decision TREE
# =============================================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Cargar el conjunto de datos de Pokémon (asegúrate de tener el archivo .csv)
pokemon_data = pd.read_excel('C:/Users/Javi/Desktop/INMUNE/CURSO IMMUNE 3AÑO/Datos/pokemon.xlsx')
pokemon_data.columns
# Seleccionar las características (variables independientes) y la variable objetivo (clase)
features = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
target = ['Legendary']

x = pokemon_data[features]
y = pokemon_data[target]

# Dividir el conjunto de datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


#Entrenamos modelos con el train
param_grid = {"criterion" :["gini","entropy"],"max_depth" :[ 4,3]}
model = GridSearchCV(estimator = DecisionTreeClassifier(), param_grid = param_grid, cv = 3)
model = model.fit(x_train,y_train)

#Vemos cual ha sido el mejor modelo
model.best_estimator_
model.best_params_
model.best_score_

#Vemos resultados 
res = model.cv_results_

#Predecimos con el test y vemos como funciona
predictions = model.best_estimator_.predict(x_test)

#Sacamos el score
model.best_estimator_.score(x_test, y_test)
confusion_matrix(y_test,predictions)

""" vemos que  en mi caso el mejor estimator es criterion= entropy
y max_depth = 3"""  
"""volvemos a hacer el DTC solo con estos parametros y ya podemos ver
elmgrafico con las variables mas importantes y con el arbol"""

from sklearn import tree
model= tree.DecisionTreeClassifier(max_depth=3, criterion='entropy')
model.fit(x_train,y_train)
model.feature_importances_


def create_df():
    data={"nombres":x.columns,"Important":model.feature_importances_}
    df= pd.DataFrame(data)
    return df

variables_importantes= create_df()

from plotnine import * 
ggplot(aes(x="nombres",y="Important",fill="Important"),variables_importantes)\
    +geom_bar(stat="identity",position="stack")+coord_flip()


plt.figure(figsize=(15, 10))
plot_tree(model, filled=True, feature_names=features, class_names=['Not Legendary', 'Legendary'], rounded=True, fontsize=10)
plt.show()













