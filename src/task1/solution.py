#!/usr/bin/env python

import re

# Map of time units to seconds
TIME_MAP = {"s": 1, "m": 60, "h": 3600, "d": 86400}


def parse_time(time_delta: str) -> int:
    """
    Main function for parsing time
    """
    if not _validate_input(time_delta):
        raise RuntimeError("Invalid input")

    search_result = re.search(r"(\d+(?:\.\d+)?)?(\w)?", time_delta)
    number, time_unit = search_result.groups()

    # setting up default values if they are not present in string
    if number is None:
        number = 1
    else:
        number = float(number)

    if time_unit is None:
        time_unit = "s"

    # Not 100% mathimatical rounding(bankers rounding)
    return round(number * TIME_MAP[time_unit])


def _validate_input(time_delta: str) -> bool:
    """
    Separate function for input validation.

    Returns(bool):
        True if input is valid. False otherwise.
    """
    if len(time_delta) == 0:
        return False

    if re.match(r"(\d+(\.\d+)?)?[smhd]?$", time_delta) is None:
        return False

    return True
