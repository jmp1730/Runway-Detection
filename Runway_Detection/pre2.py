from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.utils import to_categorical
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
import os
from tensorflow.keras.callbacks import ModelCheckpoint

imagePaths = list(paths.list_images('NWPU-RESISC45'))
data = []
labels = []

print(len(imagePaths))

# loop over the image paths
c=0
for imagePath in imagePaths:
    label = imagePath.split(os.path.sep)[-2]
    print(label)
    # if label!='runway':
    #     label='other'
    image = cv2.imread(imagePath)
    image = cv2.resize(image, (150, 150))
    # update the data and labels lists, respectively
    data.append(image)
    labels.append(label)
    c+=1
    #print(c,end='')

data = np.array(data, dtype="float16") / 255.0
# encode the labels (which are currently strings) as integers and then
# one-hot encode them
le = LabelEncoder()
labels = le.fit_transform(labels)
labels = to_categorical(labels, 36)

import pickle

pickle_out = open("le.pickle","wb")
pickle.dump(le, pickle_out)
# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainX, testX, trainY, testY) = train_test_split(data, labels,
	test_size=0.25, random_state=42) 

from resnet50 import build_model

aug = ImageDataGenerator(
		rotation_range=20,
		zoom_range=0.15,
		width_shift_range=0.2,
		height_shift_range=0.2,
		shear_range=0.15,
		horizontal_flip=True,
		fill_mode="nearest")   

INIT_LR = 1e-3
BS = 16
EPOCHS = 25     
opt = SGD(lr=INIT_LR, momentum=0.9, decay=INIT_LR / EPOCHS)
model=build_model()
model.compile(loss="categorical_crossentropy", optimizer=opt,
	metrics=["accuracy"])
# train the network
checkpointer = ModelCheckpoint(filepath='model1.h5', verbose=1, save_best_only=True ,monitor='val_accuracy')
print("[INFO] training network for {} epochs...".format(EPOCHS))
H = model.fit(
	x=aug.flow(trainX, trainY, batch_size=BS),
	validation_data=(testX, testY),callbacks=[checkpointer],
	steps_per_epoch=len(trainX) // BS,
	epochs=EPOCHS)  

#model.save('detect_model.md')
print('model saved')

model_json = model.to_json()
with open("model1.json", "w") as json_file:
    json_file.write(model_json)  


predictions = model.predict(x=testX.astype("int8"), batch_size=BS)
print(classification_report(testY.argmax(axis=1),
	predictions.argmax(axis=1), target_names=le.classes_))
# plot the training loss and accuracy
N = np.arange(0, EPOCHS)
plt.style.use("ggplot")
plt.figure()
plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, H.history["accuracy"], label="train_acc")
plt.plot(N, H.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy on Dataset")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc="lower left")
plt.savefig('training.png')
