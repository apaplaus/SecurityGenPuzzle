#!/usr/bin/env python

import pytest
from unittest import mock
from io import StringIO

from task2.solution import generate_output


class MockFile(StringIO):
    def __init__(self, lines):
        """
        Set lines to be return by mocked file
        """
        parent = super().__init__()
        self.write("\n".join(lines))


@pytest.mark.parametrize(
    "files, inline_output",
    [
        ([MockFile(["1", "2"]), MockFile(["-"])], "1-2-1-2-1"),
        (
            [
                MockFile(["1", "2", "3"]),
                MockFile(["A", "B", "C", "D"]),
                MockFile(["-", "+"]),
            ],
            "1A-2B+3C-1D+2A-",
        ),
        (
            [
                MockFile(["\n"]),
                MockFile(["ABCD"]),
            ],
            ["\n", "ABCD", "\n"],
        ),
        ([MockFile(["\n"])], ["\n", "\n", "\n"]),
    ],
)
def test_generate_output(files, inline_output, capsys):
    # condition to make infinite loop stop
    stop_condition = len(inline_output) + 1

    # function to stop iteration and than compare the current output
    def stop_interation():
        nonlocal stop_condition
        stop_condition -= 1
        return bool(stop_condition)

    with mock.patch("task2.solution.RUNNING") as running_mock:
        # Mocking __bool__ method to control the infinite loop
        running_mock.__bool__.side_effect = stop_interation
        generate_output(*files)

    # last line should still end with \n, because we go in infinite loop
    expected_out = "\n".join(inline_output) + "\n"
    assert capsys.readouterr().out == expected_out
