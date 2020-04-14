# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    from itertools import product

    n = int(input())
    ans = list()

    for element in product('ab', repeat=n):
        s = ''.join(map(str, element))

        if s[0] == 'a':
            ans.append(s)

    print('\n'.join(map(str, sorted(ans))))


if __name__ == '__main__':
    main()
