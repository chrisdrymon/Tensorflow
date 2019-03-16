import tensorflow as tf
import numpy as np
from tensorflow.keras import layers

print(tf.VERSION)
print(tf.keras.__version__)

model = tf.keras.Sequential([
    layers.Dense(10, activation='relu', input_shape=(3,)),
    layers.Dense(10, activation='relu'),
    layers.Dense(3, activation='softmax')])

model.compile(optimizer=tf.train.AdamOptimizer(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#train_samples = np.array([[4, 3, 1], [3, 7, 0], [9, 2, 1], [8, 3, 2]])

dayDict = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
classDict = {'Druid': 0, 'Hunter': 1, 'Mage': 2, 'Paladin': 3, 'Priest': 4, 'Rogue': 5, 'Shaman': 6,\
             'Warlock': 7, 'Warrior': 8}

train_samples = np.array([['Tuesday', 'Paladin', 71.8], ['Tuesday', 'Rogue', 72.7], ['Tuesday', 'Warrior', 71.1], \
                 ['Wednesday', 'Mage', 69.4]])
y_binary = tf.keras.utils.to_categorical(['Tuesday'])
train_labels = np.array(y_binary)
print(train_labels)

#model.fit(x=train_samples, y=train_labels, batch_size=4, epochs=10, shuffle=True)
