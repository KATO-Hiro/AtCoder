# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    ab = list()

    for i in range(3):
        ai, bi = map(int, input().split())
        ab.append(ai)
        ab.append(bi)

    ab_count = Counter(ab)

    for ab_val in ab_count.values():
        if ab_val == 3:
            print('NO')
            exit()

    print('YES')


if __name__ == '__main__':
    main()
