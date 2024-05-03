import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from scipy.stats import f_oneway
from tkinter import ttk
import tkinter as tk
data = pd.read_csv('FINAL_USO.csv')

#converting data into the same type to normalize it
data['Date'] = pd.to_datetime(data['Date'])
data[data.columns[1:81]] = data[data.columns[1:81]].astype(float)
data = data.rename(columns = {'Open' : 'Opening Price', 'Close' : 'Closing Price in $'}, inplace = False)
data.dtypes

corr_columns_matrix = data.corr()

corr_columns_matrix['Closing Price in $'][abs(corr_columns_matrix['Closing Price in $']) >.5]

new_data = data[corr_columns_matrix]

final_selection = ['GDX_Low', 'SF_Price', 'High', 'EG_open']

aidata = data[final_selection]

numericdata_ai = pd.get_dummies(aidata)

numericdata_ai['Closing Price in $'] = data['Closing Price in $']


TargVar = 'Closing Price in $'
PredVars = ['GDX_Low', 'SF_Price', 'High', 'EG_open']
X = numericdata_ai[PredVars].values
y = numericdata_ai[TargVar].values
ScalePredictors = StandardScaler()
FitScalePredictors = ScalePredictors.fit(X)
X = FitScalePredictors.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 69)
linear_model = LinearRegression()
LINEAR_M = linear_model.fit(X_train,y_train)
funcPrediction = LINEAR_M.predict(X_test)
DECISION_TREE = DecisionTreeRegressor(max_depth = 3)
LinearModel = AdaBoostRegressor(n_estimators = 100, estimator = DECISION_TREE, learning_rate = 0.04)
XL = LinearModel.fit(X_train,y_train)
prediction_results = XL.predict(X_test)

@property
def funcPrediction(number):
    prediction_return = XL.predict(number)
    return(prediction_return)

