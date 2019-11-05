class Path:
    def __init__(self, node_a, node_b):
        self._map = {node_a: node_b,
                     node_b: node_a}
        node_a.add_path(self)
        node_b.add_path(self)

    def __getitem__(self, item):
        return self._map[item]

    @property
    def nodes(self):
        return self._map.keys()
