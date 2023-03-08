import datetime as dt
from dateutil.relativedelta import relativedelta


class Entity(object):
    """
    Entity class for people, objects, and institutions.
    """
    def __init__(self, name, dob=None):
        self.name = name
        self.dob = dob
        self.age = self.gen_age() if self.dob is not None else None


    def gen_age(self, from_time=None, to_time=dt.datetime.now()):
        """generate age as float, if given %Y-%m-%d start"""
        if from_time is None:
            assert self.dob is not None, "need to provide start time or set dob"
            from_time = self.dob

        if isinstance(from_time, dt.datetime):
            age = relativedelta(to_time, from_time)
        else:
            age = relativedelta(
                to_time,
                dt.datetime.strptime(from_time, "%Y-%m-%d")
            )
        years = age.years
        months = age.months / cfg.MNTHS
        days = age.days / cfg.DAY_YR

        return years + months + days
