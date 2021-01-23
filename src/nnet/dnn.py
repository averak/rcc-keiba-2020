import tensorflow.keras.layers as layers
from tensorflow.keras import Model
from .nnet import NNET


class DNN(NNET):
    def _make(self, input_shape, n_class):
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

        result = Model(inputs=input_layer, outputs=y)
        if self.weight_exists:
            result.load_weights(self.weight_path)
        return result

    def _compile(self):
        self.nnet.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'],
        )
