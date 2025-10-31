# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    scores = list()

    for i in range(n):
        ei, mi = map(int, input().split())
        scores.append((ei + mi, mi, i + 1))

    scores = sorted(scores, key=lambda x: (-x[0], -x[1], -x[2]))
    ans = list()

    for _, _, id in scores:
        ans.append(id)

    print(*ans)


if __name__ == "__main__":
    main()
