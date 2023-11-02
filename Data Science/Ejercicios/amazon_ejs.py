import pandas as pd

def main():
    # eje_28()
    # eje_29()
    # eje_30()
    # eje_31()
    # eje_32()
    # eje_33()
    # eje_34()
    # eje_35()
    pass

def eje_28():
    x = data.loc[:,['HoursUntilDelivery','OrderID']].sort_values(by='HoursUntilDelivery',ascending=0).head(10)
    print(x)

def eje_29():
    x = data.loc[:,['CustomerName','Bill']].groupby(by='CustomerName',as_index=False).sum().sort_values(by='Bill',ascending=0).head(4)
    print(x)

def eje_30():
    x = data.loc[:,['State','Bill']].groupby(by='State',as_index=False).sum().sort_values(by='Bill',ascending=0).head(1)
    print(x)

def eje_31():
    x = data.loc[:,['State','OrderYear','Bill']].groupby(by=['State','OrderYear'],as_index=False).sum()
    print(x)

def eje_32():
    x = data.loc[:,['State','OrderYear','Bill']].groupby(by=['State','OrderYear'],as_index=False).sum().sort_values(by=['Bill','OrderYear'],ascending=[0,0]).head(1)
    print(x)

def eje_33():
    x = data.loc[(data.City == 'New York City')|(data.City == 'Los Angeles'),:].loc[data.HoursUntilDelivery > 200,:]
    x = data.loc[data.City.isin(['New York City','Los Angeles'])].loc[data['HoursUntilDelivery'] > 200] # Otra forma
    print(x)

def eje_34():
    data['logica'] = data.HoursUntilDelivery > 500
    print(data)

def eje_35():
    x = data.loc[(data.State == 'Texas')&(data.Bill < 300)&(data.HoursUntilDelivery < 200)].groupby(by=['City','Year']).sum()\
    .sort_values(by='Bill',ascending=0).drop_duplicates(subset=['OrderYear'],keep='first')
    print(x)
    


if __name__ == "__main__":
    data = pd.read_excel("Datasets\Exam_Amazon_Shipments.xlsx")
    main()