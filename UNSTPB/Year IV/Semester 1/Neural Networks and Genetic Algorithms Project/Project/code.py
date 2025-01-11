import tensorflow as tf
import tensorflow_hub as hub
import tf_keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime

labels = pd.read_csv("/type-labels.csv")
labels.head()

labels["ID"] = labels["ID"].astype(str)

filenames = ["/Train/"+ i + ".jpg" for i in labels["ID"]]

train_image_path = "/Train/"

if len(os.listdir(train_image_path)) == len(filenames):
  print("Filenames match actual amount of files!!! Proceed.")
else:
  print("Filenames do no match actual amount of files, check the target directory.")

lab_arr = labels["Type"].to_numpy()
# labels = np.array(labels) # does same thing as above

# Taking out the unique image types
unique_type = np.unique(lab_arr)
# Turn every label into a boolean array
boolean_labels = [label == unique_type for label in lab_arr]
len(boolean_labels), boolean_labels[:2]

# Define image size
IMG_SIZE = 224

# Create a function for preprocessing images
def process_image_mobilenet(image_path, img_size = IMG_SIZE):
  """
  Take am image file path and turns the image into a Tensor
  """
  # Read in an image file
  image = tf.io.read_file(image_path)
  # Turn the jpeg image into numerical Tensor with 3 colour channels (Red, Green, Blue)
  image = tf.image.decode_jpeg(image, channels=3)
  # Convert the colour channel values from 0-255 to 0-1 values
  image = tf.image.convert_image_dtype(image, tf.float32)
  # Resize the image to our desired value (224, 224)
  image = tf.image.resize(image, size=[img_size, img_size])

  return image

# Create a simple function to return a tuple (image, label)
def get_image_label(image_path, label):
  """
  Takes an image file path name and the associated label, processes the image and returns a tuple of (image, label)
  """
  image = process_image_mobilenet(image_path)
  return image, label

# Define the batch size, 32 is a good start
BATCH_SIZE = 64

# Create a function to turn data into batches
def create_data_batches(x, y = None, batch_size = BATCH_SIZE, valid_data = False, test_data = False):
  """
  Create batches of data out of image (X) and label (y) pairs.
  Shuffles the data if it's training data but doesn't shuffle if it's validation data.
  Also accepts test data as input (no labels).
  """
  # If the data is a test dataset, we probably don't have labels
  if test_data:
    print("Creating test data batches...")
    data = tf.data.Dataset.from_tensor_slices((tf.constant(x))) # only filepaths (no labels)
    data_batch = data.map(process_image_mobilenet).batch(batch_size)
    return data_batch

  # If the data is a valid dataset, we don't need to shuffle it
  elif valid_data:
    print("Creating validation data batches...")
    data = tf.data.Dataset.from_tensor_slices((tf.constant(x), # filepaths
                                               tf.constant(y))) # labels
    data_batch = data.map(get_image_label).batch(batch_size)
    return data_batch

  else:
    print("Creating training data batches...")
    # Turn filepaths and labels into Tensors
    data = tf.data.Dataset.from_tensor_slices((tf.constant(x),
                                               tf.constant(y)))
    # Shuffling pathnames and labels before mapping image processor function is faster than shuffling image
    data = data.shuffle(buffer_size=len(x))

    # Create (image, label) tuples (this also turns the image path into a preprocessed image)
    data = data.map(get_image_label)

    # Turn the training data into batches
    data_batch = data.batch(batch_size)
    return data_batch

# Setup input shape to the model
INPUT_SHAPE = [None, IMG_SIZE, IMG_SIZE, 3] # batch, height width, colour channels

# Setup output shape of our model
OUTPUT_SHAPE = len(unique_type)

# Setup model URL from TensorFLow HUB
MODEL_URL = "https://www.kaggle.com/models/google/mobilenet-v3/TensorFlow2/large-075-224-classification/1"

 # Create a function which builds a Keras model
def create_model(input_shape = INPUT_SHAPE, output_shape = OUTPUT_SHAPE, model_url = MODEL_URL):
    print("Building model with:", model)

    # Setup the model layers
    model = tf_keras.Sequential([
       hub.KerasLayer(model_url), # Layer 1 (input layer)
       tf_keras.layers.Dense(units = output_shape, activation="softmax") # Layer 2 (output layer)
    ])

    # Compile the model
    model.compile(
        loss = tf.keras.losses.CategoricalCrossentropy(),
        optimizer = tf_keras.optimizers.Adam(),
        metrics = ["accuracy"]
    )

    # Build the model
    model.build(input_shape)

    return model

# Create Model instance
model = create_model()
model.summary()

# Create a function to build a TensorBoard callback
def create_tensorboard_callback():
    # Create a log directory for storing TensorBoard logs
    logdir = os.path.join("/kaggle/working/vehicle-classification-dataset/logs",
                          # Make it so the logs get tracked whenever we run an experiment
                          datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    return tf_keras.callbacks.TensorBoard(logdir)

model_tensorboard = create_tensorboard_callback()

# Create early stopping callback
early_stopping = tf_keras.callbacks.EarlyStopping(monitor = "val_accuracy", patience = 3)

NUM_EPOCHS = 100 #@param {type:"slider", min:10, max:100, step:10}

# Create a function to save a model
def save_model(model, suffix = None):
    """
    saves a given mode in a models directory and appends a suffix (string).
    """
    # Create a model directory pathname with current time
    modeldir = os.path.join("/kaggle/working/vehicle-classification-dataset/Models",
                            datetime.datetime.now().strftime("%Y%m%d-%H%M%s"))
    model_path = modeldir + "-" + suffix + ".h5" # save format of model
    print(f"Saving model to: {model_path}...")
    model.save(model_path)
    return model_path