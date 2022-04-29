# APARTMENT PRICE PREDICTION - DUBAI


Real Estate is one of the important sectors that have a great influence on the national economy. 
Rental prices and their changes have a great impact on residential investment and economic growth. 
Therefore house price prediction is an important topic for real estate. 
The price of a house depends on many factors like location, square feet area, number of bedrooms, bathrooms, etc.

This project aims to predict the rent of apartments in Dubai. 
The data that has been used is web scrapped from one of the famous real estate search engines in Dubai.
It has information about the number of bedrooms, bathrooms, title(building name and location), building name, and square feet area. 

# WORK FLOW

1. Data collection(web scrapping)
2. Data cleaning
3. Data analysis
4. Data preprocessing
5. Train-test split 
6. Training regression model
7. Evaluation

# Data cleaning and analysis

The data set consists of 30613 records of which 9874 are duplicate properties that have to be removed.
![price distribution](https://user-images.githubusercontent.com/35625908/165927176-e4e9f4d2-99f3-4106-8303-4f5a60c8dd20.png)




The figure shows the distribution of price in our data set. Price ranges from 8400 to 1875000 and It could be seen that price distribution is positively skewed. Skewness is 5.002124, which means the number of apartments with low prices is more. 
While training our model it gives better prediction at predicting the apartments with low prices. 
Here apartments with high prices are outliers so we remove them. 

# DATA PREPROCESSING
Converting categorical feature(title) into numerical feature.

