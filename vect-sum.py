import pandas as pd
from xlsxwriter import Workbook

#---Ingresa el nombre del archivo de excel que vamos a leer ().xlsx)
df = pd.read_excel('StrLoadsFromPLS.xlsx')

loadCases = sorted(df["Load Case Description"].unique())
structures = sorted(df["Str. No."].unique())

#---Ingresa los nombres de los sets con el siguiente formato 'NombreQueRecibiráLaPrimerSuma': ['set1','set2], 'NombreQueRecibiráLaSegundaSuma': ['set3','set4']
sets = {1: [1,2,11,12]}
ind = ['Load Case Description', 'Str. No.', 'Set No.', 'Phase No.', 'Structure Loads Vert. (daN)', 'Structure Loads Trans. (daN)', 'Structure Loads Long. (daN)']

results = []

for case in loadCases:
    df_case = df[df['Load Case Description'] == case]
    for structure in structures:
        df_structure = df_case[df_case['Str. No.'] == structure]
        for key in sets.keys():
            df_set = df_structure[df_structure['Set No.'].isin(sets[key])]
            add_results = [
                case,
                structure,
                key,
                1,
                sum(df_set['Structure Loads Vert. (daN)']),
                sum(df_set['Structure Loads Trans. (daN)']),
                sum(df_set['Structure Loads Long. (daN)'])
            ]
            results.append(add_results)

summary = pd.DataFrame(results, columns=ind)
summary.to_excel('VectSum.xlsx', engine='xlsxwriter')
print("Excel file created")

