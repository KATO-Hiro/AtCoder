# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    s = Counter(input())

    if len(s.keys()) == 2:
        count = 0

        for v in s.values():
            if v == 2:
                count += 1

        if count == 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


if __name__ == '__main__':
    main()
