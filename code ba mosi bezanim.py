import numpy as np
w =  np.array([[1.], [2]])
b = 1.5
X = np.array([[1., -2., -1.], [3., 0.5, -3.2]])
Y = np.array([[1, 1, 0]])
m = X.shape[1]
A = 1/(1+np.exp(-(np.dot(w.T, X)+b)))
cost = -1/m*np.sum(Y*np.log(A) + (1-Y)*np.log(1-Y))
    