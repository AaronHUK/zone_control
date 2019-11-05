import display.text_display as display


def play_game(board_func, layout):
    players = display.get_players()
    board = board_func(*players)
    round_no = 1
    active_players = board.get_active_players()
    display.init(board, layout)
    while len(active_players) > 1:
        display.announce_round(round_no)
        moves = display.get_moves(board)
        combat, defence, agress, logistic = categorise_moves(moves)
        stop_moves = set()
        for categ in (combat, defence, agress, logistic):
            for from_node, to_node in categ:
                if from_node in stop_moves:
                    continue
                print("{} {} ({}) -> {} {} ({})".format(from_node.player.name if from_node.player is not None else "", from_node.name, from_node.power,
                                                        to_node.player.name if to_node.player is not None else "", to_node.name, to_node.power))
                to_captured = board.move(from_node, to_node)
                if to_captured:
                    stop_moves.add(to_node)
                print("now {} and {}".format(from_node.power, to_node.power))
        # Prep for next round
        active_players = board.get_active_players()
        board.next_round()
        round_no += 1


def categorise_moves(moves):
    agress = [move for move in moves if move[0].player != move[1].player]
    under_attack = {to_node for _, to_node in agress}
    combat = []
    for move in agress:
        for counter in agress:
            if (counter[0] == move[1] and
                counter[1] == move[0]):
                combat.append(move)
    for move in combat:
        agress.remove(move)
    defence = [move for move in moves if move[0].player == move[1].player and move[1] in under_attack]
    logistic = [move for move in moves if move not in agress and move not in defence]
    return combat, defence, agress, logistic


if __name__ == "__main__":
    from levels.test_3p import create_board, LAYOUT
    play_game(create_board, LAYOUT)
