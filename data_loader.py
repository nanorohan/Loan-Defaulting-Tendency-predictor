#Import libraries
import pandas as pd
import csv
import numpy as np
import pickle

#Function for reducing the size of the Pandas Dataframe
def df_size_optimizer(df):
  """This function accepts a Pandas DataFrame and each feature variable type is checked and assigned appropriately. 
  This is primarily done to optimize the size the dataframe occupies on system RAM."""
  #Source ref [1] & Code Credit - https://www.kaggle.com/rinnqd/reduce-memory-usage
  #Source ref [2] - https://www.analyticsvidhya.com/blog/2021/04/how-to-reduce-memory-usage-in-python-pandas/ [For understanding the logic and implementation]  
  for col in df.columns:
    col_type=df[col].dtype
    if col_type!=object:
      c_min=df[col].min()
      c_max=df[col].max()
      if str(col_type)[:3]=='int':
        if c_min>np.iinfo(np.int8).min and c_max<np.iinfo(np.int8).max:
          df[col]=df[col].astype(np.int8)
        elif c_min>np.iinfo(np.int16).min and c_max<np.iinfo(np.int16).max:
          df[col]=df[col].astype(np.int16)
        elif c_min>np.iinfo(np.int32).min and c_max<np.iinfo(np.int32).max:
          df[col]=df[col].astype(np.int32)
        elif c_min>np.iinfo(np.int64).min and c_max<np.iinfo(np.int64).max:
          df[col]=df[col].astype(np.int64)  
      else:
        if c_min>np.finfo(np.float16).min and c_max<np.finfo(np.float16).max:
          df[col]=df[col].astype(np.float16)
        elif c_min>np.finfo(np.float32).min and c_max<np.finfo(np.float32).max:
          df[col]=df[col].astype(np.float32)
        else:
          df[col]=df[col].astype(np.float64)
  return df

#Import saved data and pickle files
bureau_numerical_merge = df_size_optimizer(pd.read_csv('bureau_numerical_merge.csv'))
bureau_categorical_merge = df_size_optimizer(pd.read_csv('bureau_categorical_merge.csv'))
previous_numerical_merge = df_size_optimizer(pd.read_csv('previous_numerical_merge.csv'))
previous_categorical_merge = df_size_optimizer(pd.read_csv('previous_categorical_merge.csv'))
model_temp = open('model.pkl', 'rb')
model = pickle.load(model_temp)
model_temp.close()
imputer_temp = open('imputer.pkl', 'rb')
imputer = pickle.load(imputer_temp)
imputer_temp.close()
scaler_temp = open('scaler.pkl', 'rb')
scaler = pickle.load(scaler_temp)
scaler_temp.close()
constant_temp = open('imputer_constant.pkl', 'rb')
imputer_constant = pickle.load(constant_temp)
constant_temp.close()
ohe_temp = open('ohe.pkl', 'rb')
ohe = pickle.load(ohe_temp)
ohe_temp.close()
