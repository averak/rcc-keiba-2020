import os


class NNET:
    def __init__(self, input_shape, n_class):
        # set tensorflow log level
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

        self._nnet = self._make(input_shape, n_class)
        self._compile()

    def _make(self, input_shape, n_class):
        raise Exception('サブクラスの責務')

    def _compile(self):
        raise Exception('サブクラスの責務')

    def predict(self, x):
        return self.nnet.predict(x)[0]

    def train(self, x, y, batch_size=64, epochs=20):
        self.nnet.fit(
            x,
            y,
            batch_size=batch_size,
            epochs=epochs,
            validation_split=0.1
        )

        self.nnet.save_weights(self.weight_path)

    @property
    def nnet(self):
        return self._nnet

    @property
    def weight_path(self):
        return '%s/ckpt/%s.h5' % (
            os.path.dirname(__file__),
            os.path.basename(__file__).split('.')[0]
        )

    @property
    def weight_exists(self):
        return os.path.exists(self.weight_path)
