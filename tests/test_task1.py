#!/usr/bin/env python

import pytest

from task1.solution import parse_time


@pytest.mark.parametrize(
    "input, expected_output",
    [("30", 30), ("30s", 30), ("s", 1), ("60.5m", 3630), ("0.0s", 0)],
)
def test_parse_time(input, expected_output):
    assert parse_time(input) == expected_output


@pytest.mark.parametrize("input", ["10seconds", "1y", "", ".123s", "1.m", "10ss", "mm"])
def test_parse_time_error(input):
    with pytest.raises(RuntimeError):
        parse_time(input)
