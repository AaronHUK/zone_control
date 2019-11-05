from model.player import Player
from model.node import Node
from model.path import Path
from model.attack import attack


class Board:
    def __init__(self):
        self._nodes = []
        self._players = []
        self._paths = []

    def get_player(self, name):
        player = Player(name)
        self._players.append(player)
        return player

    def add_node(self, name, player=None, power=1):
        assert self.get_node_from_name(name) is None, "Attempting to add second node with name {}".format(name)
        node = Node(name, player=player, power=power)
        self._nodes.append(node)
        return node

    def get_empty_nodes(self, names):
        nodes = [Node(name) for name in names]
        self._nodes.extend(nodes)
        return nodes

    def add_paths(self, path_list):
        paths = [Path(node_a, node_b) for node_a, node_b in path_list]
        self._paths.extend(paths)
        return paths

    def move(self, from_node, to_node):
        if from_node.player == to_node.player:
            to_node.power += from_node.power
            from_node.power = 0
            return
        from_power = from_node.power
        to_power = to_node.power
        success, remainder = attack(from_power, to_power)
        if success:
            to_node.player = from_node.player
        to_node.power = remainder
        from_node.power = 0
        return success

    def next_round(self):
        for node in self._nodes:
            if node.occupied and node.power < 6:
                node.power += 1

    def get_active_players(self):
        return {node.player for node in self._nodes if node.occupied}

    def get_nodes(self, player=None):
        if player is not None:
            return [node for node in self._nodes if node.player == player]
        return self._nodes

    def get_node_from_name(self, name):
        node = None
        for i_node in self._nodes:
            if i_node.name == name:
                node = i_node
        return node
