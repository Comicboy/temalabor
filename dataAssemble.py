import tensorflow as tf
from tensorflow import  keras
import numpy as np
import matplotlib.pyplot as plt

data_root=r'C:\Users\peisz\Documents\BME\Deep Learning\Temalabor\dataset'

IMAGE_SHAPE = (256, 256)
TRAINING_DATA_DIR = str(data_root)
print(TRAINING_DATA_DIR);

# Generators for training and validation images with keras.preprocessing
datagen_kwargs = dict(rescale=1./255, validation_split=.20) #20% validation data

valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
valid_generator = valid_datagen.flow_from_directory(TRAINING_DATA_DIR,subset="validation",shuffle=True,target_size=IMAGE_SHAPE) # Found 4088 images belonging to 20 classes.

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
train_generator = train_datagen.flow_from_directory(TRAINING_DATA_DIR,subset="training",shuffle=True,target_size=IMAGE_SHAPE) # Found 16393 images belonging to 20 classes.

# Creating batches for the training
image_batch_train, label_batch_train = next(iter(train_generator))
print("Image batch shape: ", image_batch_train.shape) # Image batch shape:  (32, 256, 256, 3)
print("Label batch shape: ", label_batch_train.shape) # Label batch shape:  (32, 20)

# Labels

dataset_labels = sorted(train_generator.class_indices.items(), key=lambda pair:pair[1])
dataset_labels = np.array([key.title() for key, value in dataset_labels])
print(dataset_labels) # ['Airplane' 'Bicycle' 'Bird' 'Boat' 'Bottle' 'Bus' 'Car' 'Cat' 'Chair' 'Cow' 'Dog' 'Horse' 'Motorbike' 'Person' 'Plant' 'Sheep' 'Sofa' 'Table' 'Train' 'Tv']

sample_training_images, _ = next(train_generator)

# This function will plot images in the form of a grid with 1 row and 5 columns where images are placed in each column.
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

plotImages(sample_training_images[:5])
