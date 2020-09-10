import tensorflow.keras.layers as layers
from tensorflow.keras import Model


def build_nnet(input_shape, n_class=21):
    # input layer
    input_layer = layers.Input(shape=input_shape)

    # hidden layer
    x1 = layers.Dense(64, activation='relu')(input_layer)
    x1 = layers.Dropout(0.1)(x1)
    x2 = layers.Dense(128, activation='relu')(x1)
    x2 = layers.Dropout(0.4)(x2)
    x3 = layers.Dense(256, activation='relu')(x2)
    x3 = layers.Dropout(0.4)(x3)

    # output layer
    y = layers.Dense(n_class, activation='softmax')(x3)

    return Model(inputs=input_layer, outputs=y)
