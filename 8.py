#!/usr/bin/python3

import aoc
import re

_MAP_REGEX = re.compile(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)")


def _navigate(start, end, graph, sequence):
    step = 0
    while start != end:
        right = sequence[step % len(sequence)] == "R"
        step += 1
        start = graph[start][right]
    return step


def _a(reader):
    instructions = reader.readline().strip()
    graph = {}
    line = reader.readline()
    while line:
        m = _MAP_REGEX.match(line)
        if m:
            graph[m.group(1)] = (m.group(2), m.group(3))
        line = reader.readline()
    return _navigate("AAA", "ZZZ", graph, instructions)


def _b(reader):
    pass


aoc.load((_a, _b))
