from datetime import datetime

import pandas as pd

df_json = pd.read_json('./data/reto.json', orient='split')

date_frmt = '%d-%m-%Y %H:%M:%S'
df_json['date_fmt'] = [datetime.fromtimestamp(ts*1e-3).strftime(date_frmt) 
                 for ts in list(df_json['Pos_date'])]

lst_pos = []
mask_lst_pos = []

for matricula, mat_group in df_json.groupby('Matricula'):
    print(mat_group.sort_values('date_fmt', ascending=False)[:1][['Matricula', 'date_fmt']])
    
    lst_pos.append(mat_group.sort_values('date_fmt', ascending=False)[:1].date_fmt.item())
    mask_lst_pos.append(mat_group.sort_values('date_fmt', ascending=False)[:1].date_fmt.index[0])
    
df_json.loc[mask_lst_pos].sort_values('date_fmt', ascending=False).to_csv('./data/lst_pos.csv', index=False)
