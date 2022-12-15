import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# subplots
fig, subs = plt.subplots(4,3)

ax1 = plt.subplot(4,3,3)
ax2 = plt.subplot(4,3,4)

# creating an object and using this object to
#  extract information in data and target attributes
iris = load_iris()
data = np.array(iris['data'])
targets = np.array(iris['target'])

# a dictionary referencing the 3 classes
cd = {0:'r',1:'b',2:"g"}
cols = np.array([cd[target] for target in targets])

# plotting the first row

subs[0][0].scatter(data[:,0], data[:,1], c=cols)
subs[0][1].scatter(data[:,0], data[:,2], c=cols)
subs[0][2].scatter(data[:,0], data[:,3], c=cols)

# plotting the second row

subs[1][0].scatter(data[:,1], data[:,0], c=cols)
subs[1][1].scatter(data[:,1], data[:,2], c=cols)
subs[1][2].scatter(data[:,1], data[:,3], c=cols)

# plotting the third row

subs[2][0].scatter(data[:,2], data[:,0], c=cols)
subs[2][1].scatter(data[:,2], data[:,1], c=cols)
subs[2][2].scatter(data[:,2], data[:,3], c=cols)

# plotting the fourth row

subs[3][0].scatter(data[:,3], data[:,0], c=cols)
subs[3][1].scatter(data[:,3], data[:,1], c=cols)
subs[3][2].scatter(data[:,3], data[:,2], c=cols)

# displaying data in a graph
plt.show()
