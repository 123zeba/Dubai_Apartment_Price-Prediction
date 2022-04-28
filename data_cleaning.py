

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#importing the dataset
df = pd.read_csv('data.csv')
print(df.shape)

#to check missing values
print(df.isnull().sum())

#to check duplicate rows

print(df.duplicated())

#to check no: of duplicated rows except first occurrence based on all columns
duplicateRowsDF = df[df.duplicated()]
print(len(duplicateRowsDF))

#to remove duplicated row

df=df.drop_duplicates()
print(df.shape)
#to replace studio by 0
df=df.replace('Studio',0)
#to remove ','
df["area"] = df['area'].str.replace(',', '').astype(int)
df["price"] = df['price'].str.replace(',', '').astype(int)

df.to_csv('data1.csv',index=False)




