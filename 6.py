#!/usr/bin/python3

import aoc
import re

_LEADING_STUFF = re.compile(r"(\d+)")


def _get_line_values(line):
    return _LEADING_STUFF.findall(line)


def _get_data(reader):
    times = _get_line_values(reader.readline())
    distances = _get_line_values(reader.readline())
    return zip(times, distances)


def _find_lower_time(race_time, max_distance):
    low = 1
    high = race_time - 1
    while low < high:
        mid = low + int((high - low) / 2)
        run_time = race_time - mid
        distance = mid * run_time
        # print(f"{low} {high} {mid} {run_time} {distance}")
        if distance <= max_distance:
            low = mid + 1
        else:
            high = mid
    return low


def _find_upper_time(race_time, max_distance):
    low = 1
    high = race_time - 1
    while low < high:
        mid = low + int((high - low) / 2)
        run_time = race_time - mid
        distance = mid * run_time
        if distance > max_distance:
            low = mid + 1
        else:
            high = mid
    return low


def _a(reader):
    ret = 1
    for stime, sdistance in _get_data(reader):
        time = int(stime)
        distance = int(sdistance)
        low = _find_lower_time(time, distance)
        high = _find_upper_time(time, distance)
        possible_wins = high - low
        ret *= possible_wins
        # print(f"{time} {distance} -> {possible_wins} ({low} {high})")
    return ret


def _b(reader):
    times = _get_line_values(reader.readline())
    distances = _get_line_values(reader.readline())
    real_time = int("".join(times))
    real_distance = int("".join(distances))
    low = _find_lower_time(real_time, real_distance)
    high = _find_upper_time(real_time, real_distance)
    return high - low


aoc.load((_a, _b))
