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
        horse = models.Horse({
            'id': id_,
            'name': name,
        })
        self.assertEqual(id_.attr, horse.id)
        self.assertEqual(name.attr, horse.name)

    def test_create_jockey(self):
        id_ = attrs.ID(0)
        name = attrs.Name('騎手名')
        jockey = models.Jockey({
            'id': id_,
            'name': name,
        })
        self.assertEqual(id_.attr, jockey.id)
        self.assertEqual(name.attr, jockey.name)
