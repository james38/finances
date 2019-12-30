"""
Person class for humans, utilizing Entity class.
"""
from Entity import *
import questions

class Person(Entity):
    """Person as individual human entity."""

    def __init__(self, name, sex, dob, smoker=False):
        super().__init__(dob)
        self.name = name
        self.sex = sex
        self.dob = dob
        self.smoker = smoker
        self.age = round(self.gen_age(), 3)
        self.utility = 1

    def get_utility(self, ret):
        return self.utility * log(ret)

    def gen_utility(self):
        qx_1 = "Would you prefer $1,000 today (a) or a 10% chance of $10,000 today (b)?\n"
        ans_1 = questions.ask_binary_qx(qx_1)
        return ('finish defining gen_utility')
