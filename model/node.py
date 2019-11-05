class Node:
    def __init__(self, name, player=None, power=1):
        self.name = name
        self.player = player
        self.power = power
        self.paths = []

    def add_path(self, path):
        self.paths.append(path)

    @property
    def occupied(self):
        return self.player is not None
