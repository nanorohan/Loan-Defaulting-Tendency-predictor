#Import libraries
import pandas as pd
import csv
import numpy as np
import pickle
from data_loader import df_size_optimizer
from model_pipeline import inference, convert_df
from app_elements import app_intro, overview_desc, html_template, html_uploader, html_file_dl
import streamlit as st
import base64
from PIL import Image

def main():
	st.set_page_config(
    page_title="Loan Defaulter Predictor",
	  page_icon="💸",
	  layout="wide",
	  initial_sidebar_state="collapsed",
  )
	header_pic = Image.open('loan_alt.jpg')
	st.image(header_pic)

	st.write(app_intro, unsafe_allow_html=True)

	st.sidebar.write(overview_desc, unsafe_allow_html=True)

	st.markdown(html_template,unsafe_allow_html=True)

	with open("applicants_details_template.csv") as template_file:
		temp_df=pd.DataFrame(template_file)
		required_fields=temp_df.columns.values.tolist()
		st.download_button("Download Applicant details template", template_file, "applicants_details_template.csv", key='download-csv')	

	st.markdown(html_uploader,unsafe_allow_html=True)
	uploaded_file = st.file_uploader("Upload a CSV file only",['csv'])    

	if uploaded_file is not None:
		query = df_size_optimizer(pd.read_csv(uploaded_file))
		col_names=query.columns.values.tolist()
		if col_names==required_fields:
			query_prediction = inference(query)
			query_pred=pd.DataFrame(query_prediction)
			query_pred.columns = ['Applicant ID', 'Defaulting Tendency']
			st.dataframe(query_pred)
			pred_append=pd.concat([query,query_pred['Defaulting Tendency']], axis=1, ignore_index=False)
			csv=convert_df(pred_append)
			st.markdown(html_file_dl,unsafe_allow_html=True)
			st.download_button("Press to Download", csv, "Defaulter_predictions.csv", key='download-csv')
		else:
			st.error('Input applicant form-fields are not in the prescribed format. Please ahdere to the template for processing.')
		
if __name__=='__main__':
    main()
