import itertools
from collections import namedtuple

Coord = namedtuple("Coord", "x y")

def get_players():
    return ["Aaron", "Ezra", "Dave", "Jeff", "Sandra", "Freya"]


_LAYOUT = []
_DIMS = [0, 0]


def init(board, layout):
    x, y = layout['dims']
    x, y = x * 2, y * 2
    _DIMS[0] = x - 1
    _DIMS[1] = y - 1
    coords = layout['coords']
    node_pos = {}
    for _ in range(y):
        _LAYOUT.append([None] * x)
    for (x, y), node_name in coords.items():
        x, y = x * 2, y * 2
        _LAYOUT[y][x] = node_name
        node_pos[node_name] = Coord(x, y)
    for path in board._paths:
        node_names = [nod.name for nod in path.nodes]
        a_pos, b_pos = [node_pos[name] for name in node_names]
        x = (a_pos.x + b_pos.x) // 2
        y = (a_pos.y + b_pos.y) // 2
        path_type = "uphill path"
        if a_pos.x == b_pos.x:
            path_type = "vertical path"
        elif a_pos.y == b_pos.y:
            path_type = "horizontal path"
        elif a_pos.x < b_pos.x and a_pos.y < b_pos.y:
            path_type = "downhill path"
        elif a_pos.x > b_pos.x and a_pos.y > b_pos.y:
            path_type = "downhill path"
        assert _LAYOUT[y][x] is None, "Can't place a path on a node, {}".format(node_names)
        _LAYOUT[y][x] = path_type


def announce_round(round_no):
    print("\n\nRound {}!\n\n".format(round_no))


def get_moves(board):
    active_players = board.get_active_players()
    done_players = set()
    moves = []
    while len(active_players) > 0:
        for player in active_players:
            announce_player(player)
            display_board(player, board)
            from_node, to_node = get_action(player, board)
            if from_node is None:
                done_players.add(player)
            else:
                moves.append((from_node, to_node))
        active_players = {player for player in active_players if player not in done_players}
    return moves


def announce_player(player):
    print("{}'s turn!\n".format(player.name))


def display_board(player, board):
    board_strs = []
    for _ in range(_DIMS[1]):
        board_strs.append(["   \n . \n   "] * _DIMS[0])
    names_to_nodes = {node.name: node for node in board.get_nodes()}
    for y, x in itertools.product(range(_DIMS[1]), range(_DIMS[0])):
        chooser = _LAYOUT[y][x]
        if chooser in names_to_nodes:
            board_strs[y][x] = _draw_node(names_to_nodes[chooser])
        elif chooser == "downhill path":
            board_strs[y][x] = "\\  \n \\ \n  \\"
        elif chooser == "vertical path":
            board_strs[y][x] = " | \n | \n | "
        elif chooser == "horizontal path":
            board_strs[y][x] = "   \n---\n   "
        elif chooser == "uphill path":
            board_strs[y][x] = "  /\n / \n/  "
    for cells in board_strs:
        prints = []
        for i in range(3):
            prints.append("".join([cell.split("\n")[i] for cell in cells]))
        print("\n".join(prints))


def _draw_node(node):
    nom = "/{}\\".format(node.name[0])
    mstr = node.player.name[:3] if node.occupied else "| |"
    pwr = "\\{}/".format(node.power)
    return "{}\n{}\n{}".format(nom, mstr, pwr)


def get_action(player, board):
    from_nodes = board.get_nodes(player)
    from_node = forced_item_input("node to move: ", from_nodes, allow_blank=True)
    if from_node == "":
        return None, None
    to_nodes = [path[from_node] for path in from_node.paths]
    to_node = forced_item_input("move to:", to_nodes, allow_blank=True)
    if to_node == "":
        return None, None
    return from_node, to_node


def forced_item_input(prompt, nodes, allow_blank=False):
    node_names_to_node = {node.name: node for node in nodes}
    node_names_to_node[""] = ""
    ipt = None
    while ipt != "" and ipt not in nodes:
        ipt = input(prompt)
        if ipt not in node_names_to_node:
            print("Received '{}', expected one of '{}'".format(ipt, "', '".join(node_names_to_node.keys())))
        else:
            ipt = node_names_to_node[ipt]
    return ipt
