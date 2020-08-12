# -*- coding: utf-8 -*-


def main():
    n = int(input())
    s = [input() for _ in range(n)]
    days = {'Mon': 'Tue', 'Tue': 'Wed', 'Wed': 'Thu', 'Thu': 'Fri',
            'Fri': 'Sat', 'Sat': 'Sun', 'Sun': 'Mon'}

    for si in s:
        print(days[si])


if __name__ == '__main__':
    main()
