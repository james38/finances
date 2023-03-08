import datetime as dt

from Agreement import Agreement


class Account(Agreement):
    """Account class
    input: account holder name
      institution counterparty name
      amount in the account
      when the account was created
    """
    def __init__(self, holder, institution, amount, opened=dt.datetime.now()):
        super().__init__(
            name=f"{institution} account",
            parties=[holder, institution],
            actions=["hold"],
            when=opened,
        )
        self.dollars = amount


    def increase(self, amount):
        self.dollars += amount


    def decrease(self, amount):
        self.dollars -= amount
