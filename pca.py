import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
import pandas as pd
import re
from random import randint
numbers = re.compile(r'[0-9]')
dataset = sys.argv[1]

try:
    df = pd.read_csv(dataset)
except:
    print('File {} not found'%(dataset))
df = df.dropna(axis = 0)

shape = df.dtypes.size

for (col, typ) in zip(df.columns, df.dtypes):
    if  typ== object:
        df = df.drop(col, axis = 1)
X = df.to_numpy()

if len(sys.argv) > 2:
    if sys.argv[2] == 'r':
        if len(sys.argv)>3:
            target = sys.argv[3]
        else:
            target = X[:,-1]
        y = df[target].to_numpy()
        y = y - min(y)
        y = y/np.max(y)
        rgb = np.c_[np.ones(y.shape[0])-y,np.zeros(y.shape[0]), y]
    elif sys.argv[2] == 'c':
        color = []
        
        if len(sys.argv)>3:
            target = sys.argv[3]
            num = len(set(df[target]))
            for i in range(num):
                color.append('#%06X' % randint(0, 0xFFFFFF))
            rgb = []
            for i in range(len(df[target].to_numpy())):
                rgb.append(color[int(df[target].to_numpy()[i])])
        else:
            try:
                target = X[:,-1]
            except:
                pass
            try:
                target = X
                num = len(set(X[:,-1]))
                for i in range(num):
                    color.append('#%06X' % randint(0, 0xFFFFFF))
                rgb = color[target]
            except:
                pass
            
        

        


else:
    (m,n) = X.shape
    rgb = np.c_[np.zeros(m), np.zeros(m), np.ones(m)]
X = X[:,0:-1]
Y = X
np.random.seed(5)

fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
pca = decomposition.PCA(n_components=3)
pca2 = decomposition.PCA(n_components=2)
pca2.fit(Y)
pca.fit(X)
X = pca.transform(X)
Y = pca2.transform(Y)
# Reorder the labels to have colors matching the cluster results
#for i in range(X.shape[0]):
ax.scatter(X[:, 0], X[:, 1], X[:, 2],color = rgb, cmap=plt.cm.nipy_spectral,
           edgecolor='k')

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])


plt.show()

plt.scatter(Y[:,0], Y[:,1], c = rgb)
plt.show()