# Hotel Check_in Predictor App using Streamlit
## By: Himanshu Gupta
___________________________________________________________________________________________________

### Statement of Purpose

The purpose of this repository creating a prediction model that predicts whether a guest will check-in into a hotel, and building a simple frontend application to make the model publicly available using Streamlit.

#Live Link for the App - https://imrawwk-hotel-check-in-prediction-app-ry2zy9.streamlitapp.com/

### Data Description 

The data we will be using for this project is a Hotel Check-In dataset. It contains 82578 observations in the training set & 1000 observation in the test set and 29 features in the dataset.

## How to Use the Predictor 

Just open the live link of the model from this streamlit link - https://imrawwk-hotel-check-in-prediction-app-ry2zy9.streamlitapp.com/
Enter the Parameters 
Click on  the Predict Check-In button
Your prediction will be generated!!!

## Steps followed for the Deployment 

1. The first step was to start by building the modelnwhich we will deploy.
2. After the model was built it was checked on test data & checked for prediction.
3. Then we saved the model to a seperate file to deploy it later.
4. After building & testing the model we developed an app.py file which had all the necessary steps for deployment.
5. We start by importing necessary packages for deployment like streamlit, tensorflow, pandas etc.
6. The Front-end part of the app was created using streamlit package in python.
7. Then to deploy it the app.py file was pushed to github repository with the other neccessary files 
   like the requirement.txt,saved model file.
8. The requirements.txt file contains list of all the necessary packages that are needed for prediction.
   Streamlit used this file to install all the necessary packages for prediction.
   
## Bonus Questions - 

1. Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution). 
Ans - 
      There are a few such difficult problems I have worked on till date - (I will also put the links of blogs to these problems below) 
      1. Ashrae - The Great Energy Predictor III
      
      Problem Statement - We have to develop accurate models of metered building energy usage in the following areas: chilled water, electric, 
      hot water and steam meters. The data is gathered from over 1000 buildings over a three year timeframe.With better estimates of these 
      energy saving investments, large scale investors and financial institutions will be more inclined to invest in this area to enable 
      progress in building efficiencies.
       
      Blog Link - https://medium.com/@hims1991l/ashrae-great-energy-predictor-iii-ec5e188ef596
      (If you have exhasuted your quota of free readings on medium open the link in incognito mode)
      
      2. Pneumothorax Segmentation Challenge
      
      Pneumothorax is usually detected by a radiologist & sometime it gets quite difficult to detect for them too.Pneumothorax can be caused 
      due to a blunt chest injury, damage from underlying chest disease or most horrifying — it may occur for no obvious reason at all. to summarize 
      we can say our task here is to achieve the following :

      Detect whether Pneumothorax is present in any given X-ray
      Determine the extent of Pneumothorax i.e. the shape & size of Pneumothorax.
      
      Blog Link - https://medium.com/@hims1991l/pneumothorax-segmentation-challenge-1be88c83e9ec
      
      
2. Explain back propagation and tell us how you handle a dataset if 4 out of 30 parameters have null values more than 40 percentage?
Ans - 
      Backpropogation can be defined as the process of weight adjustment for nueron by looking at the difference between the predicted and the actual results.Backpropogation is like the last layer of neurons giving feedback to the previos layers on how to better adjust their weights & biases to reduce the difference between actual & predicted results.
      
   2b. How to handle if 4 out of 30 parameters have null values more than 40 percentage?
   
   Ans.
    Depends on what type of data it is if its categorical data we can assign it  new  missing label to all the missing entires so the missing data has a new
    categoty called missing.If its numerical data we can fill it with the most frequent value or mean value depending on the data that is provided.
    Apart from this we can also add a binary missing indicator to all these rows so that the model that the value is an imputed one.It can be done somewhat this way - 
    X_train[var + '_na'] = np.where(X_train[var].isnull()).
     
     



