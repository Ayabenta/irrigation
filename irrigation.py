#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import schedule
import time
import pyrebase
import pandas as pd

def irrigation():
    config = {
    "apiKey": "AIzaSyDJM6U2PhmhURsYaBOFZ-mWJO4rn5GhKL8",
    "authDomain": "highagriv6.firebaseapp.com",
    "databaseURL": "https://highagriv6-default-rtdb.firebaseio.com",
    "projectId": "highagriv6",
    "storageBucket": "highagriv6.appspot.com",
    "messagingSenderId": "902180705852",
    "appId": "1:902180705852:web:893176f34cffa29909d539"}

    firebase = pyrebase.initialize_app(config)
    database = firebase.database()
    moisture = list(dict(database.child("soil_moisture").get().val()).values())
    h = moisture[-1]
    if h < 80 :
        irr='on'
    else :
        irr='off'
    database.child("").child("irrigation").set({'decision':irr})
schedule.every(2).seconds.do(irrigation)
while 1 : 
    schedule.run_pending()
    time.sleep(1)


# In[ ]:




