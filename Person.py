"""
Person class for humans, utilizing Entity class.
"""
import math

from Entity import Entity
import questions

class Person(Entity):
    """Person as individual human entity."""

    def __init__(self, name, dob, sex, smoker=False):
        super().__init__(name, dob)
        self.sex = sex
        self.smoker = smoker
        self.utility = 1

    def get_utility(self, ret):
        return self.utility * math.log(ret)

    def gen_utility(self):
        qx_1 = "Would you prefer $1,000 today (a) or a 10% chance of $10,000 today (b)?\n"
        ans_1 = questions.ask_binary_qx(qx_1)
        return ('finish defining gen_utility')
