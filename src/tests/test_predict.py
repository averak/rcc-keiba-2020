import unittest
import datetime
import numpy as np
import model.attribute as attrs
from extractor import RaceExtractor
from predict.feature import preprocessing
from predict.nnet import build_nnet


class TestPredict(unittest.TestCase):
    def setUp(self):
        self.nnet = self.build_nnet()

        race_extractor = RaceExtractor(attrs)
        race_id = '202004020501'
        self.sample_data = race_extractor.fetch_race_data(
            attrs.RaceID(race_id))

    def build_nnet(self):
        nnet = build_nnet(150)
        nnet.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'],
        )
        nnet.load_weights('predict/model.h5')

        return nnet

    def feature(self, data):
        return preprocessing(data)

    def test_preprocessing(self):
        feature = self.feature(self.sample_data)
        self.assertEqual(150, len(feature))
        for x in feature:
            self.assertIsInstance(x, np.float64)

    def test_predict(self):
        feature = self.feature(self.sample_data)
        pred = self.nnet.predict(np.array([feature]))
        self.assertEqual(21, len(pred[0]))
