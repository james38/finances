"""
Person class for humans..
"""

import datetime as dt
from dateutil.relativedelta import relativedelta

def gen_age(date_birth):
    age = relativedelta(
        dt.datetime.now(),
        dt.datetime.strptime(date_birth, "%Y/%m/%d")
    )
    years = age.years
    months = age.months/12
    days = age.days/365.2425
    return years + months + days

def ask_binary_qx(qx):
    ans = input(qx)
    if ans == "a":
        pass
    elif ans == "b":
        pass
    else:
        print("Please enter either a or b")
    return ans

class Person(object):
    """Person as individual human."""

    def __init__(self, name, sex, dob):
        #super(, self).__init__()
        self.name = name
        self.sex = sex
        self.dob = dob
        self.age = round(gen_age(dob), 3)
        self.utility = 1

    def get_utility(self, ret):
        return self.utility * log(ret)

    def gen_utility(self):
        qx_1 = "Would you prefer $1,000 today (a) or a 10% chance of $10,000 today (b)?"
        ans_1 = ""
        while !((ans_1 == "a") | (ans_1 == "b")):
            ans_1 = ask_binary_qx(qx_1)
        return ('finish defining gen_utility')
