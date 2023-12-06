#!/usr/bin/python3

import aoc


def _make_winner_value(winning_string):
    vals = winning_string.split(" ")
    ret = 0
    for val in vals:
        if len(val) != 0:
            ret |= 1 << int(val)
    return ret


def _count_winners(winning_val, numbers):
    ret = 0
    vals = numbers.split(" ")
    for val in vals:
        if len(val) != 0:
            key = 1 << int(val)
            if (winning_val & key) != 0:
                ret += 1
    return ret


def _a(runner):
    line = runner.readline()
    ret = 0
    while line:
        ticket = line.split(":")[1].split("|")
        winning_val = _make_winner_value(ticket[0])
        win_count = _count_winners(winning_val, ticket[1])
        if win_count != 0:
            ret += 1 << (win_count - 1)
        line = runner.readline()
    return ret


def _b(runner):
    pass


aoc.load((_a, _b))
