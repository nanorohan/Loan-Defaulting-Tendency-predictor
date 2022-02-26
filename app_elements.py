#import the library
import base64

#Purpose of the app
app_intro = f"""
        <div style="display:flex;justify-content:space-between;background:#3E4248;padding:10px;border-radius:5px;margin:5px;">
            <div style="float:justify; text-align: justify; width:100%; background:#3E4248; padding:10px; border-radius:5px; margin:5px;">
                <p style="text-align: justify; color:#FFF8DC; line-height: 1.35;font-size: 23px; font-family:Playfair;">
		    <b>Loan Defaulter Predictor helps you identify potential defaulters.</b>
		    <br>
		    Given a loan application of a potential or existing client at Home Credit, this app "predicts" whether 
		    the client will be able to repay the loan or not.
		    <br>
		    Applicants deemed capable of repaying the loan shall be labelled <b>Low</b> under defaulting tendency and those deemed as incapable 
		    shall be labelled as <b>High</b>.    
                </p>    
            </div>
        </div>
	"""

# Side bar portion of app
overview_desc = f"""
  <div style="display:flex;justify-content:space-between;background:#FFEBCD;padding:10px;border-radius:5px;margin:5px;">
  <div style="float:justify; text-align: justify; width:100%; background:#FFEBCD; padding:10px; border-radius:5px; margin:5px;">
    <p style="text-align: justify; color:#8B0000; line-height: 1.35;font-size: 23px; font-family:Playfair;">
		  <h2 style="color:#000059; font-family:Playfair;">Why this app?</h2>
      <p style="color:#8B0000; text-align: justify; line-height: 1.35;font-size: 23px; font-family:Playfair;">
      Post-pandemic world has disrupted many aspects of life including financial requirements. 
      Many are resorting to loans to ensure basic subsistence. Some struggle to get loans due to insufficient or 
      non-existent credit histories. And, unfortunately, such a population is often taken advantage of by unscrupulous lenders. 
      Conversely, lending institutions need to ensure very low credit delinquency rates to stay profitable and provide loans to 
      worthy applicants.
      <br>
      An objective model helps the lending agencies disburse prudent loans. This system helps process and disburse loans faster, 
      increase profit and client base  as well as possibly protect genuine debtors from predatory lenders.
      <br>
      Thus, this app.
      <br>
      </p>
    </p>
    <p style="text-align: justify; color:#8B0000; line-height: 1.35;font-size: 23px; font-family:Playfair;">
      <h2 style="color:#000059; font-family:Playfair;">Behind the Secene</h2>
      <p style="color:#8B0000; text-align: justify; line-height: 1.35;font-size: 23px; font-family:Playfair;">
      This app is powered by Machine Learning! It uses a 
      <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html">Gradient Boosting Classifier model from SKlearn library</a>
      trained on Kaggle's <a href="https://www.kaggle.com/c/home-credit-default-risk/overview">Home Credit Default Risk dataset</a>. 
      I have used Streamlit & deployed this app on Heroku.
      A complete repository of this app right from data preprocessing upto the deployment can be viewed on my <a href="https://github.com/nanorohan">GitHub page</a>.
      Feedback and ideas may be directed <a href="mailto:nanorohan@gmail.com">here</a>.
      </p>
    </p>
	</div>
	</div>
  """

#Placeholders for the app elements
html_template = """
  <html>
	<body>
	<style> 
	#rcorners2 {border-radius: 20px; border: 3px solid #c83349; background: #1E323B; padding: 10px; color:tomato; 
	font-size:23px; font-family:Playfair; text-align:center;
	}	
	</style>
	<p id="rcorners2" >Please adhere to the template below to fill in applicant details for predicting defaulting tendency</p>
	<br>
  </body>
  </html>	
	"""

#file upload template
html_uploader = """
  <html>
	<body>
	<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
	<style> 
	p {
	  font-size: 23px;
	  color: #151B54;
	  font-family: Playfair, bold;
	  text-align: center;
	}	
	#rcorners1 {border-radius: 20px; border: 3px solid #c83349; background: #ffcc5c; padding: 10px;
	}	
	</style>
	<p id="rcorners1" >Upload applicant details in required format</p>
	</body>
  </html>
	"""	

#template for downloading the query appended with the predictions as csv file
html_file_dl = """
  <html>
	<body>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
	<style> 
	p {
	  font-size: 23px;
	  color: #151B54;
	  font-family: Playfair, bold;
	  text-align: center;
	}	
	#rcorners1 {border-radius: 20px; border: 3px solid #c83349; background: #ffcc5c; padding: 10px;
	}	
	</style>
	<p id="rcorners1" >For downloading the predictions appended to the applicant details, click below link</p>
	</body>
	</html>
	"""
