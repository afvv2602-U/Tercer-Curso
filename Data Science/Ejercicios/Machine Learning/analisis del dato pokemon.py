# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:48:48 2021
 
@author: Javi
""" 

import pandas as pd



#%%

def check(datos,nombreArchivo):
    o = datos.select_dtypes(include=[object])
    f = datos.select_dtypes(include=["datetime64"])
    n = datos.select_dtypes(include=["int64","float64"])

    print("Los siguientes dos numeros deberian coincidir")
    print("Vbles filtradas: ", o.shape[1] + f.shape[1]+ n.shape[1])
    print("Vbles totales: ", datos.shape[1])


    # VBLES FECHA:
    f1 = f.isnull().sum()
    f2 = f.min()
    f3 = f.max()
    f4 = f.nunique()

    f_sol = pd.concat([f1,f2,f3,f4],axis=1)
    f_sol.columns= ["empty_rows","min","max","unique_values"]

    # VBLES NUM:
    n1 = n.isnull().sum()
    n2 = n.mean()
    n3 = n.median()
    n4 = n.min()
    n5 = n.max()
    n6 = n.nunique()

    n_sol = pd.concat([n1,n2,n3,n4,n5,n6],axis=1)
    n_sol.columns= ["empty_rows","mean","median","min","max","unique_values"]
    
    # VBLES OBJECT:
    o1 = o.isnull().sum()
    o2 = o.apply(lambda x:x.value_counts().index[0] if (len(x.value_counts())>=1) else "")
    o3 = o.apply(lambda x:x.value_counts().iloc[0]  if (len(x.value_counts())>=1) else "")
    o4 = o.apply(lambda x:x.value_counts().index[1] if (len(x.value_counts())>=2) else "")
    o5 = o.apply(lambda x:x.value_counts().iloc[1]  if (len(x.value_counts())>=2) else "")
    o6 = o.apply(lambda x:x.value_counts().index[2] if (len(x.value_counts())>=3) else "")
    o7 = o.apply(lambda x:x.value_counts().iloc[2]  if (len(x.value_counts())>=3) else "")
    o8 = o.nunique()

    o_sol = pd.concat([o1,o2,o3,o4,o5,o6,o7,o8],axis=1)
    o_sol.columns= ["empty_rows","Factor1","CasesFactor1","Factor2","CasesFactor2","Factor3","CasesFactor3","unique_values"]


    # SAVING EVERYTHING IN ONE FILE
    #writer = pd.ExcelWriter(nombrearchivo)
    #o_sol.to_excel(writer,'VblesFactor')
    #n_sol.to_excel(writer,'VblesNumericas')
    #f_sol.to_excel(writer,'VblesFecha')
    #writer.save()

    # SAVING EVERYTHING IN ONE FILE WITH CONDITIONAL FORMAT
    writer = pd.ExcelWriter(nombreArchivo, engine='xlsxwriter')
    o_sol.to_excel(writer,'VblesFactor')
    n_sol.to_excel(writer,'VblesNumericas')
    f_sol.to_excel(writer,'VblesFecha')


    # Formatting Headers and Variable names
    workbook    = writer.book
    cell_format = workbook.add_format({'bold': True, 'font_color': '#ffffff', 'bg_color':"#1f497d"})

    # Formatting Factor
    worksheet = writer.sheets['VblesFactor']
    worksheet.conditional_format('A1:A140', {'type': 'no_blanks', 'format': cell_format})
    worksheet.conditional_format('A1:I1', {'type': 'no_blanks', 'format': cell_format})
    worksheet.conditional_format('B2:B140', {'type': '3_color_scale',
                                         'min_color': "#63be7b",
                                         'mid_color': "#fbea84",
                                         'max_color': "#f8696b"})  #
    worksheet.conditional_format('D2:D140', {'type': 'data_bar'})
    worksheet.conditional_format('F2:F140', {'type': 'data_bar'})
    worksheet.conditional_format('H2:H140', {'type': 'data_bar'})
    worksheet.conditional_format('I2:I140', {'type': '3_color_scale',  #
                                         'min_color': "#63be7b",
                                         'mid_color': "#fbea84",
                                         'max_color': "#f8696b"})  #
    
    # Formatting Numerics
    worksheet = writer.sheets['VblesNumericas']
    worksheet.conditional_format('A1:A140', {'type': 'no_blanks', 'format': cell_format})
    worksheet.conditional_format('A1:I1', {'type': 'no_blanks', 'format': cell_format})
    worksheet.conditional_format('B2:B140', {'type': '3_color_scale',
                                         'min_color': "#63be7b", #Verde
                                         'mid_color': "#fbea84", #Amarillo
                                         'max_color': "#f8696b"}) #Rojo
   
    worksheet.conditional_format('G2:G140', {'type': '3_color_scale'})  
    
    
    # Formatting Fechas
    worksheet = writer.sheets['VblesFecha']
    worksheet.conditional_format('A1:A140', {'type': 'no_blanks', 'format': cell_format})
    worksheet.conditional_format('A1:I1', {'type': 'no_blanks', 'format': cell_format})
    worksheet.conditional_format('B2:B140', {'type': '3_color_scale',
                                         'min_color': "#63be7b", #Verde
                                         'mid_color': "#fbea84", #Amarillo
                                         'max_color': "#f8696b"}) #Rojo
   
    worksheet.conditional_format('E2:E140', {'type': '3_color_scale'})  
    
    writer._save()
#%%
#CARGAMOS LOS DATOS
data = pd.read_excel("C:/Users/Adri/Documents/Tercer-Curso/Data Science/Ejercicios/Machine Learning/pokemon.xlsx")
data.drop("#",axis=1,inplace=True)
#VEMOS DE QUE TIPO SON LAS COLUMNAS SI OBJECTO, NUMERICA, FECHA...
a=data.dtypes


#%%

check(data,"calidad del dato.xlsx")

# =============================================================================
# # ~~                               FIN                                    ~~
# =============================================================================
