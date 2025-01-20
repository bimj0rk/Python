#%%
import tensorflow as tf
import tf_keras
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tf_keras import layers
from tf_keras.models import Sequential
from sklearn.metrics import confusion_matrix
from tf_keras.optimizers import Adam
from tf_keras.regularizers import l2

tf.keras.backend.clear_session()

gpu_devices = tf.config.list_physical_devices('GPU')
if gpu_devices:
  tf.config.experimental.set_memory_growth(gpu_devices[0], True)
  print('GPU found', gpu_devices[0])
else:
  print('No GPU found')

#define image size
IMG_SIZE = 224

#define batch size
BATCH_SIZE = 64

#training directory
TRAINING_DIR = "Train"
  
#training split
train_ds = tf_keras.utils.image_dataset_from_directory(
  TRAINING_DIR,
  labels = "inferred",
  image_size = (IMG_SIZE, IMG_SIZE),
  batch_size = BATCH_SIZE,
  subset = "training",
  validation_split = 0.25,
  shuffle = True,
  seed = 225
)

#validation split, taken directly from the same directory as train
validation_ds = tf_keras.utils.image_dataset_from_directory(
  TRAINING_DIR,
  labels = "inferred",
  image_size = (IMG_SIZE, IMG_SIZE),
  batch_size = BATCH_SIZE,
  subset = 'validation',
  validation_split = 0.25,
  shuffle = True,
  seed = 225
)

CLASS_NAMES = train_ds.class_names

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size = AUTOTUNE)
val_ds = validation_ds.cache().prefetch(buffer_size = AUTOTUNE)

#data augmentation to increase robustness
data_augmentation = Sequential([
  layers.experimental.preprocessing.RandomFlip('horizontal'),
  layers.experimental.preprocessing.RandomRotation(0.2),
  layers.experimental.preprocessing.RandomZoom(0.2) 
])

train_ds = train_ds.map(lambda x, y: (data_augmentation(x, training = True), y))

#normalizing and augmenting the data
norm_layer = layers.Rescaling(1./255)
train_ds = train_ds.map(lambda x, y: (norm_layer(x), y))
validation_ds = validation_ds.map(lambda x, y: (norm_layer(x), y))

num_classes = len(CLASS_NAMES)

#training model
model = Sequential([
  layers.Conv2D(64, (3, 3), input_shape = (224, 224, 3)),
  layers.Activation('relu'),
  layers.MaxPooling2D(2, 2),
  layers.Conv2D(64, (3, 3)),
  layers.Activation('relu'),
  layers.MaxPooling2D(2, 2),
  layers.Conv2D(128, (3, 3)),
  layers.Activation('relu'),
  layers.MaxPooling2D(2, 2),
  layers.Conv2D(128, (3, 3)),
  layers.Activation('relu'),
  layers.MaxPooling2D(2, 2),
  layers.Conv2D(256, (5, 5)), 
  layers.Activation('relu'),
  layers.MaxPooling2D(2, 2),
  layers.Conv2D(256, (3, 3)),
  layers.Activation('relu'),
  layers.MaxPooling2D(2, 2),
  layers.Flatten(),
  layers.Dense(512, activation = 'relu', kernel_regularizer = l2(0.02)),
  layers.Dropout(0.5),
  layers.Dense(num_classes, activation = 'softmax')
])

model.summary()

model.compile(optimizer = Adam(learning_rate = 0.0001, weight_decay = 1e-6), 
              loss = tf_keras.losses.SparseCategoricalCrossentropy(from_logits = True), 
              metrics = ['accuracy'])

#no of epochs
epochs = 100


#early stopping
early_stopping = tf_keras.callbacks.EarlyStopping(monitor = 'val_loss', 
                                                  mode = 'min', 
                                                  verbose = 1, 
                                                  patience = 7, 
                                                  restore_best_weights = True)
                                       

#class weights since the dataset is imbalanced
class_weights = {
    0: 0.657,  #bike
    1: 1.165,  #bus
    2: 1.006,  #cng
    3: 0.885,  #easy bike
    4: 1.385,  #hatchback
    5: 1.296,  #mpv
    6: 2.689,  #pickup
    7: 0.695,  #sedan
    8: 1.117,  #suv
    9: 0.770   #truck
}


#fitting of the model
history = model.fit(train_ds, 
                    validation_data = validation_ds, 
                    epochs = epochs,
                    class_weight = class_weights,
                    callbacks = [early_stopping])

#accuracy and loss values
accuracy = history.history['accuracy']
val_accuracy = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

true_labels = []
predicted_labels = []

for images, labels in val_ds:
  true_labels.extend(labels.numpy())
  pred = model.predict(images)
  predicted_labels.extend(np.argmax(pred, axis = 1))

confusion_matrix = confusion_matrix(true_labels, predicted_labels)

print('Confusion Matrix: ')
plt.figure(figsize=(8, 8))
sns.heatmap(confusion_matrix, annot = True, fmt = 'd', xticklabels = CLASS_NAMES, yticklabels = CLASS_NAMES, cmap = 'Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')

score = model.evaluate(validation_ds, verbose = 0)
print('Validation loss:', score[0])
print('Validation accuracy:', score[1])

plt.figure(figsize = (8, 8))
plt.subplot(1, 2, 1)
plt.plot(accuracy, label = 'Training Accuracy')
plt.plot(val_accuracy, label = 'Validation Accuracy')
plt.legend(loc = 'lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(loss, label = 'Training Loss')
plt.plot(val_loss, label = 'Validation Loss')
plt.legend(loc = 'upper right')
plt.title('Training and Validation Loss')
plt.show()
# %%