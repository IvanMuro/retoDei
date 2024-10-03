from astropy import units as u
import numpy as np
import pandas as pd

import fun_dist

df_json = pd.read_json('./data/reto.json', orient='split')

#Euclidean
#sum_dist_mat = []
print('\tEuclidean method')
for matricula, mat_group in df_json.groupby('Matricula'):
    lat, lon = np.array(mat_group['Latitud']), np.array(mat_group['Longitud'])
    dif_lat = lat[1:] - lat[:-1]
    dif_lon = lon[1:] - lon[:-1]
    dist = fun_dist.calc_dist(dif_lat, dif_lon)

    #sum_dist_mat.append(np.sum(dist))
    print(matricula, np.sum(dist))
    
print('\n\tAstropy')
#dct_sep = {}
for matricula, mat_group in df_json.groupby('Matricula'):
    lat, lon = np.array(mat_group['Latitud'])*u.deg, np.array(mat_group['Longitud'])*u.deg
    
    sep_lst = [ fun_dist.calc_sep_astropy(aux_lon, lon[loop_lon+1], lat[loop_lon], lat[loop_lon+1]) 
               for loop_lon, aux_lon in enumerate(lon[:-1]) ] 
    #dct_sep.update({f'{matricula}':sep_lst})
    print(matricula, np.sum(sep_lst))
    
print('\n\tHaversine')
dct_sep = {}

for matricula, mat_group in df_json.groupby('Matricula'):
    lat, lon = np.array(mat_group['Latitud'])*u.deg, np.array(mat_group['Longitud'])*u.deg

    sep_lst = [ fun_dist.haversine(lat[loop_lon], aux_lon, lat[loop_lon+1], lon[loop_lon+1])
                 for loop_lon, aux_lon in enumerate(lon[:-1]) ] 
    dct_sep.update({f'{matricula}':sep_lst})
    print(matricula, np.sum(sep_lst))