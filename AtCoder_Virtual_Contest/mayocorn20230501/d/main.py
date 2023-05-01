# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))

    # See:
    # https://pekempey.hatenablog.com/entry/2015/12/21/215900
    c = Counter(a)
    s1, s2, s3 = 0, 0, 0

    for value in c.values():
        s1 += value
        s2 += value ** 2
        s3 += value ** 3

    ans = (s1 ** 3 - s1 * s2 - 2 * s1 * s2 + 2 * s3) // 6
    print(ans)


if __name__ == "__main__":
    main()
