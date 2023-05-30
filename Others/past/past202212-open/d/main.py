# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = input().rstrip()

    cards = [0] * n
    field_count = 0

    for i, si in enumerate(s):
        i %= n
        cards[i] += 1

        if si == "+":
            cards[i] += field_count
            field_count = 0
        elif si == "-":
            field_count += cards[i]
            cards[i] = 0

    print(*cards, sep="\n")


if __name__ == "__main__":
    main()
