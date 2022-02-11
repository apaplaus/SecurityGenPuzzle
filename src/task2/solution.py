#!/usr/bin/env python

from itertools import cycle

RUNNING = True


def generate_output(*files):
    # Infinite loop to cycle through files and lines
    current_file_iter = cycle(files)
    while RUNNING:
        current_file = next(current_file_iter)
        file_line = current_file.readline()
        # If last line in the file ends with 'new line',
        # go to start and read new line
        if file_line == "":
            current_file.seek(0)
            file_line = current_file.readline()
        # If last line in the file doesn't end's with the new line
        # OR if the last line of a file is empty line
        # go to the start and add new line to consumed line
        if file_line[-1] != "\n" or (len(file_line) == 1):
            current_file.seek(0)
            file_line += "\n"
        print(file_line, end="")
