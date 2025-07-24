import pandas as pd
from xlsxwriter import Workbook

#---Ingresa el nombre del archivo de excel que vamos a leer ().xlsx)
df = pd.read_excel('PLSCADDStrLoadsReport.xlsx')

structures = sorted(df["Str. No."].astype(str).unique())

#---Ingresa los nombres de los sets con el siguiente formato 'NombreQueRecibiráLaPrimerSuma': ['set1','set2], 'NombreQueRecibiráLaSegundaSuma': ['set3','set4']
sets = {1: [1,2,11,12]}
ind = [
    'Str. No.',
    'Str. Name',
    'Load Case Description',
    'Set No.',
    'Phase No.',
    'Structure Loads Vert. (daN)',
    'Structure Loads Trans. (daN)',
    'Structure Loads Long. (daN)'
]

results = []

for structure in structures:
    df_structure = df[df['Str. No.'].astype(str) == structure]
    str_name = df_structure['Str. Name'].iloc[0] if not df_structure.empty else ''
    loadCases = sorted(df_structure["Load Case Description"].unique())
    for case in loadCases:
        df_case = df_structure[df_structure['Load Case Description'] == case]
        # 1. Handle sets in your dictionary (sum)
        for key in sets.keys():
            df_set = df_case[df_case['Set No.'].isin(sets[key])]
            add_results = [
                structure,
                str_name,
                case,
                key,
                1,
                sum(df_set['Structure Loads Vert. (daN)']),
                sum(df_set['Structure Loads Trans. (daN)']),
                sum(df_set['Structure Loads Long. (daN)'])
            ]
            results.append(add_results)
        # 2. Handle all other sets (no sum, just append each row)
        other_sets = set(df_case['Set No.'].unique()) - set(sum(sets.values(), []))
        for set_no in other_sets:
            df_other = df_case[df_case['Set No.'] == set_no]
            for _, row in df_other.iterrows():
                add_results = [
                    structure,
                    str_name,
                    case,
                    set_no,
                    row['Phase No.'],
                    row['Structure Loads Vert. (daN)'],
                    row['Structure Loads Trans. (daN)'],
                    row['Structure Loads Long. (daN)']
                ]
                results.append(add_results)

summary = pd.DataFrame(results, columns=ind)
summary.to_excel('StrLoadsReportWithVectSum.xlsx', engine='xlsxwriter', index=False)
print("Excel file created")

