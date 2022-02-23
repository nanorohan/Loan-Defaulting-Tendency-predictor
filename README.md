# Loan Defaulting Tendency predictor
An end-to-end binary classification model based on the Home Credit Default Risk competition dataset hosted on Kaggle

[💸Streamlit App](https://share.streamlit.io/nelsonchris1/ml-explainability-app/main/app.py)



## ✅ Description
Post-pandemic world has disrupted many aspects of life including financial requirements. Many are resorting to loans to ensure basic subsistence. Some struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, such a population is often taken advantage of by unscrupulous lenders. 
Conversely, lending institutions need to ensure very low credit delinquency rates to stay profitable and provide loans to	worthy applicants.
<br>
An objective model helps the lending agencies disburse prudent loans. This system helps process and disburse loans faster, increase profit and client base as well as possibly protect genuine debtors from predatory lenders.
<br>
<b>Loan Defaulter Predictor</b> helps you identify potential defaulters.
Given a loan application of a potential or existing client at Home Credit, this app predicts whether the client will be able to repay the loan or not.
Applicants deemed capable of repaying the loan shall be labelled <b>Low</b> under defaulting tendency and those deemed as incapable shall be labelled as <b>High</b>. 



## ✅ Python Libraries used
| Name  | What its used for |
| ------------- | ------------- |
| Streamlit  |  *An open source app framework for building beautiful data and ML apps* |
| PyCaret  | *An open-source, low-code machine learning library in Python that automates machine learning workflows.*  |
| PyOD | *A comprehensive and scalable Python toolkit for detecting outlying objects in multivariate data.* |
| Phi-K | *A new and practical correlation coefficient based on several refinements to Pearson’s hypothesis test of independence of two variables.* |
| MLxtend | *A Python library of useful tools for the day-to-day data science tasks.* |
| Keras | *An open-source software library that provides a Python interface for artificial neural networks.* |
| SHAP | *A game theoretic approach to explain the output of any machine learning model implemented in Python.* |
| LIME | *A Python library about explaining what machine learning classifiers (or models) are doing, supporting explaining individual predictions* |
| sklearn | *A Python library containing an ensemble of simple and efficient tools for predictive data analysis* |
| seaborn | *A Python data visualization library providing a high-level interface for drawing attractive and informative statistical graphics.* |
| matplotlib | *A comprehensive library for creating static, animated and interactive visualizations in Python.* |
| Pandas | *A Python library for data manipulaion and analysis*|
| Numpy | *A Python library for numerical computation*|



## ✅ High-level summary
* The dataset for training and testing the model is sourced from Kaggle's [Home Credit Default Risk competition](https://www.kaggle.com/c/home-credit-default-risk).<br>
* This is a binary classification [defaulter or not] with imbalanced data [defaulters are approximately 8% of total sample population].<br>
* Performance metrics are decided cosnidering these quirks.<br>
* Elaborate Exploratory Data Analysis is carried out to visualize the data and get context for feature importance.<br>
* A strategy for creating new features is decided based on EDA & literature reviews/domain knowledge and dataset is prepared.<br>
* Model-based feature selection is performed to reduce model complexity.<br>
* All required pre-processing such as imputation, standardization, encoding, etc. is carried out .<br>
* With train-test split done, through PyCaret, a number of models are evaluated and best model is selected.<br> 
* The best model and entire dataflow pipeline is created using sklearn and the process is deployed on Heroku using Streamlit.<br>



## ✅ If you want to use/improve upon this app
* Fork the repo
* Clone the repo
* Navigate to your local repository
* Pull latest changes from upstream to local repository
* create new branch
* Contribute
* Commit changes
* Push changes to your fork
* Begin pull request(PR)
