# -*- coding: utf-8 -*-
import unittest
import models
import models.attributes as attrs


class TestHorseModel(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_instance(self):
        id_ = attrs.ID(0)
        name = attrs.Name('競走馬名')
        horse = models.Horse(
            id_=id_,
            name=name,
        )
        self.assertEqual(id_.get_attr(), horse.get_id())
        self.assertEqual(name.get_attr(), horse.get_name())
