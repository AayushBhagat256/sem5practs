import numpy as np
X1=np.array([1,0,0,1,0,0,1,1,1])
X2=np.array([1,0,0,1,0,0,1,1,1])
X3=np.array([1,1,0,1,0,0,1,1,1])
X4=np.array([1,0,0,1,0,0,1,1,1])
X5=np.array([1,0,0,1,0,1,1,1,1])
X6=np.array([1,0,1,1,1,1,1,0,1])
X7=np.array([1,0,1,1,1,1,1,0,1])
X8=np.array([1,0,1,1,1,1,1,0,1])
X9=np.array([1,0,1,1,1,1,1,1,1])
X10=np.array([1,1,1,1,1,1,1,0,1])
XM1=np.array([1,0,0,0,1,0,0,0,1])
XM2=np.array([1,1,0,0,0,1,1,0,1])
XM3=np.array([1,1,0,0,0,1,1,0,1])
XM4=np.array([1,0,0,0,1,0,0,0,1])
XM5=np.array([1,0,0,0,1,0,0,0,1])
XM6=np.array([1,0,0,0,1,1,1,1,1])
XM7=np.array([1,0,0,0,1,1,1,1,1])
XM8=np.array([1,0,0,0,1,1,1,1,1])
XM9=np.array([1,0,0,0,1,1,1,1,1])
XM10=np.array([1,0,0,0,1,1,1,1,1])

X = np.vstack((X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, XM1, XM2, XM3, XM4, XM5, XM6, XM7, XM8, XM9, XM10))

d = np.hstack((np.ones(10), np.zeros(10)))
print(f'the d is : {d}')
# W = np.array([1, -1, 0, 0.5, 0, 1, 1, 0.5, 1])
W = np.random.randn(X.shape[1])
print(f'the w is : {W}')
c = 1
epochs = 2

for i in range(epochs):
    print("Iteration ", i + 1)
    for j in range(len(X)):
        net = np.dot(X[j], W)
        if net <= 0:
            op = 0
        else:
            op = 1
        error = d[j] - op
        dW = c * error * X[j]
        W += dW
        print("W", j, W)
    print("W after ", i + 1, " epochs ", epochs)
print("Final W after ", epochs, " epochs:")
print(W)
unknown_input = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1])
net = np.dot(unknown_input, W)
if net <= 0:
    op = "L"
else:
    op = "M"
print("Classification of unknown input: ", op)
