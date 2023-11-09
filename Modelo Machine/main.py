import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import r2_score 

borouT = pd.read_csv('data/taxis_trips.csv')

app = FastAPI()
@app.get('/predecir_costo/{}')

def predecir_costo(recorrido, tiempo):
    data = borouT[['trip_distance','fare_amount','duracion_segundos']].copy()
    linear_model = LinearRegression()

    x1 = data['trip_distance']
    x2 = data['duracion_segundos']

    y = data['fare_amount']

    X = np.vstack((x1,x2)).T

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)


    linear_model.fit(X_train, y_train)

    y_train_pred = linear_model.predict(X_train) 
    y_test_pred = linear_model.predict(X_test) 

    rmse_train = (mean_squared_error(y_train, y_train_pred, squared = False))
    rmse_test = (mean_squared_error(y_test, y_test_pred, squared = False))


    rmse_train
    rmse_test

    r2 = r2_score(y_test, y_test_pred)
    r2

    r2_train = r2_score(y_train, y_train_pred)
    r2_train

    tarifa_predicha = linear_model.predict([[recorrido,tiempo]])

    return tarifa_predicha,  r2_train , rmse_train
