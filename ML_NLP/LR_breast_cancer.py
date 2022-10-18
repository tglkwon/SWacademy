import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
import numpy as np

data = load_breast_cancer()
X = data.data[:,0]
Y = data.target

_X = np.c_[np.ones(len(X)), X]
theta = np.linalg.inv(_X.T.dot(_X)).dot(_X.T).dot(Y)

plt.scatter(X,Y)
plt.plot([0,30], [np.array([1,0]).dot(theta), np.array([1,30]).dot(theta)], 'r-')
plt.show()


seq_Theta = list()
Theta = np.array([-0.1, 1.1])
seq_Theta.append(Theta)
h = 0.001
for _ in range(1000):
    theta = Theta[-1]
    for x, y in zip(_X, Y):
        newtheta = theta + 2*h*(y-x.dot(theta))*x
    # Theta = np.append(Theta, (theta + h*2 * (Y-_X.dot(theta))*(X)).reshape(1,-1), axis=0)
    # Theta = np.stack((Theta, newtheta), axis=1)
    seq_Theta.append(newtheta)

# Theta