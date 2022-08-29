###############################
# This program lets you       #
# - enter values in Streamlit #
# - get prediction            #
###############################
import streamlit as st
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

from tensorflow.python.keras import utils
st.title("Web App for Hotel Check-In Prediction")
st.image("""https://images.pexels.com/photos/4907455/pexels-photo-4907455.jpeg?auto=compress&cs=tinysrgb&w=600""")
st.header('Please feed in the below parameters to get Check-In prediction:')

#Loading the model
loaded_model = load_model(r'model.h5')

# Get input from user
Age = st.number_input("Enter Person's Age", min_value=0,
                 max_value=100, value=0)
SRHighFloor = st.number_input("Enter 1 if room is at higher floor", min_value=0,
                 max_value=1, value=0)
SRCrib = st.number_input("Enter 1 if Crib is present", min_value=0,
                 max_value=1, value=0)
SRKingSizeBed = st.number_input("Enter 1 if King size bed is present", min_value=0,
                 max_value=1, value=0)
SRTwinBed = st.number_input("Enter 1 if King twin bed is present", min_value=0,
                 max_value=1, value=0)

 #Get Input for Categorical data
Nationality = st.selectbox('Please choose your Nationality',
                            ('Brasil',
                             'Canada',
                             'Espanol',
                             'Portugese',
                             'USA'))
if Nationality == 'Brasil':
     Nationality_BRA = 1
     Nationality_CAN = 0
     Nationality_ESP = 0
     Nationality_PRT = 0
     Nationality_USA = 0
elif Nationality == 'Canada':
     Nationality_BRA = 0
     Nationality_CAN = 1
     Nationality_ESP = 0
     Nationality_PRT = 0
     Nationality_USA = 0
elif Nationality == 'Espanol':
     Nationality_BRA = 0
     Nationality_CAN = 0
     Nationality_ESP = 1
     Nationality_PRT = 0
     Nationality_USA = 0
elif Nationality == 'Portugese':
     Nationality_BRA = 0
     Nationality_CAN = 0
     Nationality_ESP = 0
     Nationality_PRT = 1
     Nationality_USA = 0
else:
     Nationality_BRA = 0
     Nationality_CAN = 0
     Nationality_ESP = 0
     Nationality_PRT = 0
     Nationality_USA = 1

Distribution = st.selectbox('Please choose distribution type',
                            ('Corporate',
                             'Electronic',
                             'Travel_Agent'))

if Distribution == 'Corporate':
      DistributionChannel_Corporate = 1
      DistributionChannel_Electronic = 0
      DistributionChannel_Travel_Agent = 0
elif Distribution == 'Electronic':
     DistributionChannel_Corporate = 0
     DistributionChannel_Electronic = 1
     DistributionChannel_Travel_Agent = 0
elif Distribution == 'Travel_Agent':
     DistributionChannel_Corporate = 0
     DistributionChannel_Electronic = 0
     DistributionChannel_Travel_Agent = 1

MarketSegment = st.selectbox('Please choose Market Segment',
                            ('Corporate','Direct',
                             'Groups', 'Other'))

if MarketSegment == 'Corporate':
      MarketSegment_Corporate = 1
      MarketSegment_Direct = 0
      MarketSegment_Groups = 0
      MarketSegment_Other = 0

elif MarketSegment == 'Direct':
      MarketSegment_Corporate = 0
      MarketSegment_Direct = 1
      MarketSegment_Groups = 0
      MarketSegment_Other = 0
elif MarketSegment == 'Groups':
      MarketSegment_Corporate = 0
      MarketSegment_Direct = 0
      MarketSegment_Groups = 1
      MarketSegment_Other = 0
else:
      MarketSegment_Corporate = 0
      MarketSegment_Direct = 0
      MarketSegment_Groups = 0
      MarketSegment_Other = 1

# when predict is clicked , make prediction and store it
if st.button("Predict Check-In"):
    X = pd.DataFrame({'Age': [Age],
                      'SRHighFloor': [SRHighFloor],
                      'SRCrib': [SRCrib],
                      'SRKingSizeBed': [SRKingSizeBed],
                      'SRTwinBed': [SRTwinBed],
                      'Nationality_BRA': [Nationality_BRA],
                      'Nationality_CAN': [Nationality_CAN],
                      'Nationality_ESP': [Nationality_ESP],
                      'Nationality_PRT': [Nationality_PRT],
                      'Nationality_USA': [Nationality_USA],
                      'DistributionChannel_Corporate': [DistributionChannel_Corporate],
                      'DistributionChannel_Electronic': [DistributionChannel_Electronic],
                      'DistributionChannel_Travel_Agent': [DistributionChannel_Travel_Agent],
                      'MarketSegment_Corporate': [MarketSegment_Corporate],
                      'MarketSegment_Direct': [MarketSegment_Direct],
                      'MarketSegment_Groups': [MarketSegment_Groups],
                      'MarketSegment_Other': [MarketSegment_Other]
                      })

    # Making Prediction
    prediction = loaded_model.predict(X)
    prediction_classes = [1 if prob > 0.5 else
                      0 for prob in np.ravel(prediction)]
    if prediction_classes == 1:
        st.success("User will Check-In")
    else:
        st.success("User will not Check-In")