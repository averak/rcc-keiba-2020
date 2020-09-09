from . import attribute
from . import attr_id


class RaceID(attr_id.ID):
    id_type = 'レース'
    max_digit = 12
