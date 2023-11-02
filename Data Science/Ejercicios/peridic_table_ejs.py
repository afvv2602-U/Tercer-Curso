import pandas as pd

def main():
    # eje_10()
    # eje_11()
    # eje_12()
    # eje_13()
    # eje_14()
    # eje_15()
    # eje_16()
    # eje_17()
    # eje_18()
    # eje_19()
    # eje_20()
    # eje_21()
    # eje_22()
    # eje_23()
    # eje_24()
    # eje_25()
    # eje_26()
    eje_27()
    pass

def eje_10():
    print(data.dtypes)
    print(data.describe())

def eje_11():
    x = data.head(10)
    print(x)

def eje_12():
    x = data.iloc[4:6:,-4:]
    print(x)
  
def eje_13():
    x = data.loc[:,['Year','Symbol']]
    print(x)
    pass

def eje_14():
    x = data.iloc[2:4,:].loc[:,['Discoverer','SpecificHeat']]
    print(x)
    pass

def eje_15():
    data.drop('Electronegativity',axis=1,inplace=True)
    print(data.describe)

def eje_16():
    x = data.shape
    print(x[1])

def eje_17():
    x = data.loc[:,'AtomicMass'].sort_values(ascending=0).head(1)
    print(x)

def eje_18():
    x = data.loc[:,['Year','NumberofValence']].sort_values(by='NumberofValence',ascending=0)
    print(x)

def eje_19(): 
    x = data.loc[:,'NumberofNeutrons'].sum()
    print(x)  

def eje_20():
    x = data.groupby('Type')['Phase'].count() 
    print(x)

def eje_21():
    x = data.loc[data.Year == 1898].loc[:,['Type','BoilingPoint']].groupby('Type').sum()
    print(x)

def eje_22():
    x = data.loc[:,['MeltingPoint','Phase']].groupby('Phase').mean()
    print(x)
  
def eje_23():
    x = data.loc[:,['Discoverer','Element']].groupby(['Discoverer'],as_index=False,).count().sort_values(by='Element',ascending=0).head(1)
    print(x)

def eje_24():
    x = data.loc[data.Metal == 'yes'].loc[:,['Density','Element']].sort_values(by='Density',ascending=1).head(1)
    print(x)

def eje_25():
    print(data.columns)
    x = data.loc[:,['Symbol','NumberofElectrons','NumberofNeutrons']]\
        .loc[(data.NumberofElectrons.between(50,100))&(data.NumberofNeutrons.between(60,100))]
    print(x)

def eje_26():
    x = data.loc[:,['Element','NumberofProtons']].loc[data['NumberofProtons'] % 2 == 0]
    print(x)

def eje_27():
    x = data.loc[:,['Element','NumberofProtons','Density']].loc[data['NumberofProtons'] % 2 == 0].sort_values(by='Density',ascending=0).head(1)
    print(x)

if __name__ == "__main__":
    data = pd.read_csv("Datasets\Periodic Table of Elements.csv")
    main()