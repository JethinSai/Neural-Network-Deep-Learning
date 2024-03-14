# -*- coding: utf-8 -*-
"""Assignment 6 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wAOtBoKAmLWHt8zlyGVS1JJStY4Tqpt1
"""



"""# 1. Use the use case in the class:
# a. Add more Dense layers to the existing code and check how the accuracy changes

"""

path_to_csv = '/content/diabetes.csv'

"""# New Section"""

from keras import Sequential
from keras.datasets import mnist
import numpy as np
from keras.layers import Dense
from keras.utils import to_categorical

(train_images,train_labels),(test_images, test_labels) = mnist.load_data()

print(train_images.shape[1:])
#process the data
#1. convert each image of shape 28*28 to 784 dimensional which will be fed to the network as a single feature
dimData = np.prod(train_images.shape[1:])
print(dimData)
train_data = train_images.reshape(train_images.shape[0],dimData)
test_data = test_images.reshape(test_images.shape[0],dimData)

#convert data to float and scale values between 0 and 1
train_data = train_data.astype('float')
test_data = test_data.astype('float')
#scale data
train_data /=255.0
test_data /=255.0
#change the labels frominteger to one-hot encoding. to_categorical is doing the same thing as LabelEncoder()
train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)

#creating network
model = Sequential([
    Dense(512, activation='relu', input_shape=(784,)),
    Dense(512, activation='relu'),
    # Added dense layers
    Dense(256, activation='relu'),
    Dense(256, activation='relu'),
    Dense(10, activation='softmax')
])
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, train_labels_one_hot, batch_size=256, epochs=10, verbose=1,
                   validation_data=(test_data, test_labels_one_hot))



"""# Change the data source to Breast Cancer dataset * available in the source code folder and make required
# changes. Report accuracy of the model.

"""

path_to_csv = '/content/breastcancer.csv'



from keras import Sequential
from keras.datasets import mnist
import numpy as np
from keras.layers import Dense
from keras.utils import to_categorical

(train_images,train_labels),(test_images, test_labels) = mnist.load_data()

dimData = np.prod(train_images.shape[1:])

train_data = train_images.reshape(train_images.shape[0],dimData)
test_data = test_images.reshape(test_images.shape[0],dimData)

train_data = train_data.astype('float')
test_data = test_data.astype('float')

train_data /=255.0
test_data /=255.0

train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(dimData,)))
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))  # Additional dense layer
model.add(Dense(128, activation='relu'))  # Additional dense layer
model.add(Dense(64, activation='relu'))   # Additional dense layer
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_data, train_labels_one_hot, batch_size=256, epochs=10, verbose=1,
                   validation_data=(test_data, test_labels_one_hot))



"""# Normalize the data before feeding the data to the model and check how the normalization change your accuracy"""

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
train_data_normalized = sc.fit_transform(train_data)
test_data_normalized = sc.transform(test_data)

# Continue with the rest of the code for model building and training using normalized data



import matplotlib.pyplot as plt

# Assuming 'history' is the object returned by the 'fit' method
plt.figure(figsize=(12, 5))

# Plot training & validation accuracy values
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

# Plot training & validation loss values
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.show()

# Plot one of the images from the test data
plt.imshow(test_images[0], cmap='gray')
plt.show()

# Make inference on that single image
prediction = model.predict(test_data[0].reshape(1, -1))
predicted_label = np.argmax(prediction)
print("Predicted label:", predicted_label)

model = Sequential()
model.add(Dense(512, activation='tanh', input_shape=(dimData,)))  # Change activation to tanh
model.add(Dense(512, activation='sigmoid'))  # Change activation to sigmoid
model.add(Dense(256, activation='sigmoid'))  # Additional dense layer
model.add(Dense(128, activation='sigmoid'))  # Additional dense layer
model.add(Dense(64, activation='sigmoid'))   # Additional dense layer
model.add(Dense(10, activation='softmax'))

train_data = train_images.reshape(train_images.shape[0], 784).astype('float32')
test_data = test_images.reshape(test_images.shape[0], 784).astype('float32')
# Do not scale data: omit the "/= 255.0" step

# Then compile, fit, and evaluate your model as usual