# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())
    ranks = [[] for _ in range(20)]

    for i in range(1, 10 + 1):
        if i % 2 == 1:
            for j in range(1, 20 + 1):
                rank = 40 * (i - 1) // 2 + j
                ranks[j - 1].append(rank)
        else:
            for j in range(20, 0, -1):
                rank = 20 * i + 1 - j
                ranks[j - 1].append(rank)

    print(sum(ranks[t - 1]))


if __name__ == "__main__":
    main()
