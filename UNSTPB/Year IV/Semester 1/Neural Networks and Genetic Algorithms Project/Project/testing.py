import tensorflow as tf
import tf_keras
import matplotlib.pyplot as plt
import numpy as np
from tf_keras import layers
from tf_keras.models import Sequential
from sklearn.metrics import confusion_matrix

#define image size
IMG_SIZE = 225

#define batch size
BATCH_SIZE = 64

#training directory, will also use as validation
TRAINING_DIR = "/Users/adiicmp_/Documents/Uni Shit/VSCode/Python/UNSTPB/Year IV/Semester 1/Neural Networks and Genetic Algorithms Project/Project/Train"
  
#training split
train_ds = tf_keras.utils.image_dataset_from_directory(
  TRAINING_DIR,
  labels = "inferred",
  image_size = (IMG_SIZE, IMG_SIZE),
  batch_size = BATCH_SIZE,
  validation_split = 0.2,
  subset = "training",
)

#validation split, taken directly from the same directory as train
validation_ds = tf_keras.utils.image_dataset_from_directory(
  TRAINING_DIR,
  labels = "inferred",
  image_size = (IMG_SIZE, IMG_SIZE),
  batch_size = BATCH_SIZE,
  validation_split = 0.2,
  subset = "validation",
)

CLASS_NAMES = train_ds.class_names

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size = AUTOTUNE)
val_ds = validation_ds.cache().prefetch(buffer_size = AUTOTUNE)

norm_layer = layers.Rescaling(1./255)
norm_ds = train_ds.map(lambda x, y: (norm_layer(x), y))
image_batch, labels_batch = next(iter(norm_ds))

num_classes = len(CLASS_NAMES)

#training model
model = Sequential([
  layers.Conv2D(32, (3, 3), activation = 'relu', input_shape = (225, 225, 3)),
  layers.MaxPooling2D(2, 2),
  layers.Conv2D(64, (3, 3), activation = 'relu'),
  layers.MaxPooling2D(2, 2),
  layers.Conv2D(128, (3, 3), activation = 'relu'),
  layers.MaxPooling2D(2, 2),
  layers.Flatten(),
  layers.Dense(128, activation = 'relu'),
  layers.Dropout(0.5),
  layers.Dense(num_classes, activation = 'softmax')
])

model.compile(optimizer = 'adam', loss = tf_keras.losses.SparseCategoricalCrossentropy(from_logits = True), metrics = ['accuracy'])

#no of epochs
epochs = 100

#fitting of the model
history = model.fit(train_ds, validation_data = validation_ds, epochs = epochs)

#accuracy and loss values
accuracy = history.history['accuracy']
val_accuracy = history.history[('val_accuracy')]

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

true_labels = []
predicted_labels = []

for images, labels in val_ds:
  true_labels.extend(labels.numpy())
  pred = model.predict(images)
  predicted_labels.extend(np.argmax(pred, axis=1))

confusion_matrix = confusion_matrix(true_labels, predicted_labels)

plt.figure(figsize=(8, 8))
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, accuracy, label='Training Accuracy')
plt.plot(epochs_range, val_accuracy, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()