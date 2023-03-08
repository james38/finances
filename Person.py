import math

from Entity import Entity
from Account import Account
from Bank import Bank
import questions


class Person(Entity):
    """
    Person class for humans, utilizing Entity class.
    """
    def __init__(self, name, dob, sex, smoker=False):
        super().__init__(name, dob)
        self.sex = sex
        self.smoker = smoker
        self.utility = 1


    def get_utility(self, ret):
        return self.utility * math.log(ret)


    def gen_utility(self):
        qx_1 = "Would you prefer now (a) $1,000 or (b) a 10% chance of $10,000?\n"
        ans_1 = questions.ask_binary_qx(qx_1)
        return ('finish defining gen_utility')


    def initialize_bank(self, name):
        self.bank = Bank(name)
        self.checking_acct = Account(self.name, self.bank, 0)
        return None
