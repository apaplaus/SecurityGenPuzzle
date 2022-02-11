#!/usr/bin/env python


def merge(*iterables):
    processed_iterables = [iter(i) for i in iterables]

    processed_numbers = []
    # Fetch one number from each iterable
    # assuming that each of them has at list one number
    for iterable in processed_iterables:
        processed_numbers.append(next(iterable))

    result = []

    while len(processed_iterables) > 0:
        min_number = min(processed_numbers)
        result.append(min_number)
        # this is index of iterable from which we need a new number
        number_index = processed_numbers.index(min_number)

        # try to get new number from iterable
        try:
            new_number = next(processed_iterables[number_index])
            processed_numbers[number_index] = new_number
        # If iterator is exhausted, remover it and it's number from lists
        except StopIteration:
            processed_iterables.pop(number_index)
            processed_numbers.pop(number_index)

    return result
