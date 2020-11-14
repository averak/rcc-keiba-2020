import unittest
from util.attr_util import AttrUtil
from util.model_util import ModelUtil


class TestModel(unittest.TestCase):
    @property
    def attrs(self):
        return AttrUtil

    def create_horse(self):
        return ModelUtil.create_horse(self.attrs)

    def create_jockey(self):
        return ModelUtil.create_jockey(self.attrs)

    def create_ped(self):
        return ModelUtil.create_ped(self.attrs)

    def create_trainer(self):
        return ModelUtil.create_trainer(self.attrs)

    def create_race(self):
        return ModelUtil.create_race(self.attrs)

    def create_race_horse(self):
        return ModelUtil.create_race_horse(self.attrs)

    def test_create_horse(self):
        horse = self.create_horse()
        self.assertEqual(
            'https://db.netkeiba.com/horse/%s' % horse.id,
            horse.url
        )

    def test_create_jockey(self):
        jockey = self.create_jockey()
        self.assertEqual(
            'https://db.netkeiba.com/jockey/%s' % jockey.id,
            jockey.url
        )

    def test_create_ped(self):
        ped = self.create_ped()
        self.assertEqual(
            'https://db.netkeiba.com/horse/ped/%s' % ped.id,
            ped.url
        )

    def test_create_trainer(self):
        trainer = self.create_trainer()
        self.assertEqual(
            'https://db.netkeiba.com/trainer/%s' % trainer.id,
            trainer.url
        )

    def test_create_race(self):
        race = self.create_race()
        self.assertEqual(
            'https://race.netkeiba.com/race/shutuba.html?race_id=%s' % race.id,
            race.url
        )

    def test_create_race_horse(self):
        race_horse = self.create_race_horse()
        self.assertEqual(
            'https://db.netkeiba.com/horse/%s' % race_horse.id,
            race_horse.url
        )

    def test_equals(self):
        horse1 = self.create_horse()
        horse2 = self.create_horse()
        self.assertTrue(horse1.__eq__(horse2))
