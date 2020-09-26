from . import Repository
import model
import glob


class JockeyRepository(Repository):
    files = glob.glob('data/jockey/*.json')
    type_ = model.Jockey
