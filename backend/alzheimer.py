import cv2
import os
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical


image_directory = 'dataset/'
INPUT_SIZE = 64
NUM_CLASSES = 4


def load_images_from_directory(image_dir, class_label):
    images = []
    labels = []
    for image_name in os.listdir(image_dir):
        if image_name.endswith('.jpg'):
            image = cv2.imread(os.path.join(image_dir, image_name))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
            image = cv2.resize(image, (INPUT_SIZE, INPUT_SIZE))
            images.append(image)
            labels.append(class_label)
    return images, labels

classes = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
dataset = []
label = []

for class_label, class_name in enumerate(classes):
    class_images, class_labels = load_images_from_directory(os.path.join(image_directory, class_name), class_label)
    dataset.extend(class_images)
    label.extend(class_labels)

dataset = np.array(dataset)
label = np.array(label)


x_train, x_test, y_train, y_test = train_test_split(dataset, label, test_size=0.2, random_state=0)

x_train = x_train / 255.0
x_test = x_test / 255.0

y_train = to_categorical(y_train, num_classes=NUM_CLASSES)
y_test = to_categorical(y_test, num_classes=NUM_CLASSES)

model = keras.Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(INPUT_SIZE, INPUT_SIZE, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(NUM_CLASSES, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_test, y_test), shuffle=True)

model.save('ALZHEIMER.h5')