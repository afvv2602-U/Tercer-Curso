import pandas as pd

def main():
    pass

def read():
    # Mostrar los nombres de las columnas
    cols = data.columns 
    # Nos da todo los datos del data set
    des = data.describe()

    dimesiones = data.shape # Dimensiones del dataset

    # Ver las 5 primera filas.
    x = data.head(5)

    # Podemos especificar cuantas filas queremos ver desde el final en esta caso 10
    z = data.tail(10)

    # Ver el tipo de dato
    types = data.dtypes

    # Crear una columna nueva al final
    data["logica"] = False

    # Filtrado y manipulacion de datos

    #.iloc para extraer por el indice numerico
    #.loc para extraer por nombre
                 #Fila    Columna
    c = data.loc[     :,["AtomicNumber","Element"] ] # Estamos sacando todas las filas de las columnas AtomicNumber y Element, creando una lista nueva
    c = data.iloc[0,:] # Cogemos todas las columnas de la fila 1
    c = data.iloc[:,5:8] # Cogemos desde la posicion 5 a la 7 con todas las filas
    c = data.iloc[2:6,:] # Cogemos de las filas 2 a 5 con todas las columnas
    # Sacamos el valor 1 y 2 de las filas y despues con loc filtramos las columnas necesarias de las columnas AtomicNumber y Element
    c = data.iloc[1:3,:].loc[:,["AtomicNumber","Element"]] 
    
    # Filtrar por condicionales
    x = data.loc[data.AtomicMass>280,:] # Sacamos todas las columnas de las filas que sean mayores de 280

    x = data.loc[(data.AtomicMass>280)&(data.Metal == 'yes'),:] # Unimos dos condicionales con el simbolo &

    # Renombrar columnas
    data.rename(columns={"AtomicNumber":"NumeroAtomico"},inplace=True) # inplace=True modifica el data si fuese false solo mostraria la operacion

# Duplicados
def duplicates():
    data.drop("Element",axis=1,inplace=True) # Borrar la columna Element axis=1 especificas que sean columnas axis=0 las filas

    c = data.dropna(axis=1) # Borramos las columnas NA (Not available)

    v = data.dropna(subset=["Type"],inplace=True) # Borramos las filas cuyos valores de Type sean nulos

    x = data.drop_duplicates(subset=["Discoverer"],keep="first") # Borramos las filas cuyo Dicoverer este duplicado y nos quedamos con el primero que aparezca 
    
# Valores NAN
def na_values():
    data.isnull().values.any() # Con este comando vemos si hay valores nulos en este Dataset

    x = data.isnull() # Devuelve el dataset entero en True o False, dependiendo True es que el valor es Null False tiene valor

    # Contar los valores nulos de un dataset por variables

    data.isnull().sum() # Te devuelve cuantos valores nulos hay por cada columna

    data.isnull().sum().sum() # Suma total de todos los valores nulos

    data.Metal.isnull() # Seleccionamos las filas de los valores nulos de la columna Metal

    data.columns[data.isnull.any()] # Nos devuelve todas las variables que tienen valores nulos
  
# Rellenar valores nulos
def fill_na():
    data.fillna(value=44444,inplace=True) # Rellenamos todos los valores NA con 444444 sean numericos o no

    data.Year.fillna(value=2023,inplace=True) # Rellenamos todos los valores NA de la variable Year con el valor 2023

    data.fillna(value=data.mean(),inplace=True) # Rellenamos todos los valores NA de todas las variables numericas usando la media de cada variable

    data["MeltingPoint"].fillna(value=data["MeltingPoint"].mean(),inplace=True) # Rellenamos todos los NA de la variables MeltingPoint con la media de la col
    data.MeltingPoint.fillna(value=data.MeltingPoint.mean(),inplace=True) # Otra forma de hacer lo mismo

    data.Metal.fillna("no info",inplace=True) # Actualizamos los NA de metal a no info

# Extraer datos
def extract_data():
    subset_string =  data.select_dtypes(include=[object]) # Dentro de los corchetes especificamos el tipo de dato que queremos
    subset_float = data.select_dtypes(include=[float]) # En esta caso float

    # Extraer valores entre dos numeros dentro de una variable
    atomicNumberBetween = data[data['AtomicNumber'].between(25,30)] # Saca todas las filas entre el valor 25 y 30 usando between

    # Extraer todas las filas que contengan un valor
    data.loc[data.Phase.str.contains('gas'),:] # Sacamos todas las filas donde aparece gas en la variables Phase

    # Extraer la primera letra de los valores de una variable
    data['letra'] = data['Discoverer'].astype(str).str[0] # Sacamos la primera letra de cada descubridor y creamos una columna nueva con esos valores

    # Extraer dos valores distintos de la misma variable (ISIN)
    data.loc[data.Phase.isin(['gas','solid']),:] # Sacamos todas las filas que contengan gas o solid en la variable Phase

    # Sacar la primera palabra de una columna entera
    data['nuevo'] = data.Discoverer.str.split().str.get(0) # Creamos una nueva columna con la primera palabra de la variable Discoverer

# Ordenar valores
def sort_values():
    cols = data.loc[:,['Year','AtomicNumber','Element']].sort_values(by='Year',ascending=1) # Ordenamos las filas por orden ascendente 1 o Descendente 0 en base a Year

# Estadisticas del dataframe
def stats():
    data.max() # Nos da los valores maximos de cada variables, En numeros el maximo en str los que tengan z
    data.min() # Nos da valores minimos
    data.mean() # Nos da la media
    data.sum() # Nos hace una suma de todos
    data.Phase.value_counts() # Nos enseña los valores de una variables y cuantas veces se repite
    data.count() # Nos cuenta los valores que hay en cada variable

    # Correlaciones
    data.AtomicMass.corr(data.AtomicRadius) # Cuanto mas se acerquen a 1 estan mas correlacionadas 0 No
    data.corrwith(data.AtomicMass) # Vemos la relacion de AtomicMass frente al resto de variables
    tabla_correlaciones = data.corr() # Creamos una tabla con todas las variables correlacionas

def group_by():
    # as_index = False es para que Phase no sea el index de los valores agrupados
    x = data.groupby(by=['Phase'],as_index=False).sum() # Agrupamos todas las variables sumadas, en phase 
    z = data.groupby(by=['Phase','AtomicMass'],as_index=False).mean()

    data.groupby('Phase')['Symbol'].count() 
    data.Phase.value_counts() # Lo mismo escrito distinto

    data.groupby('Phase').count()['gas']
    data.Phase.value_counts()['gas']

    # Agrupamos en Phase y Type, con la funcion agg Creamos tres columnas que cogen el MAX, MIN y MEAn de BoilingPoint
    # Y reseteamos el index para que sean numeros y no Phase \ la barra sirve para seguir la instruccion en otra linea
    x = data.loc[:,['BoilingPoint','Phase','Type']].groupby(by=['Phase','Type'])\
    .agg(MAX=('BoilingPoint','max'),MIN=('BoilingPoint','min'),MEAN=('BoilingPoint','mean'))\
    .reset_index()

# Reemplazar variables
def replace_values():

    # Reemplazar valores numericos
    data.Group.replace(to_replace= 1, value=100, inplace=True) # Cambiamos el valor 1 por el 100
    data.Group.replace(to_replace= (1,18), value=(100,1800), inplace=True) # Cambiamos el valor 1 por el 100 y el 18 por el 1800

    # Reemplazar tipo texto
    data.Phase.replace(to_replace=['gas'], value=['GASESSSSSS'],inplace=True) # Cambiamos Gas por GASESSSS
    data.Phase.replace(to_replace=['gas','solid'], value=['GASESSSSSS','solidoossss'],inplace=True)

def crosstab():

    # Es una tabla que muestra la relacion entre dos variables
    x = pd.crosstab(data.Phase,data.NumberOfShells) # Te hace un count de las variables y las veces que aparecen, pero usando dos variables
    data.NumberOfShells.value_counts() # Te hace un conteo de las veces que aparece cada variable

    # Porcentaje to total de toda la tabla
    x = pd.crosstab(data.Phase,data.NumberOfShells,normalize='all') # Porcentaje total de toda la tabla
    x = pd.crosstab(data.Phase,data.NumberOfShells,normalize='columns') # Porcentaje total por columnas 
    x = pd.crosstab(data.Phase,data.NumberOfShells,normalize='index') # Porcentaje total por filas

def other_commands():
    # Nos muestra una lista con todos los valores que hay en esa variable
    data.Type.unique()
    data.Phase.unique()

    # Nos muestra el numero total de datos que no son unicos dentro de esta variable
    data.Type.nunique()

    # pd.cut te permite crear una nueva columna en base a los valores de una variable
    data['letras'] = pd.cut(data.AtomicMass,bins=[0,100,200,300],labels=['Bajo','Medio','Alto'])
    data['letras'] = pd.cut(data.AtomicMass,bins=[data.AtomicMass.min(),data.AtomicMass.mean(),data.AtomicMass.mean()*2,data.AtomicMass.max()],
                            labels=['Bajo','Medio','Alto']) # Otro modo de hacerlo usando los valores de las variables

def transform_variables():

    data['Group'] = pd.to_numeric(data['Group'],downcast='float') # transformar de tipo Int a tipo Float
    data['Group'] = data.Group.astype(str) # transformar de tipo float a tipo string

   
    



if __name__ == "__main__":
    data = pd.read_csv("Datasets\Periodic Table of Elements.csv")
    main()