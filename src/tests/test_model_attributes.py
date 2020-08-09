# -*- coding: utf-8 -*-
import unittest
import models.attributes as attrs


class TestModelAttributes(unittest.TestCase):
    def setUp(self):
        pass

    def test_id_create(self):
        id_ = attrs.ID(0)
        self.assertEqual(0, id_.attr)

    def test_name_create(self):
        name = attrs.Name('競走馬名')
        self.assertEqual('競走馬名', name.attr)
