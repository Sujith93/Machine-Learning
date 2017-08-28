# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 08:17:47 2017

@author: jagadeeshwr Reddy
"""

from sklearn.datasets import load_iris

iris=load_iris()
x=iris.data
y=iris.target

print(x.shape)
print(y.shape)

#import the class
from sklearn.linear_model import LogisticRegression
#instantiate the model
logreg=LogisticRegression()
#fit the model with the data
logreg.fit(x,y)
#predict the response for new observaions
x_new=[[3,5,4,2],[5,4,3,2]]
logreg.predict(x_new)

#step1
y_pred2=logreg.predict(x)
len(y_pred2)

from sklearn import metrics
print(metrics.accuracy_score(y,y_pred2)) #traning accuracy
#if training accuracy is high(1) the data is over fitted,model is learned on noise instead of signal

#step2
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=4)#random_state=exact same for several times

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#fit the model with the data
logreg.fit(x_train,y_train)
#predict the response for new observaions
y_pred3=logreg.predict(x_test)
print(metrics.accuracy_score(y_test,y_pred3)) 













