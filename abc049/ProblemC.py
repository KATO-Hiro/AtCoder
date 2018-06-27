'''input
erasedreamerasedream
YES

erasedream
YES

dreameraser
YES

dreamerer
NO

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C


def initialize():
    count = 1
    extracted_s = ''
    return count, extracted_s


if __name__ == '__main__':
    s = input()
    words = ['dream', 'dreamer', 'erase', 'eraser']
    count, extracted_s = initialize()

    while len(s) != len(extracted_s):
        extracted_s = s[len(s) - count:]
        count += 1

        if extracted_s in words:
            s = s[:-len(extracted_s)]
            count, extracted_s = initialize()

    if len(s) == 0:
        print('YES')
    else:
        print('NO')
