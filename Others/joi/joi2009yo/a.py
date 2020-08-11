# -*- coding: utf-8 -*-


def solve(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    diff = end - start

    h, q = divmod(diff, 3600)
    m, s = divmod(q, 60)

    return h, m, s


def main():
    for i in range(3):
        h1, m1, s1, h2, m2, s2 = map(int, input().split())
        result = solve(h1, m1, s1, h2, m2, s2)
        print(result[0], result[1], result[2])


if __name__ == '__main__':
    main()
