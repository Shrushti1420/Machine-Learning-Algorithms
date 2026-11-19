from sklearn.neighbors import KNeighborsClassifier

# Training data
X = [[1], [2], [3], [6], [7], [8]]
y = [0, 0, 0, 1, 1, 1]

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[5]])

print("Predicted Class:", prediction[0])
