"""
Creates a simple single path 5 node board like:
P1 - O - O - O - P2
"""
from model.board import Board


def create_board(P1, P2, *args):
    board = Board()
    P1 = board.get_player(P1)
    P2 = board.get_player(P2)
    A = board.add_node('A', player=P1, power=2)
    B, C, D = board.get_empty_nodes(['B', 'C', 'D'])
    E = board.add_node('E', player=P2, power=2)
    board.add_paths([(A, B),
                     (B, C),
                     (C, D),
                     (D, E)])
    return board


LAYOUT = {'dims': (5, 1), 'coords': {(0, 0): "A", (1, 0): "B", (2, 0): "C", (3, 0): "D", (4, 0): "E"}}
