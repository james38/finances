import datetime as dt

from Entity import Entity


class Relationship(Entity):
    """
    Relationship class for humans, utilizing Entity class.
      This Relationship class differs from the Agreement class,
       in that it doesn't have required actions.
    """
    def __init__(self, name, parties, when=dt.datetime.now()):
        super().__init__(name, when)
        self.parties = parties
        self.current = True


    def terminate(self, end_date=dt.datetime.now()):
        self.end_date = end_date
        self.age = round(self.gen_age(end_date), 3)
        self.current = False
