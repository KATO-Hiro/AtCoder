# -*- coding: utf-8 -*-


# See:
# https://atcoder.jp/contests/abc308/tasks/abc308_c/editorial
class Fraction:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ab = list()

    for i in range(1, n + 1):
        ai, bi = map(int, input().split())
        ab.append((ai, bi))

    ans = sorted(
        range(1, n + 1),
        key=lambda i: Fraction(ab[i - 1][0], ab[i - 1][0] + ab[i - 1][1]),
        reverse=True,
    )

    print(*ans)


if __name__ == "__main__":
    main()
