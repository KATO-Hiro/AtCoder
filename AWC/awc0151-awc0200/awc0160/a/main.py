# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    scores = []

    for i in range(n):
        si = sorted(map(int, input().split()))
        score = sum(si[1:-1])
        scores.append((score, i + 1))

    scores.sort(key=lambda x: (-x[0], x[1]))
    print(scores[0][1])


if __name__ == "__main__":
    main()
