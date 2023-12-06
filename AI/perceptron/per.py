import numpy as np

X1 = np.array([2,1,-1])
X2 = np.array([0,-1,-1])
# X3 = np.array([-1, 1, 0.5])

X = np.array([X1, X2])
W = np.array([0, 1, 0])

d = np.array([-1, 1])

c = 1
epochs = 2

for i in range(epochs):
    print(f'Iteration : {i}')
    for j in range(len(X)):
        net = np.dot(X[j],W)
        
        if net<0:
            op = -1
        elif net>=0:
            op = 1
        
        error = d[j]-op
        delW = c*error*X[j]
        W+=delW
        print("W", j,  W)
    