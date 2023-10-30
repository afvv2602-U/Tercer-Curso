import pandas as pd

def main():
    eje_1()
    eje_2()
    eje_3()
    eje_4()
    eje_5()
    eje_6()
    eje_7()
    eje_8()
    eje_9()

def eje_1():
    data = pd.read_excel("Datasets\pokemon_Pandas.xlsx")
    Sp = data.Sp_Atk.isnull().sum()
    Hp = data.HP.isnull().sum()

    print(f'Sp null {Sp}, Hp null {Hp}')

def eje_2():
    print(data.isnull())

def eje_3():
    print(data.columns)
    data["Type 2"].fillna(value="Sin informacion",inplace=True)
    c = data.loc[:,"Type 2"]
    print(c)

def eje_4():
    print(data.columns)
    data.Defense.fillna(value=data.Defense.mean(),inplace=True)
    data.Sp_Def.fillna(value=data.Sp_Def.max(),inplace=True)
    c = data.loc[:,["Defense","Sp_Def"] ]
    print(c)

def eje_5():
    data = pd.read_excel("Datasets\pokemon_Pandas.xlsx")
    data['HP'] = 0
    c = data.loc[:,"HP"]
    print(c)

def eje_6():
    x = data.loc[data.Speed>90,:]
    print(x)
 
def eje_7():
    fire_pokemons = data.loc[(data["Type 1"] == 'Fire'),:]
    top_fire_pokemons = fire_pokemons.nlargest(5,'Attack')
    print(top_fire_pokemons)

def eje_8():
    first_generation = (data['Generation'] == 1).sum()
    second_generation = (data['Generation'] == 2).sum()
    print(f'First generation count {first_generation}, Second generation count {second_generation}')

def eje_9():
    data.fillna(value=data.mean(),inplace=True)
    print(data)

if __name__ == "__main__":
    data = pd.read_excel("Datasets\pokemon_Pandas.xlsx")
    main()