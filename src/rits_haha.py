#!/usr/bin/env python
import time
import tqdm
import datetime
import numpy as np
import model.attribute as attrs
import model
from model import Horse
from model import Race
from extractor import RaceExtractor
from predict.nnet import build_nnet
from predict.feature import preprocessing
from post import Guide, Poster

# build nnet
nnet = build_nnet(150)
nnet.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'],
)
nnet.load_weights('predict/model.h5')

# fetch today's race id list
race_extractor = RaceExtractor(attrs, model)
race_id_list = race_extractor.fetch_race_id_list()

# predict & post to twitter!
for race_id in tqdm.tqdm(race_id_list):
    race_data = race_extractor.fetch_race_data(race_id)

    if race_data is None:
        continue

    # predict
    feature = preprocessing(race_data)
    pred = nnet.predict(np.array([feature]))

    winner_index = np.argmax(pred[0])
    if winner_index >= len(race_data.horses):
        winner_index = len(race_data.horses) - 1

    # post to twitter
    guide = Guide()
    text = guide.construct(
        race_data, race_data.horses[winner_index], pred[0][winner_index] * 5.0)
    try:
        Poster.publish(text)
    except Exception as e:
        print(e)

    time.sleep(3)
