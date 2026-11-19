from sklearn.linear_model import Perceptron

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

model = Perceptron()

model.fit(X, y)

prediction = model.predict([[1, 1]])

print("Predicted Class:", prediction[0])
