#!/usr/bin/env python
import time
import tqdm
import numpy as np
import model.attribute as attrs
import model
from extractor import RaceExtractor
from nnet.dnn import DNN
from nnet.feature import preprocessing
from tweet import Tweet, Guide

# build nnet
nnet = DNN(150, 21)

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

    winner_index = np.argmax(pred)
    if winner_index >= len(race_data.horses):
        winner_index = len(race_data.horses) - 1

    # post to twitter
    guide = Guide()
    text = guide.construct(
        race_data, race_data.horses[winner_index], pred[winner_index] * 5.0)
    try:
        Tweet.publish(text)
    except Exception as e:
        print(e)

    time.sleep(3)
