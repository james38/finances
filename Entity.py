"""
Entity class for people, objects, and institutions.
"""

import datetime as dt
from dateutil.relativedelta import relativedelta

MNTHS = 12
DAY_YR = 365.2425

class Entity(object):
    """Entity."""

    def __init__(self, name, dob=None):
        self.name = name
        self.dob = dob
        self.age = self.gen_age()

    def gen_age(self, now=dt.datetime.now()):
        """generate age as float, if given %Y-%m-%d start"""
        if self.dob is not None:
            age = relativedelta(
                now,
                dt.datetime.strptime(self.dob, "%Y-%m-%d")
            )
            years = age.years
            months = age.months / MNTHS
            days = age.days / DAY_YR
            return years + months + days
        else:
            return None
