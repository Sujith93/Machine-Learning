# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 21:34:23 2017

@author: jagadeeshwr Reddy
"""



import pandas as pd
data=pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv',index_col=0)

data.head()
data.tail()
data.shape

#for visualization
import seaborn as sns
#visualize the relationship between the features and the response using scatterplot
sns.pairplot(data,x_vars=['TV','Radio','Newspaper'],y_vars='Sales')
sns.pairplot(data,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',size=7,aspect=0.7) #increase size
#TV high
#Radio low
#Newspaper weak

sns.pairplot(data,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',size=7,aspect=0.7,kind='reg')


#features
features_col=['TV','Radio','Newspaper']
x=data[features_col]   #dataframe
#x=data[['TV','Radio','Newspaper']]
x.head()

type(x)
x.shape

#taregt
y=data['Sales'] #series
#y=data.Sales
y.head()

type(y)
y.shape


#spliting the x and y

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1 )#default 75-25%

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)



#import model
from sklearn.linear_model import LinearRegression
#instantiate
linreg=LinearRegression()
#fitthe model
linreg.fit(x_train,y_train)

#interpreting the model
#intercept and coefficients
print(linreg.intercept_)
print(linreg.coef_)

zip(features_col,linreg.coef_)
list(zip(features_col,linreg.coef_))

#y=2.8 + 0.04  TV + 0.17 Radio + 0.003 Newspaper    
#if unit change in tv there will be 0.04 unit increase in sale
#addition 1000$ on Tv adds is associated with increase in sale of 46.6 items  

#statement of association , not causation

#prediction
y_pred=linreg.predict(x_test)



#Metrices
#MAE
true=[100,50,30,20]
pred=[90,50,50,30]
#by hand
print((10+0+20+10)/4)

from sklearn import metrics
print(metrics.mean_absolute_error(true,pred))

#MSE
#by hand
print((10**2+0**2+20**2+10**2)/4)
print(metrics.mean_squared_error(true,pred))

#RMSE
import numpy as np
print(np.sqrt((10**2+0**2+20**2+10**2)/4))
print(np.sqrt(metrics.mean_squared_error(true,pred)))

#comparing metrics
#MAE-easy to understand,because its avaerage error
#MSE-more popular than MAE,beacuse its punishes large errors.
#RMSE-more popular than MSE,beacuse RMSE interpretable in y units

print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))#1.40465


#feature selection
#Newspaper is removed because its weak ,check RMSE

features_col=['TV','Radio']
x=data[features_col] 
y=data.Sales
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1 )
linreg.fit(x_train,y_train)
y_pred=linreg.predict(x_test)
print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))#1.39



