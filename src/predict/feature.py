import json
import glob
import numpy as np
import sklearn.preprocessing


def preprocessing(race, n_race_features=3, n_horse_features=7, n_horses=21):
    result = []

    # レース情報
    result.append(['芝', 'ダート'].index(race['馬場状態'].attr))
    result.append(race['走距離'].attr)
    result.append(['晴', '曇', '雨'].index(race['天気'].attr))

    # 競走馬情報
    for horse in race['競走馬']:
        result.append(horse['馬番'])
        result.append(['牡', '牝', 'セ'].index(horse['性別']))
        result.append(horse['年齢'])
        result.append(horse['斤量'])
        result.append(horse['オッズ'])
        result.append(horse['体重'])
        result.append(horse['体重増減'])

    fill = np.zeros(n_horses*n_horse_features + n_race_features - len(result))
    result.extend(fill)

    return np.array(result).reshape((150))
