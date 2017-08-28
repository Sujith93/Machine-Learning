# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 06:43:56 2017

@author: jagadeeshwr Reddy
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits=datasets.load_digits()
print(digits.data)
print(digits.target)
print(digits.images[0])

clf=svm.SVC(gamma=0.001,C=100)#0.1 #0.0001

print(len(digits.data))
x,y=digits.data[:-10],digits.target[:-10]#left last 10 for testing

clf.fit(x,y)

print('Prediction:',clf.predict(digits.data[-2]))
plt.imshow(digits.images[-2],cmap=plt.cm.gray_r,interpolation='nearest')

print('Prediction:',clf.predict(digits.data[-1]))
plt.imshow(digits.images[-1],cmap=plt.cm.gray_r,interpolation='nearest')

print('Prediction:',clf.predict(digits.data[-3]))
plt.imshow(digits.images[-3],cmap=plt.cm.gray_r,interpolation='nearest')

print('Prediction:',clf.predict(digits.data[-4]))
plt.imshow(digits.images[-4],cmap=plt.cm.gray_r,interpolation='nearest')