from Entity import Entity


class Employer(Entity):
    """
    Employer class for companies that offer Jobs.
    """
    def __init__(self, name, founded=None):
        super().__init__(name, founded)
