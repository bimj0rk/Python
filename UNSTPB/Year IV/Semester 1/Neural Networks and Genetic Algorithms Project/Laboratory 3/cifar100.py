from tf_keras.datasets import cifar100
from tf_keras.models import Sequential
from tf_keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Activation, Dropout
from tf_keras.losses import categorical_crossentropy
from tf_keras.optimizers import Adam
from tf_keras.utils import to_categorical
from tf_keras.callbacks import EarlyStopping
from tf_keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np

(xTrain, yTrain), (xTest, yTest) = cifar100.load_data()

#normalization
xTrain = xTrain.astype('float32')/255
xTest = xTest.astype('float32')/255

nb_classes = len(np.unique(yTrain))

input_shape = (32, 32, 3) #img width and height, no_channels

yTrain = to_categorical(yTrain, nb_classes)
yTest = to_categorical(yTest, nb_classes)

'''
build the fucking model idk what these do google it
features: normalization (up, mandatory for images), dropout (kill some of the neurons and see if the other neurons 
have information to be learned, if not, overfitting), 
new transfer functions, fully connected layers(softmax), pooling
'''

model = Sequential()

model.add(Conv2D(128, (3, 3), paddin = 'same', input_shape = xTrain.shape[1:]))
model.add(Activation('elu'))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('elu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(256, (3, 3), padding = 'same'))
model.add(Activation('elu'))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('elu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(512, (3, 3), padding = 'same'))
model.add(Activation('elu'))

model.add(Conv2D(512, (3, 3)))
model.add(Activation('elu'))    
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('elu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.summary()
model.compile(loss = categorical_crossentropy, optimizer = Adam(learning_rate = 0.0001, decay = 1e-6), metrics = ['accuracy'])

datagen = ImageDataGenerator(
    featurewise_center = False,
    samplewise_center = False,
    featurewise_std_normalization = False,
    samplewise_std_normalization = False,
    zca_whitening = False,
    rotation_range = 0,
    width_shift_range = 0.1,
    height_shift_range = 0.1,
    horizontal_flip = True,
    vertical_flip = False
)

datagen.fit(xTrain)

earlyStop = EarlyStopping(
    monitor = 'val_loss',
    mode = 'min',
    verbose = 1,
    patience = 8,
    restore_best_weights = True
)

history = model.fit(datagen.flow(xTrain, yTrain, batch_size = 50),
                    steps_per_epoch = xTrain.shape[0] // 50,
                    epochs = 600,
                    validation_data = (xTest, yTest),
                    verbose = 1,
                    callbacks = [earlyStop])

score = model.evaluate(xTest, yTest, verbose = 0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

plt.plot(history.history['val_loss'])
plt.title('Validation loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

plt.plot(history.history['val_accuracy'])
plt.title('Validation accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()

evaluation = model.evaluate(datagen.flow(xTest, yTest, batch_size = 50), steps = xTest.shape[0])
print('Model accuracy: ', evaluation[1])