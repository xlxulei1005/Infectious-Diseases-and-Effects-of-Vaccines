'''
Module for calculating the average numbers of infected people before and after vaccine invented 
Created on Dec 15, 2016
'''
import get_heatmap_matrix
from get_heatmap_matrix import heatmap_disease_matrix
import numpy as np

Measles_vaccine_year = 1963
Hepatitis_A_vaccine_year = 1995
Mumps_vaccine_year = 1967
Rubella_vaccine_year = 1969
Smallpox_vaccine_year = 1796
Poliomyelitis_vaccine_year = 1955

def get_mean(disease):
    
    df = heatmap_disease_matrix(disease) 
    df['sum_all_state'] = df.sum(axis=1)
    df = df[['sum_all_state']] 
    
    if disease == 'measles':
        mean_before_vc = np.mean(df.loc[:Measles_vaccine_year])
        mean_after_vc  = np.mean(df.loc[Measles_vaccine_year:])
    elif disease == 'hepatitis_a':
        mean_before_vc = np.mean(df.loc[:Hepatitis_A_vaccine_year])
        mean_after_vc  = np.mean(df.loc[Hepatitis_A_vaccine_year:])
    elif disease == 'rubella':
        mean_before_vc = np.mean(df.loc[:Rubella_vaccine_year])
        mean_after_vc  = np.mean(df.loc[Rubella_vaccine_year:])
    elif disease == 'poliomyelitis':
        mean_before_vc = np.mean(df.loc[:Poliomyelitis_vaccine_year])
        mean_after_vc  = np.mean(df.loc[Poliomyelitis_vaccine_year:])
    elif disease == 'smallpox':
        mean_before_vc = np.mean(df.loc[:Smallpox_vaccine_year])
        mean_after_vc  = np.mean(df.loc[Smallpox_vaccine_year:])
    else:
        mean_before_vc = np.mean(df.loc[:Mumps_vaccine_year])
        mean_after_vc  = np.mean(df.loc[Mumps_vaccine_year:])
    
    return [mean_before_vc,mean_after_vc]