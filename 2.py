# /usr/bin/python3

import aoc

_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def _validate_subset(ss):
    info = ss.split(",")
    for ci in info:
        ci_chunks = ci.strip().split(" ")
        limit = _LIMITS[ci_chunks[1]]
        if limit < int(ci_chunks[0]):
            return False
    return True


def _validate_game(game):
    for ss in game.split(";"):
        if not _validate_subset(ss):
            return False
    return True


def _a(reader):
    sum = 0
    line = reader.readline()
    while line:
        id_split = line.split(":")
        if _validate_game(id_split[1]):
            sum += int(id_split[0].split(" ")[1])
        line = reader.readline()
    return sum


def _game_power(game):
    counts = {}
    for ss in game.split(";"):
        info = ss.split(",")
        for ci in info:
            ci_chunks = ci.strip().split(" ")
            counts[ci_chunks[1]] = max(counts.get(ci_chunks[1], 0), int(ci_chunks[0]))
    return counts.get("red", 1) * counts.get("green", 1) * counts.get("blue", 1)


def _b(reader):
    sum = 0
    line = reader.readline()
    while line:
        id_split = line.split(":")
        power = _game_power(id_split[1])
        sum += power
        line = reader.readline()
    return sum


aoc.load((_a, _b))
