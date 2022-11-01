import os
import pandas as pd 

def save_as_csv(df, csv_path): 
    df.to_csv(csv_path, mode='a', sep=',', na_rep='null', header=False, index=False)