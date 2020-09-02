# -*- coding: utf-8 -*-
import unittest
import model
import model.attribute as attrs
import repository as repo
from util.attr_util import AttrUtil
from util.model_util import ModelUtil


class TestModel(unittest.TestCase):
    def setUp(self):
        self.horse_repo = repo.Repository(model.Horse)
        self.jockey_repo = repo.Repository(model.Jockey)

    def attrs(self):
        return AttrUtil

    def create_horse(self):
        return ModelUtil.create_horse(self.attrs())

    def create_jockey(self):
        return ModelUtil.create_jockey(self.attrs())

    def test_create_horse(self):
        horse = self.create_horse()
        self.assertEqual(self.attrs().id.attr, horse.id)

    def test_create_jockey(self):
        jockey = self.create_jockey()
        self.assertEqual(self.attrs().id.attr, jockey.id)

    def test_equals(self):
        horse1 = self.create_horse()
        horse2 = self.create_horse()
        self.assertTrue(horse1.equals(horse2))

    def test_horse_repo(self):
        horse = self.create_horse()
        self.horse_repo.store(horse)
        self.assertEqual([horse], self.horse_repo.find(0, 'id'))

    def test_jockey_repo(self):
        jockey = self.create_jockey()
        self.jockey_repo.store(jockey)
        self.assertEqual([jockey], self.jockey_repo.find(0, 'id'))
