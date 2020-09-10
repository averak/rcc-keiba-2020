#!/usr/bin/env python
import time
import tqdm
import datetime
import numpy as np
import model.attribute as attrs
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
race_extractor = RaceExtractor(attrs)
race_id_list = race_extractor.fetch_race_id_list()

# predict & post to twitter!
for race_id in tqdm.tqdm(race_id_list):
    race_data = race_extractor.fetch_race_data(race_id)

    horses = []
    for horse in race_data['競走馬']:
        horses.append(
            Horse(
                id_=None,
                name=attrs.Name(horse['馬名']),
                birthday=None,
                sex=None,
                ped_id=None,
                trainer_id=None,
                wins=None,
                win_rate=None,
                rank_average=None,
                money=None,
                limb=None,
                growth=None,
                speed=None,
                breeding_center=None,
                course_suitability=None,
                distance_suitability=None,
                muddy_track_suitability=None,
                summer_suitability=None,
                winter_suitability=None,
            )
        )

    race = Race(
        id_=race_id,
        name=race_data['レース名'],
        date=None,
        weather=race_data['天気'],
        field=race_data['馬場状態'],
        turn=race_data['周回方向'],
        distance=race_data['走距離'],
        prize=race_data['賞金'],
        horses=attrs.Horses(horses),
    )

    # predict
    feature = preprocessing(race_data)
    pred = nnet.predict(np.array([feature]))

    winner_index = np.argmax(pred[0])
    if winner_index >= len(horses):
        winner_index = len(horses) - 1

    # post to twitter
    guide = Guide()
    text = guide.construct(
        race, horses[winner_index], pred[0][winner_index] * 5.0)
    try:
        Poster.publish(text)
    except Exception as e:
        print(e)

    time.sleep(3)
