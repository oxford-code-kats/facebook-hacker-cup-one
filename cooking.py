def convert_to_sequence(num):
    return [int(digit) for digit in str(num)]


def convert_to_integer(sequence):
    return int(''.join(str(digit) for digit in sequence))


def find_last_index(sequence, number):
    reversed_sequence = list(reversed(sequence))
    last_index = reversed_sequence.index(number)
    return len(sequence) - last_index - 1

def find_first_different_index(sequence, sorted_sequence):
    for index, value in enumerate(sequence):
        if value != sorted_sequence[index]:
            return index

def find_swap_index(sequence, reverse=False):
    sorted_sequence = sorted(sequence, reverse=reverse)
    if sorted_sequence[0] != 0:
        return find_first_different_index(sequence, sorted_sequence)
    sequence = sequence[1:]
    sorted_sequence = sorted(sequence, reverse=reverse)
    index = find_first_different_index(sequence, sorted_sequence)
    if index is not None:
        return index + 1

def find_max(num):
    sequence = convert_to_sequence(num)
    swap_index = find_swap_index(sequence, reverse=True)
    if swap_index is not None:
        rest = sequence[swap_index:]
        highest = max(rest)
        index = find_last_index(sequence, highest)
        sequence[swap_index], sequence[index] = sequence[index], sequence[swap_index]
    return convert_to_integer(sequence)

def find_min(num):
    sequence = convert_to_sequence(num)
    swap_index = find_swap_index(sequence)
    if swap_index is not None:
        rest = sequence[swap_index:]
        lowest = min(rest)
        index = find_last_index(sequence, lowest)
        sequence[swap_index], sequence[index] = sequence[index], sequence[swap_index]
    return convert_to_integer(sequence)

def cook(num):
    max_num = find_max(num)
    min_num = find_min(num)
    return (min_num, max_num)