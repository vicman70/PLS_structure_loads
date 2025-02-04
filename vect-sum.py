import pandas as pd
from xlsxwriter import Workbook

#---Ingresa el nombre del archivo de excel que vamos a leer, en este caso se llamaba arbol.xlsx
df = pd.read_excel('StrLoadsReport_anclajes.xlsx')

loadCases = sorted(df["Load Case Description"].unique())

structures = sorted(df["Str. No."].unique())

print(structures)

#---Ingresa los nombres de los sets con el siguiente formato 'NombreQueRecibiráLaPrimerSuma': ['set1','set2], 'NombreQueRecibiráLaSegundaSuma': ['set3','set4']
sets = {1: [1,11], 2: [2,12]}

dicc = {}
ind = ['Str. No.', 'Set No.', 'Phase No.', 'Structure Loads Vert. (daN)', 'Structure Loads Trans. (daN)', 'Structure Loads Long. (daN)']

for case in loadCases:
    df_case = df[df['Load Case Description'] == case]
    for structure in structures:
        df_structure = df_case[df_case['Str. No.'] == structure]
        
        for key in sets.keys():
            add_results = []
            df_set = df_structure[df_structure['Set No.'].isin(sets[key])]

            add_results.extend([str(structure), key, 1, sum(df_set['Structure Loads Vert. (daN)']), sum(df_set['Structure Loads Trans. (daN)']), sum(df_set['Structure Loads Long. (daN)'])])

            dicc[str(case)+ '%' + str(structure) + ' ' + str(key)]=add_results #cuando se tenga el excel, se delimita con % los textos de la columna que da el nombre del caso climático y se elimina el texto de número de torre y número de set para luego acomodar esto al código que hace los cuadros de carga

#print(dicc)
#print(ind)

summary = pd.DataFrame(dicc, index=ind).transpose()
summary.to_excel('strengths.xlsx', engine='xlsxwriter')
print("Excel file created")
