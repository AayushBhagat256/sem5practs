import numpy as np

X1 = np.array([1, 0, 0, 1, 0, 0, 1, 1, 1])
X2 = np.array([1, 0, 0, 1, 0, 0, 1, 1, 1])
X3 = np.array([1, 1, 0, 1, 0, 0, 1, 1, 1])
X4 = np.array([1, 0, 0, 1, 0, 0, 1, 1, 1])
X5 = np.array([1, 0, 0, 1, 0, 1, 1, 1, 1])
X6 = np.array([1, 0, 1, 1, 1, 1, 1, 0, 1])
X7 = np.array([1, 0, 1, 1, 1, 1, 1, 0, 1])
X8 = np.array([1, 0, 1, 1, 1, 1, 1, 0, 1])
X9 = np.array([1, 0, 1, 1, 1, 1, 1, 1, 1])
X10 = np.array([1, 1, 1, 1, 1, 1, 1, 0, 1])

X = np.array([X1, X2, X3, X4, X5, X6, X7, X8, X9, X10])
W = np.array([2, -1, 0.5, 1.5,0,2,2,1.5,1])

d = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

c = 1
epochs = 3
for i in range(epochs):
    print(f"\nIteration {i + 1}")
    for j in range(len(X)):
        net = np.dot(X[j], W)

        if net <= 0:
            op = 0
        elif net > 0:
            op = 1

        error = d[j] - op

        dW = c * error * X[j]
        W += dW
        print("W", j, W)

    print(f"W after {i + 1}epochs {W}")

print(f"\nFinal W after {epochs} epochs: ")
print(W)

def test(test_data, W):
    net = np.dot(test_data, W)
    if net <= 0:
        op = 'L'
    elif net > 0:
        op = 'M'
    return op

test_data1 = np.array([1, 0, 1, 1, 1, 1, 0, 0, 0])
test_data2 = np.array([0, 1, 0, 0, 1, 0, 0, 1, 1])

print(f"\nPrediction for test data: {test_data1} which is M and model gives : ", test(test_data1,W))
print(f"Prediction for test data: {test_data2} which is L and model gives : ", test(test_data2,W))