'''input
'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    people_count = int(input())

    person_name = list()

    for person in range(people_count):
        person_name.append(str(input()))

    initial_strings = list()

    for name in person_name:
        initial_strings.append(name[0])

    mod_initial_strings = set(initial_strings)

    count = 0

    matching_strings = ['M', 'A', 'R', 'C', 'H']
    matching_strings_count = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}

    for string in matching_strings:
        if string in mod_initial_strings:
            count += initial_strings.count(string)

    for string in initial_strings:
        matching_strings_count[string] += 1

    # TODO: Calc combination.

    if count >= 3:
        print(matching_strings_count)
    else:
        print(0)
