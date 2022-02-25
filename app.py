import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
date_input = st.text_input("Enter the date with format yyy-mm-dd")
time_input = st.text_input("Enter the time with format hh:mm:ss")
date_time_input = date_input + " " + time_input
date_time_object = datetime.datetime.strptime(date_time_input, '%Y-%m-%d %H:%M:%S')

pickup_longitude = st.number_input("pickup_longitude")
pickup_latitude = st.number_input("pickup_latitude")
dropoff_longitude = st.number_input("dropoff_longitude")
dropoff_latitude = st.number_input("dropoff_latitude")
passenger_count = st.number_input("passenger_count")

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


# 2. Let's build a dictionary containing the parameters for our API...

params = {"pickup_datetime" : date_time_object,
          "pickup_longitude" : pickup_longitude,
          "pickup_latitude" : pickup_latitude,
          "dropoff_longitude" : dropoff_longitude,
          "dropoff_latitude" : dropoff_latitude,
          "passenger_count" : int(passenger_count)
          }

# 3. Let's call our API using the `requests` package...

taxifare_api_url = "http://127.0.0.1:8000/predict"

response = requests.get(
    taxifare_api_url,
    params=params
)

if response.status_code == 200:
    print("API call success")
else:
    print("API call error")


# 4. Let's retrieve the prediction from the **JSON** returned by the API...

prediction = response.json().get("pred", "no prediction")

## Finally, we can display the prediction to the user
st.write(prediction)
