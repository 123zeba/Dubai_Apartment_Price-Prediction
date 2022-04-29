

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# encoding the dataset
df = pd.read_csv('data2.csv')

df1 = pd.concat([df.drop('title', 1), df['title'].str.get_dummies(sep=",")], 1)
df1.to_csv('data3.csv',index=False)


