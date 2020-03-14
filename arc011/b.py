# -*- coding: utf-8 -*-


def main():
    n = int(input())
    w = input().split()
    d = {'b': '1', 'c': '1',
         'd': '2', 'w': '2',
         't': '3', 'j': '3',
         'f': '4', 'q': '4',
         'l': '5', 'v': '5',
         's': '6', 'x': '6',
         'p': '7', 'm': '7',
         'h': '8', 'k': '8',
         'n': '9', 'g': '9',
         'z': '0', 'r': '0'}
    ans = list()

    for wi in w:
        number = ''

        for s in wi:
            if s.lower() in d:
                number += d[s.lower()]

        if len(number) > 0:
            ans.append(number)

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
