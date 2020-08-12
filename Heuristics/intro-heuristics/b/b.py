# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    d = int(input())
    c = list(map(int, input().split()))
    s = [list(map(int, input().split())) for _ in range(d)]
    t = [int(input()) for _ in range(d)]
    last = [0 for _ in range(26)]
    score = 0

    for di in range(1, d + 1):
        ti = t[di - 1]
        score += s[di - 1][ti - 1]

        last[ti - 1] = di

        for j, cj in enumerate(c, 1):
            score -= cj * (di - last[j - 1])

        print(score)


if __name__ == '__main__':
    main()
