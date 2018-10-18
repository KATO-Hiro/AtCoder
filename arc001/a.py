# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    c = Counter(list(input()))
    count_min = min(c.values())

    if len(c.keys()) != 4:
        count_min = 0

    print(max(c.values()), count_min)


if __name__ == '__main__':
    main()
