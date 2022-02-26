#Import libraries
import pandas as pd
import csv
import numpy as np
from data_loader import (df_size_optimizer, bureau_numerical_merge, bureau_categorical_merge, previous_numerical_merge, 
previous_categorical_merge, model, imputer, scaler, imputer_constant, ohe)

#Define a function to create a pipeline for prediction
def inference(query):
	#Add columns titled DEBT_INCOME_RATIO to application_train
	query_int=query.copy();
	query_int['DEBT_INCOME_RATIO'] = query['AMT_ANNUITY']/query['AMT_INCOME_TOTAL']
	#Add columns titled LOAN_VALUE_RATIO to application_train
	query_int['LOAN_VALUE_RATIO'] = query['AMT_CREDIT']/query['AMT_GOODS_PRICE']
	#Add columns titled LOAN_INCOME_RATIO to application_train
	query_int['LOAN_INCOME_RATIO'] = query['AMT_CREDIT']/query['AMT_INCOME_TOTAL']
	#Merge numerical features from bureau to query
	query_bureau = query_int.merge(bureau_numerical_merge, on='SK_ID_CURR', how='left', suffixes=('', '_BUREAU'))
	#Merge categorical features from bureau to query
	query_bureau = query_bureau.merge(bureau_categorical_merge, on='SK_ID_CURR', how='left', suffixes=('', '_BUREAU'))
	#Drop SK_ID_BUREAU
	query_bureau = query_bureau.drop(columns = ['SK_ID_BUREAU'])
	#Shape of query and bureau data combined
	print('The shape of query and bureau data merged: ', query_bureau.shape)  
	#Merge numerical features from previous_application to query_bureau
	query_bureau_previous = query_bureau.merge(previous_numerical_merge, on='SK_ID_CURR', how='left', suffixes=('', '_PREVIOUS'))
	#Merge categorical features from previous_application to query_bureau
	query_bureau_previous = query_bureau_previous.merge(previous_categorical_merge, on='SK_ID_CURR', how='left', suffixes=('', '_PREVIOUS'))
	#Drop SK_ID_PREV and SK_ID_CURR
	query_bureau_previous = query_bureau_previous.drop(columns = ['SK_ID_PREV'])
	#Shape of query_bureau and previous_application data combined
	print('The shape of query_bureau and previous_application data merged: ', query_bureau_previous.shape)  
	#Drop SK_ID_PREV and SK_ID_CURR
	query_bureau_previous = query_bureau_previous.drop(columns = ['SK_ID_CURR'])
	query_numerical = query_bureau_previous.select_dtypes(exclude=object)
	query_categorical = query_bureau_previous.select_dtypes(include=object)
	query_numerical_imputed = imputer.transform(query_numerical)
	query_numerical_imputed_scaled = scaler.transform(query_numerical_imputed)
	query_categorical_imputed = imputer_constant.transform(query_categorical)
	query_categorical_imputed_ohe = ohe.transform(query_categorical_imputed)
	query_data = np.concatenate((query_numerical_imputed_scaled, query_categorical_imputed_ohe.toarray()), axis = 1)
	predictions = model.predict(query_data)
	pred_cat=[]
	for i in range(len(predictions)):
		if predictions[i]==0:
			pred_cat.append("Low")
		else:
			pred_cat.append("High")
	applicant_no=query['SK_ID_CURR'].copy()
	#applicant_no['Defaulting Tendency']=pred_cat
	pred_df=pd.DataFrame(pred_cat, columns = ['Defaulting Tendency'])
	pred_out=pd.concat([applicant_no,pred_df], axis=1, ignore_index=False)
	return pred_out

def convert_df(df):
   return df.to_csv().encode('utf-8')
   
