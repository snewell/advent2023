#!/usr/bin/python3

import aoc
import re

_DIGIT_PATTERN = re.compile(r"[a-z]*([1-9])(?:.*([1-9]))?")
_WORD_DIGIT_SUBPATTERN = r"((?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)|[1-9])"
_WORD_DIGIT_PATTERN = re.compile(
    f"{_WORD_DIGIT_SUBPATTERN}(?:.*{_WORD_DIGIT_SUBPATTERN})"
)

_vals = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def _get_val(val):
    ret = _vals.get(val, None)
    if ret:
        return ret
    return int(val)


def _a(reader):
    sum = 0
    line = reader.readline()
    while line:
        m = _DIGIT_PATTERN.search(line)
        if m:
            first = m.group(1)
            second = m.group(2)
            if not second:
                second = first
            val = int(first) * 10 + int(second)
            sum += val
        line = reader.readline()
    return sum


def _b(reader):
    sum = 0
    line = reader.readline()
    while line:
        m = _WORD_DIGIT_PATTERN.search(line)
        if m:
            first = m.group(1)
            second = m.group(2)
            if not second:
                second = first
            val = (_get_val(first) * 10) + _get_val(second)
            sum += val
        line = reader.readline()
    return sum


aoc.load((_a, _b))
