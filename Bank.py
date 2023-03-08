from Entity import Entity


class Bank(Entity):
    """
    Bank class for financial institutions.
    """
    def __init__(self, name, founded=None):
        super().__init__(name, founded)

        self.checking = Entity(self.name)
