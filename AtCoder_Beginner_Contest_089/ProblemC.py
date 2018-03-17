'''input
4
ZZ
ZZZ
Z
ZZZZZZZZZZ

0

5
CHOKUDAI
RNG
MAKOTO
AOKI
RINGO

7

5
MASHIKE
RUMOI
OBIRA
HABORO
HOROKANAI

2

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


def count_initial_name(people_count: int) -> dict:
    matching_strings_count = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}

    for person in range(people_count):
        initial_name = input()[0]

        if initial_name in matching_strings_count.keys():
            matching_strings_count[initial_name] += 1

    return matching_strings_count


def count_patterns(matching_strings_count):
    import itertools

    patterns = itertools.combinations(matching_strings_count.keys(), 3)
    pattern_count = 0

    for a_pattern in patterns:
        pattern_count += matching_strings_count[a_pattern[0]] * \
            matching_strings_count[a_pattern[1]] * \
            matching_strings_count[a_pattern[2]]
    return pattern_count


if __name__ == '__main__':
    matching_strings_count = count_initial_name(people_count=int(input()))

    if sum(matching_strings_count.values()) >= 3:
        print(count_patterns(matching_strings_count))
    else:
        print(0)
