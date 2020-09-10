import json
import glob
import numpy as np
import sklearn.preprocessing


def preprocessing(race, n_race_features=3, n_horse_features=7, n_horses=21):
    result = []

    # レース情報
    result.append(['芝', 'ダート'].index(race.field.attr))
    result.append(race.distance.attr)
    result.append(['晴', '曇', '雨'].index(race.weather.attr))

    # 競走馬情報
    for race_horse in race.horses:
        result.append(race_horse.number.attr)
        #result.append(['牡', '牝', 'セ'].index(race_horse['性別']))
        result.append(0) # fixme : sex
        result.append(race_horse.age.attr)
        result.append(race_horse.load.attr)
        result.append(race_horse.odds.attr)
        result.append(race_horse.weight.attr)
        result.append(race_horse.weight_change.attr)

    fill = np.zeros(n_horses*n_horse_features + n_race_features - len(result))
    result.extend(fill)

    return np.array(result).reshape((150))
