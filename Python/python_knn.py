# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 07:35:43 2017

@author: jagadeeshwr Reddy
"""

from sklearn.datasets import load_iris

iris=load_iris()
x=iris.data
y=iris.target

print(x.shape)
print(y.shape)

#step1
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)#instantiate the mode
print(knn) #see default parameters

knn.fit(x,y) #Training
knn.predict([3,5,4,2])      #Predict

x_new=[[3,5,4,2],[5,4,3,2]] #can predict multiple obs at oncek
knn.predict(x_new) 

y_pred=knn.predict(x)
len(y_pred)

from sklearn import metrics
print(metrics.accuracy_score(y,y_pred)) #traning accuracy

#step2
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=4)#random_state=exact same for several times

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

knn.fit(x_train,y_train) #Training
y_pred4=knn.predict(x_test)      #Predict

print(metrics.accuracy_score(y_test,y_pred4)) 







#Tuning with different k value
#from instantiate
knn1=KNeighborsClassifier(n_neighbors=5)#instantiate the estimator
print(knn1) #see default parameters

knn1.fit(x,y) #Training

knn1.predict(x_new)



y_pred1=knn.predict(x)
len(y_pred1)

from sklearn import metrics
print(metrics.accuracy_score(y,y_pred1)) #traning accuracy


#step2

knn1.fit(x_train,y_train) #Training
y_pred5=knn1.predict(x_test)      #Predict

print(metrics.accuracy_score(y_test,y_pred5)) 






#try k=1 through 25 and record testing accuracy
k_range=range(1,26)
scores=[]
for k in k_range:
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    y_pred=knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test,y_pred))


import matplotlib.pyplot as plt
plt.plot(k_range,scores)
plt.xlabel('value of k')
plt.ylabel('Testing accuracy')

#lower k value =more complex,so we need to take optimal k (middle)

knn=KNeighborsClassifier(n_neighbors=11)
knn.fit(x_train,y_train)
knn.predict([3,5,4,2])

