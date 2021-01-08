# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    diff = 0
    ab = list()

    for i in range(n):
        ai, bi = map(int, input().split())

        ab.append(2 * ai + bi)
        diff -= ai

    ab = sorted(ab, reverse=True)
    ans = 0

    while diff <= 0:
        diff += ab[ans]
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
