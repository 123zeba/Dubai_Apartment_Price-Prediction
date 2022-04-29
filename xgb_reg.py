# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:57:21 2022

@author: Rishab
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importing the dataset
dataset = pd.read_csv('data3.csv')
X = dataset.iloc[:, 1:].values
y = dataset.iloc[:, 0].values
print(dataset.shape)
print(dataset.isnull().sum)
print(dataset.describe())

print(X)
print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#training
from xgboost import XGBRegressor
regressor=XGBRegressor(n_estimators=5000)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
from sklearn.metrics import r2_score
print(r2_score(y_test, y_pred))

