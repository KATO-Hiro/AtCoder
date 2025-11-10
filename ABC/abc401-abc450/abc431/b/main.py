# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    n = int(input())
    w = list(map(int, input().split()))
    q = int(input())
    used = set()

    for _ in range(q):
        p = int(input())
        p -= 1

        if p in used:
            x -= w[p]
            used.discard(p)
        else:
            x += w[p]
            used.add(p)

        print(x)


if __name__ == "__main__":
    main()
