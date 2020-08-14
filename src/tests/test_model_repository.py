# -*- coding: utf-8 -*-
import unittest
import models
import models.repos as repos
import models.attributes as attrs


class TestModelRepository(unittest.TestCase):
    def setUp(self):
        pass

    def test_horse_repo(self):
        id_ = attrs.ID(0)
        name = attrs.Name('競走馬名')
        birthday = attrs.Birthday('2000年1月1日')
        horse = models.Horse(
            id_=id_,
            name=name,
            birthday=birthday,
        )
        horse_repo = repos.HorseRepository()
        horse_repo.store(horse)
        self.assertEqual([horse], horse_repo.find(0))

    def test_jockey_repo(self):
        id_ = attrs.ID(0)
        name = attrs.Name('騎手名')
        jockey = models.Jockey(
            id_=id_,
            name=name,
        )
        jockey_repo = repos.JockeyRepository()
        jockey_repo.store(jockey)
        self.assertEqual([jockey], jockey_repo.find(0))
