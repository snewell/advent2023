#!/usr/bin/python3

import aoc


def _get_values(line):
    vals = line.split(" ")
    ret = []
    for val in vals:
        ret.append(int(val))
    return ret


def _get_next(vals):
    last = len(vals) - 1
    diffs = []
    recurse = False
    for i in range(0, last):
        diffs.append(vals[i + 1] - vals[i])
        if diffs[i] != 0:
            recurse = True
    if recurse:
        next_diff = _get_next(diffs)
        return diffs[-1] + next_diff
    return 0


def _a(reader):
    line = reader.readline()
    ret = 0
    while line:
        vals = _get_values(line)
        next = _get_next(vals)
        ret += vals[-1] + next
        line = reader.readline()
    return ret


def _b(reader):
    pass


aoc.load((_a, _b))
