

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#importing the dataset
df = pd.read_csv('data1.csv')
print(df.shape)

#statistical measure of the data set
print(df.describe())

#price analysis
print(df.price.describe())

#price distribution
fig, ax = plt.subplots(figsize = (8, 8))
sns.distplot(df.price)

#to check skewness and kurtosis
print("Skewness: %f" % df.price.skew())
print("Kurtosis: %f" % df.price.kurt())
#to select data under 220001 aed
df2 = df[df.price < 220001]
print(df2.shape)

df3 = df[df.price > 220000]
print(df3.shape)

#price distribution
fig, ax = plt.subplots(figsize = (8, 8))
sns.distplot(df2.price)
#to check skewness and kurtosis
print("Skewness: %f" % df2.price.skew())
print("Kurtosis: %f" % df2.price.kurt())

df2.to_csv('data2.csv',index=False)

