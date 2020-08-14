# -*- coding: utf-8 -*-
import unittest
import models
import models.attributes as attrs


class TestModel(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_horse(self):
        id_ = attrs.ID(0)
        name = attrs.Name('競走馬名')
        birthday = attrs.Birthday('2000年1月1日')
        horse = models.Horse(
            id_=id_,
            name=name,
            birthday=birthday,
        )
        self.assertEqual(id_.attr, horse.id)
        self.assertEqual(name.attr, horse.name)

    def test_create_jockey(self):
        id_ = attrs.ID(0)
        name = attrs.Name('騎手名')
        jockey = models.Jockey(
            id_=id_,
            name=name,
        )
        self.assertEqual(id_.attr, jockey.id)
        self.assertEqual(name.attr, jockey.name)

    def test_equals(self):
        id_ = attrs.ID(0)
        birthday = attrs.Birthday('2000年1月1日')
        horse1 = models.Horse(
            id_=id_,
            name=attrs.Name('競走馬1'),
            birthday=birthday,
        )
        horse2 = models.Horse(
            id_=id_,
            name=attrs.Name('競走馬2'),
            birthday=birthday,
        )
        self.assertTrue(horse1.equals(horse2))
