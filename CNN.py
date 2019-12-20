import tensorflow as tf
from tensorflow import  keras
import numpy as np
import matplotlib.pyplot as plt
import dataAssemble

callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
# This callback will stop the training when there is no improvement in
# the validation loss for three consecutive epochs.

model = tf.keras.models.Sequential([# Először megadjuk a 12 konvolúciós hálózatot 2-esével illetve 3-asával összekapcsolva, poolingokkal elválasztva, majd a 3 rétegű fully connected hálózatot droput regularizációval
                                    tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu', input_shape=(256,256,3)),
                                    tf.keras.layers.Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.MaxPool2D(pool_size=(2,2), strides = (2,2)),

                                    tf.keras.layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.Conv2D(filters=128, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.MaxPool2D(pool_size=(2,2), strides = (2,2)),

                                    tf.keras.layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.MaxPool2D(pool_size=(2,2), strides = (2,2)),

                                    tf.keras.layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.MaxPool2D(pool_size=(2,2), strides = (2,2)),

                                    tf.keras.layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.Conv2D(filters=512, kernel_size=(3,3), strides=(1,1), padding = 'same', activation='relu'),
                                    tf.keras.layers.MaxPool2D(pool_size=(2,2), strides = (2,2)),

                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(4096, activation='relu'),
                                    tf.keras.layers.Dropout(0.5),
                                    tf.keras.layers.Dense(4096, activation='relu'),
                                    tf.keras.layers.Dropout(0.5),
                                    tf.keras.layers.Dense(20, activation='softmax')

])

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

steps_per_epoch = np.ceil(train_generator.samples/train_generator.batch_size) # epochonkénti lépés batch-ek alapján
val_steps_per_epoch = np.ceil(valid_generator.samples/valid_generator.batch_size)

history = model.fit(train_generator, epochs=10, verbose=1, steps_per_epoch=steps_per_epoch, validation_data=valid_generator, validation_steps=val_steps_per_epoch, callbacks = [callback])

plt.plot(history.history["acc"])
plt.plot(history.history['val_acc'])
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title("model accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.legend(["Accuracy","Validation Accuracy","loss","Validation Loss"])
plt.show()

'''model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu', input_shape=(256,256,3)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(20, activation='sigmoid')
])'''