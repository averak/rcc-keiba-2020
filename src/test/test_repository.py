import unittest
import repository as repo


class TestModel(unittest.TestCase):
    def setUp(self):
        self.jockey_repo = repo.JockeyRepository()

    def test_jockey_repo(self):
        if self.jockey_repo == []:
            return

        jockey = self.jockey_repo[0]
        self.assertEqual([jockey], self.jockey_repo.find(jockey.id))
        self.assertEqual([jockey], self.jockey_repo.find(
            jockey.name, attr='name'))
