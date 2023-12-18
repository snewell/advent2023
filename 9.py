#!/usr/bin/python3

import aoc


def _get_values(line):
    vals = line.split(" ")
    ret = []
    for val in vals:
        ret.append(int(val))
    return ret


def _get_prev_next(vals):
    last = len(vals) - 1
    diffs = []
    recurse = False
    for i in range(0, last):
        diffs.append(vals[i + 1] - vals[i])
        if diffs[i] != 0:
            recurse = True
    if recurse:
        prev_diff, next_diff = _get_prev_next(diffs)
        return (diffs[0] - prev_diff), (diffs[-1] + next_diff)
    return 0, 0


def _a(reader):
    line = reader.readline()
    ret = 0
    while line:
        vals = _get_values(line)
        prev, next = _get_prev_next(vals)
        ret += vals[-1] + next
        line = reader.readline()
    return ret


def _b(reader):
    line = reader.readline()
    ret = 0
    while line:
        vals = _get_values(line)
        prev, next = _get_prev_next(vals)
        ret += vals[0] - prev
        line = reader.readline()
    return ret


aoc.load((_a, _b))
