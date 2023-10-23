import tensorflow as tf
from tensorflow import keras
import numpy as np

# Create a sample dataset
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 0])

# Build an FNN model
model = keras.Sequential([
    keras.layers.Input(shape=(2,)),            # Input layer with 2 features
    keras.layers.Dense(units=4, activation='relu'),  # Hidden layer with 4 neurons and ReLU activation
    keras.layers.Dense(units=1, activation='sigmoid')  # Output layer with 1 neuron and sigmoid activation
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=1000, verbose=0)

# Evaluate the model
loss, accuracy = model.evaluate(X_train, y_train)
print(f"Loss: {loss:.4f}, Accuracy: {accuracy * 100:.2f}%")

# Make predictions
predictions = model.predict(X_train)
print("Predictions:", predictions)
