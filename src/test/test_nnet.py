import unittest
import numpy as np
from util.attr_util import AttrUtil
from util.model_util import ModelUtil
from nnet.dnn import DNN
from nnet.feature import preprocessing


class TestPredict(unittest.TestCase):
    def setUp(self):
        self.input_shape = 150
        self.n_class = 21
        self.nnet = DNN(self.input_shape, self.n_class)

        self.sample_data = ModelUtil.create_race(AttrUtil)

    def feature(self, data):
        return preprocessing(data)

    def test_preprocessing(self):
        feature = self.feature(self.sample_data)
        self.assertEqual(self.input_shape, len(feature))
        for x in feature:
            self.assertIsInstance(x, np.float64)

    def test_predict(self):
        feature = self.feature(self.sample_data)
        pred = self.nnet.predict(np.array([feature]))
        self.assertEqual(self.n_class, len(pred))
