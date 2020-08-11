# -*- coding: utf-8 -*-


def main():
    from collections import Counter

    n = int(input())
    results = Counter([input() for _ in range(n)])

    for status in ['AC', 'WA', 'TLE', 'RE']:
        print(status + ' x ' + str(results[status]))


if __name__ == '__main__':
    main()
