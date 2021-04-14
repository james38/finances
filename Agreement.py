"""
Agreement class between persons or institutions.
"""
from Entity import Entity

class Agreement(Entity):
    """Agreement class"""

    def __init__(self, name, parties, actions, when=dt.datetime.now()):
        super().__init__(name, when)
        self.parties = parties
        self.actions = actions
        self.current = True

    def terminate(self, end_date=dt.datetime.now()):
        self.end_date = end_date
        self.age = round(self.gen_age(end_date), 3)
        self.current = False
