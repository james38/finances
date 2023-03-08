import logging
import datetime as dt

import cfg
from Agreement import Agreement


class Job(Agreement):
    """
    Job class as an Agreement for payment between persons and companies.
    """
    def __init__(
        self, name, employer, employee, employer_actions, employee_actions,
        when=dt.datetime.now(),
    ):
        super().__init__(
            name,
            {'employer': employer, 'employee': employee},
            {'employer': employer_actions, 'employee': employee_actions},
            when,
        )
        self.employer = employer
        self.employee = employee
        self.employer_actions = employer_actions
        self.employee_actions = employee_actions


    def set_employee_pay(self, pay):
        """
        Set yearly payment.
        """
        self.employee_pay = pay
        return None


    def set_pay_schedule(self, paychecks=25):
        """
        Set number of payments per year.
        """
        self.n_paychecks = paychecks
        return None


    def gen_payments(self, env):
        while self.current:
            payment = (self.employee_pay / self.n_paychecks)
            self.employee.checking_acct.increase(payment)
            logging.info(f"{self.employer} paid {payment} to {self.employee}")
            yield env.timeout(round(cfg.DAY_YR / self.n_paychecks))
