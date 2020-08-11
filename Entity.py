"""
Entity class for people, objects, and institutions.
"""

import datetime as dt
from dateutil.relativedelta import relativedelta

class Entity(object):
    """docstring for Entity."""

    def __init__(self, date_birth):
        #super(Entity, self).__init__()
        self.date_birth = date_birth

    def gen_age(self):
        # return age as float given %Y/%m/%d start
        age = relativedelta(
            dt.datetime.now(),
            dt.datetime.strptime(self.date_birth, "%Y/%m/%d")
        )
        years = age.years
        months = age.months/12
        days = age.days/365.2425
        return years + months + days
