"""
3 node board like:
         P1
       / | \
     B   C   D
  /      |     \
E        F       G
|      /   \     |
H    I       J   K
|  /           \ |
P2 - M - N - O - P3
"""
from model.board import Board


def create_board(P1, P2, P3, *args):
    board = Board()
    P1 = board.get_player(P1)
    P2 = board.get_player(P2)
    P3 = board.get_player(P3)
    A = board.add_node('A', player=P1, power=2)
    L = board.add_node('L', player=P2, power=2)
    P = board.add_node('P', player=P3, power=2)
    B, C, D, E, F, G, H, I, J, K, M, N, O = board.get_empty_nodes(['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                                                                   'M', 'N', 'O'])
    board.add_paths([(A, B),
                     (A, C),
                     (A, D),
                     (B, E),
                     (C, F),
                     (D, G),
                     (E, H),
                     (F, I),
                     (F, J),
                     (G, K),
                     (H, L),
                     (I, L),
                     (J, P),
                     (K, P),
                     (L, M),
                     (M, N),
                     (N, O),
                     (O, P)
                     ])
    return board

LAYOUT = {'dims': (5, 5), 'coords': {                          (2, 4): "A",
                                                  (1, 3): "B", (2, 3): "C", (3, 3): "D",
                                     (0, 2): "E",              (2, 2): "F",              (4, 2): "G",
                                     (0, 1): "H", (1, 1): "I",              (3, 1): "J", (4, 1): "K",
                                     (0, 0): "L", (1, 0): "M", (2, 0): "N", (3, 0): "O", (4, 0): "P"}}
