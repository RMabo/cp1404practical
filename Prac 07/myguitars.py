class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, {self.year}, ${self.cost}"

    def __lt__(self, other):
        if self.year < 50:
            return True
        else:
            return False
