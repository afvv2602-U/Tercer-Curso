import pandas as pd

def main():
    print(data.columns)
    # eje_36()
    # eje_37()
    # eje_38()
    # eje_39()
    # eje_40()
    # eje_41()
    # eje_42()
    # eje_43()
    # eje_44()
    # eje_45()
    # eje_46()
    pass

def eje_36():
    data['bill_results'] = pd.cut(data.bill,bins=[0,300,1000,data.bill.max()],labels=['Barato','Mediano','Caro'])
    print(data.bill_results)

def eje_37():
    bill_orders_corr = data.bill.corr(data.orders) 
    tip_bill_corr = data.bill.corr(data.tip) 
    print(f'Correlacion entre bill y orders {bill_orders_corr}')
    print(f'Correlacion entre bill y tips {tip_bill_corr}')

def eje_38():
    x = pd.crosstab(data.service,data.supervisor)
    print(x)

def eje_39():
    data.drop(['gender','orders'],inplace=True,axis=1)
    print(data.describe)

def eje_40():
    count = data.supervisor.nunique()
    x = data.supervisor.unique()
    print(f'Count of values uniques in supervisor {count} Values of that unique values {x}')

def eje_41():
    x = data.nationality.unique()
    y = data.nationality.value_counts().head(1)
    print(f'Values of variable nationality {x}, value that appear the most {y}')

def eje_42():
    x = data.drop_duplicates(subset=['items'],keep='first')
    print(x)

def eje_43():
    x = data.loc[(data.gender == 'F')&(data.tip.between(25,30))].sort_values(by='tip',ascending=0).head(1)
    x = data.loc[(data.gender == 'F')&(data.tip.between(25,30))].loc[:,['supervisor','tip']]\
    .groupby(by=['survisor'],as_index=False).sum().sort_values(by=['tip'],ascending=0).head(1)
    print(x)

def eje_44():
    x = data.loc[(data.gender == 'F')&(data.bill > 500)&(data.service.isin(['excellent','brilliant']))&(data.nationality != 'German')]
    print(x)

def eje_45():
    x = data.loc[(data.week_day.between(6,7))].loc[:,['week_day','orders']].groupby(['week_day'],as_index=False).sum()
    print(x)

def eje_46():
    x = data.loc[:,['day','tip']].groupby(by='day',as_index=False).sum().sort_values(by=['tip'],ascending=0).head(3)
    print(x)

if __name__ == "__main__":
    data = pd.read_excel("Datasets\\bar.xlsx")
    main()