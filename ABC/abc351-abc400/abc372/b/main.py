# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    m = int(input())
    threes = [(i, 3**i) for i in range(11)]
    ans = []

    for i, three in threes[::-1]:
        p, q = divmod(m, three)
        m = q
        ans += [i] * p

    print(len(ans))
    print(*ans[::-1])


if __name__ == "__main__":
    main()
