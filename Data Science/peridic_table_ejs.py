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

if __name__ == "__main__":
    data = pd.read_csv("Datasets\Periodic Table of Elements.csv")
    main()