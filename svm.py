from sklearn.svm import SVC

X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

model = SVC(kernel='linear')

model.fit(X, y)

prediction = model.predict([[5]])

print("Predicted Class:", prediction[0])
