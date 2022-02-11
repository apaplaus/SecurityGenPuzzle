#!/usr/bin/env python

import pytest

from task3.solution import merge


@pytest.mark.parametrize(
    "iterables, expected_out",
    [
        ([[1, 5, 9], [2, 5], [1, 6, 10, 11]], [1, 1, 2, 5, 5, 6, 9, 10, 11]),
        ([[1], [1]], [1, 1]),
        ([[99999], [-100000]], [-100000, 99999]),
    ],
)
def test_merge(iterables, expected_out):
    output = merge(*iterables)
    assert output == expected_out
