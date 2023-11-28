# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:11:45 2023

@author: Javi
"""


# =============================================================================
# ##~ 5. Decission Tree Ejercicio IRIS dataset
# =============================================================================

from sklearn import tree
import pandas as pd
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from plotnine import *
from sklearn.model_selection import train_test_split

# Cargo los datos
flores = datasets.load_iris()
x = flores.data
y = flores.target
x=pd.DataFrame(x)
x.columns= flores.feature_names

# divido en train y test

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# decido el modelo
modelo = tree.DecisionTreeClassifier(criterion =  "gini",max_depth = 7,min_samples_split= 0.05,min_samples_leaf=0.01)

# entreno el modelo con el train
modelo.fit (x_train, y_train)

# veo y grafico las vbles mas imp del modelo
modelo.feature_importances_

def create_df():
    data = {'nombres': x.columns, 'important': modelo.feature_importances_}
    df = pd.DataFrame(data)
    return df
variables_importantes = create_df()
ggplot(aes(x ="nombres",y="important",fill="important"),variables_importantes)+geom_bar(stat ="identity",position ="stack")

# hago predicciones para el test y comparo con la realidad para ver si el modelo es bueno
predictions= modelo.predict(x_test)
modelo.score (x_test,y_test)

confusion_matrix(y_test,predictions)

# creaccion del arbol

plt.figure(figsize=(15, 10))
plot_tree(modelo, filled=True, feature_names=features, rounded=True, fontsize=10)
plt.show()



# =============================================================================
# ##~ 6. Decission Tree Ejercicio IRIS dataset con grid search CV
# =============================================================================
from sklearn import tree
import pandas as pd
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from plotnine import *
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz

# Cargo los datos
flores = datasets.load_iris()
x = flores.data
y = flores.target
x=pd.DataFrame(x)
x.columns= flores.feature_names

# divido en train y test

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# decido el modelo
param_grid = {"criterion" :["gini","entropy"],"max_depth" : [None,7],"min_samples_split": [2,0.05],"min_samples_leaf":[1,0.01]}
modelo = GridSearchCV(estimator = DecisionTreeClassifier(), param_grid = param_grid)


# entreno el modelo con el train
modelo.fit (x_train, y_train)

modelofinal = modelo.best_estimator_

# veo y grafico las vbles mas imp del modelo
modelofinal.feature_importances_

def create_df():
    data = {'nombres': x.columns, 'important': modelofinal.feature_importances_}
    df = pd.DataFrame(data)
    return df
variables_importantes = create_df()
ggplot(aes(x ="nombres",y="important",fill="important"),variables_importantes)+geom_bar(stat ="identity",position ="stack")

# hago predicciones para el test y comparo con la realidad para ver si el modelo es bueno
predictions= modelofinal.predict(x_test)
modelofinal.score (x_test,y_test)

confusion_matrix(y_test,predictions)


""" vemos que  en mi caso el mejor estimator es criterion= entropy
y max_depth = 7,min_samples_leaf=0.01,
                       min_samples_split=0.05"""  
"""volvemos a hacer el DTC solo con estos parametros y ya podemos ver
el grafico con las variables mas importantes y con el arbol"""

from sklearn import tree
model= tree.DecisionTreeClassifier(max_depth=7, criterion='entropy',min_samples_leaf=0.01,
                       min_samples_split=0.05)
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
# ## 7. Ramdon Forest Ejercicio
# =============================================================================

import pandas as pd
from plotnine import *
from plotnine.data import diamonds
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier

y = diamonds.loc[:,["cut"]]
x = diamonds.loc[:,~ diamonds.columns.isin (["cut"])]
 
# Convertir variables categóricas a numéricas
label_encoders = {}
for column in ["color", "clarity"]:
    le = preprocessing.LabelEncoder()
    le.fit(x[column].astype(str))
    x[column] = le.transform(x[column].astype(str))
    label_encoders[column] = le


# Dividir los datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# Crear y entrenar el modelo de clasificación RandomForest
modelo = RandomForestClassifier(n_estimators=10, min_samples_leaf=1, min_samples_split=2, criterion="gini", class_weight="balanced")
modelo.fit(x_train, y_train)

# Obtener la importancia de las características
variables_importantes = pd.DataFrame({'nombres': x.columns, 'important': modelo.feature_importances_})

# Visualizar la importancia de las características usando ggplot
(ggplot(variables_importantes, aes(x="nombres", y="important", fill="important"))
 + geom_bar(stat="identity", position="stack")
)

# Realizar predicciones y evaluar el rendimiento del modelo
predictions = modelo.predict(x_test)
accuracy = modelo.score(x_test, y_test)
conf_matrix = confusion_matrix(y_test, predictions)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(conf_matrix)


# =============================================================================
# ## Xgboost ejemplo
# =============================================================================

#conda install c conda forge xgboost 
#conda install c anaconda py xgboost
#pip install xgboost

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn import preprocessing
from plotnine import *
from sklearn.metrics import confusion_matrix

# Cargamos datos
pokemon = pd.read_excel("C:/Users/Javi/Desktop/INMUNE/CURSO IMMUNE 3AÑO/Datos/pokemon.xlsx")

# Cambio de nombre las columnas Type
pokemon.rename(columns={"Type 1": "Type1", "Type 2": "Type2"}, inplace=True)

# Convertimos variables factor a numérico
label_encoders = {}
for column in ["Type1", "Type2"]:
    le = preprocessing.LabelEncoder()
    le.fit(pokemon[column].astype(str))
    pokemon[f"{column}_numerico"] = le.transform(pokemon[column].astype(str))
    label_encoders[column] = le

# Dividimos en variable a predecir (y) y variables predictoras (x)
y = pokemon["Legendary"]
x = pokemon.drop(['Legendary', "Name", "Type2", "Type1", "#"], axis=1)

# Dividimos en train (80%) y test (20%)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

booster_types = ["gblinear", "dart", "gbtree"]

for booster_type in booster_types:
    model = XGBClassifier(booster=booster_type)
    model.fit(x_train, y_train)
    
    # Obtener la importancia de las características
    variables_importantes = pd.DataFrame({'nombres': x_train.columns, 'important': model.feature_importances_})
    
    # Visualizar la importancia de las características usando ggplot
    plot = (ggplot(aes(x="nombres", y="important", fill="important"),
                   variables_importantes.sort_values("important", ascending=False).head(20))
            + geom_bar(stat="identity", position="stack") + coord_flip())
    
    # Mostrar información relevante
    print(plot)
    print(variables_importantes.sort_values("important", ascending=False).head(20))
    print(f"Booster Type: {booster_type}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, model.predict(x_test))}")
    print(f"Accuracy: {model.score(x_test, y_test)}")
