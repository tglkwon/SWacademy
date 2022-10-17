import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
print(data.data[:,3], data.target)

import numpy as np

X = np.c_[np.ones(len(data.data)), data.data[:,3], np.power(data.data[:,3], 2),
        np.power(data.data[:,3], 3), np.power(data.data[:,3], 4), np.power(data.data[:,3], 5),]
np.hstack((np.ones(len(data.data)).reshape(-1,1), data.data[:,].reshape(-1,1)))[:3]
X.shape

theta = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(data.target))

plt.scatter(data.data[:,3], data.target)
plt.scatter(data.data[:,3], X.dot(theta), color='r')
plt.show()
