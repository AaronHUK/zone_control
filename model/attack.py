def attack(from_power, to_power):
    success = from_power > to_power
    big, small = max(from_power, to_power), min(from_power, to_power)
    remainder = _remainders(big, small)
    print("success {} remainder {}".format(success, remainder))
    return success, remainder


def _remainders(big, small):
    if big > small + 2:
        return big
    if big == small + 2:
        return big - 1
    if big == small + 1:
        return big - 2
    return 0
