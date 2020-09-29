"""
Agreement class between persons or institutions.
"""
from Entity import *

class Agreement(Entity):
    """docstring for Agreement class"""

    def __init__(self, entered, parties, actions, when, now=dt.datetime.now()):
        super().__init__(entered)
        self.age = round(self.gen_age(now), 3)
        self.parties = parties
        self.actions = actions
        self.when = when
        self.existent = True

    def terminate(self, end_date=dt.datetime.now()):
        self.end_date = end_date
        self.age = round(self.gen_age(end_date), 3)
        self.existent = False
