# Self Organizing Map

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('after_preprocessing.csv',encoding="cp1252")
dataset.insert(loc=0, column='A', value=range(0,dataset.shape[0]))

X = dataset.iloc[:, :56].values
# if u have target variable
#y = dataset.iloc[:, -1].values

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
X = sc.fit_transform(X)

# Training the SOM
from minisom import MiniSom
som = MiniSom(x = 5, y = 5, input_len = 56, sigma = 1.0, learning_rate = 0.5) # for 5by5 = 25 clusters
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 100)



# Visualizing the results
from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
#colorbar()
#markers = ['o', 's']
#colors = ['r', 'g']
#for i, x in enumerate(X):
#    w = som.winner(x)
#    plot(w[0] + 0.5,
#         w[1] + 0.5,
#         markers[y[i]],
#         markeredgecolor = colors[y[i]],
#         markerfacecolor = 'None',
#         markersize = 10,
#         markeredgewidth = 2)
#show()

# Identifying the clusters data.
mappings = som.win_map(X)
cluster_data = pd.DataFrame()
from decimal import Decimal
s=0
for i in range(5):
    for j in range(5):
        try:
            a = mappings[(i,j)]
            a1 = sc.inverse_transform(a)
            a2 = pd.DataFrame(a1)
            a2.insert(loc=0, column='cluster', value=Decimal(s+j))
            cluster_data = cluster_data.append(a2)
        except:
            pass
    s += 5

#for i in mappings.keys():
#    print(i)


set(cluster_data.cluster)
#len(set(cluster_data1.A))
len(set(dataset.A))
cluster_data1 = cluster_data.iloc[:,:2]
cluster_data1.columns = ['y_kmeans','A']

result = pd.merge(dataset, cluster_data1,how='left', on='A')
result = result.iloc[:,1:]

result.to_csv('somCluster.csv',index=False)
